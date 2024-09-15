"use client";
import React, { useState } from 'react';
import { Inbox, Send, Star, Trash, Mail, Plane, PlusCircle, Settings, LogOut, Search } from 'lucide-react';

const EmailClient = () => {
    const [selectedFolder, setSelectedFolder] = useState('inbox');
    const [selectedEmail, setSelectedEmail] = useState<null | number>(null);
    const [searchQuery, setSearchQuery] = useState('');

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

    const filteredEmails = emails.filter(email =>
        email.folder === selectedFolder &&
        (email.subject.toLowerCase().includes(searchQuery.toLowerCase()) ||
            email.sender.toLowerCase().includes(searchQuery.toLowerCase()) ||
            email.preview.toLowerCase().includes(searchQuery.toLowerCase()))
    );

    return (
        <div className="flex h-screen bg-white">
            <div className="w-64 bg-gray-100 border-r flex flex-col justify-between">
                <div className="p-4">
                    <div className="mb-4">
                        <button className="flex items-center w-full py-2 bg-gray-900 text-white rounded-md shadow-md hover:bg-gray-800 transition duration-300 ease-in-out transform hover:scale-105">
                            <PlusCircle className="mr-2 ml-2" size={18} />
                            Compose
                        </button>
                    </div>

                    <ul>
                        {folders.map((folder) => (
                            <li
                                key={folder.name}
                                className={`flex items-center p-2 rounded-md cursor-pointer  ${selectedFolder === folder.name.toLowerCase() ? 'bg-gray-300' : ''
                                    }`}
                                onClick={() => setSelectedFolder(folder.name.toLowerCase())}
                            >
                                <folder.icon className="mr-2" size={18} />
                                {folder.name}
                            </li>
                        ))}
                    </ul>
                </div>

                <div className="p-4 border-t">
                    <div className="flex items-center p-2 cursor-pointer hover:bg-gray-300 rounded-md">
                        <Settings className="mr-2" size={18} />
                        <div className="flex-1">
                            <div className="font-semibold">Settings</div>
                        </div>
                    </div>
                    <div className="flex items-center p-2 cursor-pointer hover:bg-gray-300 rounded-md mt-2">
                        <LogOut className="mr-2" size={18} />
                        <div className="flex-1">
                            <div className="font-semibold">Log Out</div>
                        </div>
                    </div>
                </div>
            </div>

            <div className="w-1/3 bg-white border-r overflow-y-auto text-left">
                <div className="py-4 px-3">
                    <div className="flex items-center mb-4">
                        <input
                            type="text"
                            placeholder="Search emails..."
                            className="flex-1 p-2 border rounded-md"
                            value={searchQuery}
                            onChange={(e) => setSearchQuery(e.target.value)}
                        />
                        <button className="ml-2 p-2 bg-black text-white rounded-md hover:bg-gray-800 transition duration-300 ease-in-out">
                            <Search size={18} />
                        </button>
                    </div>
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


            <div className="flex-1 bg-white p-4 overflow-y-auto text-left">
                {selectedEmail ? (
                    <div>
                        <h3 className="text-xl font-semibold mb-2">
                            {emails.find((e) => e.id === selectedEmail)?.subject}
                        </h3>
                        <p className="text-sm text-gray-600 mb-4">
                            From: {emails.find((e) => e.id === selectedEmail)?.sender}
                        </p>
                        <p className="pb-4">{emails.find((e) => e.id === selectedEmail)?.preview}</p>
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
