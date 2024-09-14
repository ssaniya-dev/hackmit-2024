import React, { useState } from 'react';
import { Inbox, Send, Star, Trash, Mail } from 'lucide-react';

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
        { id: 1, subject: 'Welcome to our service', sender: 'info@example.com', preview: 'Thank you for signing up...', folder: 'inbox' },
        { id: 2, subject: 'Your invoice', sender: 'billing@example.com', preview: 'Please find attached your latest invoice...', folder: 'inbox' },
        { id: 3, subject: 'Meeting reminder', sender: 'team@example.com', preview: 'Don\'t forget our team meeting tomorrow at 10 AM...', folder: 'inbox' },
    ];

    const filteredEmails = emails.filter(email => email.folder === selectedFolder);

    return (
        <div className="flex h-screen bg-gray-100">
            {/* Sidebar */}
            <div className="w-64 bg-white border-r">
                <div className="p-4">
                    <h2 className="text-xl font-semibold mb-4">Email Client</h2>
                    <ul>
                        {folders.map((folder) => (
                            <li
                                key={folder.name}
                                className={`flex items-center p-2 cursor-pointer ${selectedFolder === folder.name.toLowerCase() ? 'bg-blue-100' : ''
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
            <div className="w-1/3 bg-white border-r overflow-y-auto">
                <div className="p-4">
                    <h3 className="text-lg font-semibold mb-4">
                        {selectedFolder.charAt(0).toUpperCase() + selectedFolder.slice(1)}
                    </h3>
                    <ul>
                        {filteredEmails.map((email) => (
                            <li
                                key={email.id}
                                className={`p-2 cursor-pointer ${selectedEmail === email.id ? 'bg-blue-100' : ''
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
            <div className="flex-1 bg-white p-4 overflow-y-auto">
                {selectedEmail ? (
                    <div>
                        <h3 className="text-xl font-semibold mb-2">
                            {emails.find((e) => e.id === selectedEmail).subject}
                        </h3>
                        <p className="text-sm text-gray-600 mb-4">
                            From: {emails.find((e) => e.id === selectedEmail).sender}
                        </p>
                        <p>{emails.find((e) => e.id === selectedEmail).preview}</p>
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