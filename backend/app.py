from flask import Flask, jsonify # type: ignore
import subprocess

app = Flask(__name__)

@app.route('/find-availability', methods=['GET'])
def find_availability():
    try:
        result = subprocess.run(['python3', 'utils/gcal/gcal2.py'], capture_output=True, text=True)
        return jsonify({
            'status': 'success',
            'output': result.stdout,
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'output': str(e)
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
