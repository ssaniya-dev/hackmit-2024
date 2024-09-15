import os.path
import datetime
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def calauth():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    service = build('calendar', 'v3', credentials=creds)
    return service

def freeSlots(busy_times, start_time, end_time):
    free_slots = []
    current_time = start_time

    for busy_time in busy_times:
        busy_start = datetime.datetime.fromisoformat(busy_time['start'][:-1])
        busy_end = datetime.datetime.fromisoformat(busy_time['end'][:-1])
        if current_time < busy_start:
            free_slots.append((current_time.isoformat(), busy_start.isoformat()))
        current_time = max(current_time, busy_end)

    if current_time < end_time:
        free_slots.append((current_time.isoformat(), end_time.isoformat()))

    return free_slots

def checkAvail(service, days, time_range):
    calendar_id = 'primary'
    free_slots = []

    for day in days:
        day_date = nextWeekday(day)
        start = datetime.datetime.combine(day_date, datetime.time(9, 0))
        end = datetime.datetime.combine(day_date, datetime.time(17, 0))
        body = {
            "timeMin": start.isoformat() + 'Z',
            "timeMax": end.isoformat() + 'Z',
            "items": [{"id": calendar_id}],
        }

        events_result = service.freebusy().query(body=body).execute()
        busy_times = events_result['calendars'][calendar_id]['busy']
        free_slots += freeSlots(busy_times, start, end)
    
    return free_slots

def nextWeekday(weekday_name):
    days_map = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2,'Thursday': 3,'Friday': 4}
    today = datetime.date.today()
    target_day = days_map.get(weekday_name, 0)

    days_ahead = target_day - today.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return today + datetime.timedelta(days_ahead)

def freeSlotsOutput(free_slots):
    formatted_slots = {}
    for start, end in free_slots:
        start_dt = datetime.datetime.fromisoformat(start)
        end_dt = datetime.datetime.fromisoformat(end)
        day_str = start_dt.strftime("%A, %B %d")
        time_str = f"{start_dt.strftime('%I:%M %p').lstrip('0')} - {end_dt.strftime('%I:%M %p').lstrip('0')}"
        if day_str in formatted_slots:
            formatted_slots[day_str].append(time_str)
        else:
            formatted_slots[day_str] = [time_str]

    out1 = "Hi!\n\nIt's great to hear from you, here's my availability in the coming week for an interview:\n\n"
    
    for day, times in formatted_slots.items():
        times_str = ", ".join(times)
        out1 += f"{day}: {times_str}\n"
    out1 += "\nIf you'd like for me to provide more availability, I'd be happy to do so!\n\nThanks,\nNeil"    
    return out1

if __name__ == '__main__':
    service = calauth()
    days = ['Monday', 'Tuesday', 'Friday']
    time_range = [('9:00 AM', '5:00 PM')]
    free_slots = checkAvail(service, days, time_range)
    email_content = freeSlotsOutput(free_slots)
    print(email_content)