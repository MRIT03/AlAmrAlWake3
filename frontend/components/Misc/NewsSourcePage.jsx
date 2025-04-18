import React, { useState } from "react";
import './NewsSourcePage.css';

import PostFeed from "../PostFeed/PostFeed";
import PostAuthNavbar from "../Navigation/PostAuthNavbar";

const NewsSourcePage = () => {

    let sourceInfo = {
        isFollowing: true,
        sourceName: "MTV",
        SRR: 3.6,
        headlines: ['Protests indeed continue and continue to continue to continue to Continue', 'Downtown Explosion']
    };

    const [isFollowing, setIsFollowing] = useState(sourceInfo.isFollowing);

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

            <PostFeed /> {/* to be passed a filtered list as a prop - TO-DO */}
        </div>

    );
};

export default NewsSourcePage;
