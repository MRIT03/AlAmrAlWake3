import React, { useState } from "react";
import './FeedPage.css';
import PostFeed from "./PostFeed";
import PostAuthNavbar from "../Navigation/PostAuthNavbar";

const FeedPage = () => {

    return (
        <div className="feed-page">
            <PostAuthNavbar />
            <PostFeed />
        </div>
    );
};

export default FeedPage;
