import React, { useState, useEffect } from "react";
import './NewsSourcePage.css';

import PostFeed from "../PostFeed/PostFeed";
import PostAuthNavbar from "../Navigation/PostAuthNavbar";
import { useLocation } from "react-router-dom";

const NewsSourcePage = () => {
    const location = useLocation();
    const queryParams = new URLSearchParams(location.search);
    const sourceNameFromQuery = queryParams.get("source");

    const [sourceInfo, setSourceInfo] = useState(null);
    const [isFollowing, setIsFollowing] = useState(false);

    useEffect(() => {
        if (sourceNameFromQuery) {
            const fetchSourceInfo = async () => {
                // TO-DO Query: Replace with actual API call
                // const res = await fetch(`/api/news-source?name=${sourceNameFromQuery}`);
                // const data = await res.json();

                // Simulated data
                const data = {
                    isFollowing: true,
                    sourceName: sourceNameFromQuery,
                    SRR: 3.6,
                    headlines: [
                        'Protests indeed continue and continue to continue to continue to Continue',
                        'Downtown Explosion'
                    ]
                };

                setSourceInfo(data);
                setIsFollowing(data.isFollowing);
            };

            fetchSourceInfo();
        }
    }, [sourceNameFromQuery]);

    if (!sourceInfo) {
        return <div className="news-source-page-wrapper">Loading...</div>;
    }

    return (
        <div className="news-source-page-wrapper">
            <PostAuthNavbar />

            <div className='outlet-container'>
                <i className="bi bi-newspaper news-source-page-avatar"></i>
                <h4 className='news-outlet-name'>{sourceInfo.sourceName}</h4>

                <button
                    className={`follow-toggle-btn ${isFollowing ? 'following' : 'not-following'}`}
                    onClick={() => setIsFollowing(prev => !prev)}
                >
                    {isFollowing ? 'Following' : 'Follow'}
                </button>
            </div>

            <PostFeed /> {/* TODO: Pass filtered list based on source */}
        </div>
    );
};

export default NewsSourcePage;