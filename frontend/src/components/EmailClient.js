import React, { useState } from 'react';
import { Inbox, Send, Star, Trash, Mail, Plane } from 'lucide-react';

const EmailClient = () => {
    const [selectedFolder, setSelectedFolder] = useState('inbox');
    const [selectedEmail, setSelectedEmail] = useState(null);

    const folders = [
        { name: 'Inbox', icon: Inbox },
        { name: 'Sent', icon: Send },
        { name: 'Starred', icon: Star },
        { name: 'Trash', icon: Trash },
    ];

    const emails = [
        {
            id: 1,
            subject: 'Time to Check-in: Flight DL1234 from Atlanta to New York',
            sender: 'checkin@delta.com',
            preview: 'It’s time to check in for your flight DL1234 from Atlanta to New York. Your flight departs on September 15th...',
            folder: 'inbox'
        },
        {
            id: 2,
            subject: 'Check-in Now Available: Flight DL5678 from New York to Los Angeles',
            sender: 'checkin@delta.com',
            preview: 'Check-in is now available for your flight DL5678 from New York to Los Angeles. Please confirm your seat...',
            folder: 'inbox'
        },
        {
            id: 3,
            subject: 'Don’t Forget to Check-in: Flight DL9101 from Los Angeles to Chicago',
            sender: 'checkin@delta.com',
            preview: 'Check-in is required for your flight DL9101 from Los Angeles to Chicago. Complete your check-in to secure your seat...',
            folder: 'inbox'
        },
    ];

    const filteredEmails = emails.filter(email => email.folder === selectedFolder);

    return (
        <div className="flex h-screen bg-gray-100">
            {/* Sidebar */}
            <div className="w-64 bg-white border-r">
                <div className="p-4">
                    <h2 className="text-3xl font-semibold mb-4">Email Client</h2>
                    <ul>
                        {folders.map((folder) => (
                            <li
                                key={folder.name}
                                className={`flex items-center p-2 cursor-pointer  ${selectedFolder === folder.name.toLowerCase() ? 'bg-blue-100' : ''
                                    }`}
                                onClick={() => setSelectedFolder(folder.name.toLowerCase())}
                            >
                                <folder.icon className="mr-2" size={18} />
                                {folder.name}
                            </li>
                        ))}
                    </ul>
                </div>
            </div>

            {/* Email list */}
            <div className="w-1/3 bg-white border-r overflow-y-auto text-left">
                <div className="p-4">
                    <h3 className="text-2xl font-semibold mb-4">
                        {selectedFolder.charAt(0).toUpperCase() + selectedFolder.slice(1)}
                    </h3>
                    <ul>
                        {filteredEmails.map((email) => (
                            <li
                                key={email.id}
                                className={`p-2 cursor-pointer ${selectedEmail === email.id ? 'bg-gray-100 rounded-md' : ''
                                    }`}
                                onClick={() => setSelectedEmail(email.id)}
                            >
                                <div className="font-semibold">{email.subject}</div>
                                <div className="text-sm text-gray-600">{email.sender}</div>
                                <div className="text-sm text-gray-500 truncate">{email.preview}</div>
                            </li>
                        ))}
                    </ul>
                </div>
            </div>

            {/* Email viewer */}
            <div className="flex-1 bg-white p-4 overflow-y-auto text-left">
                {selectedEmail ? (
                    <div>
                        <h3 className="text-xl font-semibold mb-2">
                            {emails.find((e) => e.id === selectedEmail).subject}
                        </h3>
                        <p className="text-sm text-gray-600 mb-4">
                            From: {emails.find((e) => e.id === selectedEmail).sender}
                        </p>
                        <p className="pb-4">{emails.find((e) => e.id === selectedEmail).preview}</p>
                        <button className="flex items-center justify-center px-4 py-2 bg-blue-500 text-white rounded-md shadow-md hover:bg-blue-600 transition duration-300 ease-in-out transform hover:scale-105">
                            <Plane className="mr-2" size={18} />
                            Check In
                        </button>
                    </div>
                ) : (
                    <div className="flex items-center justify-center h-full text-gray-500">
                        <Mail className="mr-2" size={24} />
                        Select an email to view its content
                    </div>
                )}
            </div>
        </div>
    );
};

export default EmailClient;