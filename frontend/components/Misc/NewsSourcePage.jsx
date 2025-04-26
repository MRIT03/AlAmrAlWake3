import React, { useState, useEffect } from "react";
import './NewsSourcePage.css';

import PostFeed from "../PostFeed/PostFeed";
import PostAuthNavbar from "../Navigation/PostAuthNavbar";
import { useLocation } from "react-router-dom";

const NewsSourcePage = () => {
    const location = useLocation();
    const queryParams = new URLSearchParams(location.search);
    const sourceNameFromQuery = queryParams.get("source");

    const [isFollowing, setIsFollowing] = useState(false);

    // TO-DO Command #B

    useEffect(() => { // To-DO Query #3
        if (sourceNameFromQuery) {
            const fetchIsFollowing = async () => {
                try {
                    const res = await fetch(`/api/following/check?sourceName=${encodeURIComponent(sourceNameFromQuery)}`, {
                        method: 'GET',
                        // credentials: 'include', // Uncomment this if authentication (like cookies or tokens) is set up later
                        headers: {
                            'Content-Type': 'application/json',
                        },
                    });

                    if (!res.ok) {
                        throw new Error('Network response was not ok');
                    }

                    const data = await res.json();

                    setIsFollowing(data.isFollowing);
                } catch (error) {
                    console.error('Error fetching follow status:', error);
                }
            };

            /* 
            Notes:
            - Assumption: API base URL is same as frontend server or proxied (no port specified).
            - If backend runs on a different port (e.g., localhost:5000), set up a proxy in package.json or change the fetch URL.
            - Authentication is not yet implemented, so 'credentials: include' is commented out for now.
            */
    
            fetchIsFollowing();
        }
    }, [sourceNameFromQuery]);    

    return (
        <div className="news-source-page-wrapper">
            <PostAuthNavbar />

            <div className='outlet-container'>
                <i className="bi bi-newspaper news-source-page-avatar"></i>
                <h4 className='news-outlet-name'>{sourceNameFromQuery}</h4>

                <button
                    className={`follow-toggle-btn ${isFollowing ? 'following' : 'not-following'}`}
                    onClick={() => setIsFollowing(prev => !prev)}
                >
                    {isFollowing ? 'Following' : 'Follow'}
                </button>
            </div>

            <PostFeed /> {/* TODO: outletFilter = true */}
        </div>
    );
};

export default NewsSourcePage;