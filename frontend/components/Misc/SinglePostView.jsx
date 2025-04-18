import React, { useState } from "react";
import './SinglePostView.css';
import PostAuthNavbar from "../Navigation/PostAuthNavbar";
import PostElement from "../PostFeed/PostElement";

const SinglePostView = () => {

    let postData = {
        "city": "Beirut",
        "selectedReaction": null,
        "counters": [120, 10, 0, 0, 3, 1, 2, 0],
        "headline": "متعاقدو الأساسي الرسمي: نطالب الحكومة بالعودة عن قرارها المجحف",
        "body": "وللمناسبة، قالت رئيسة الرابطة نسرين شاهين: \"جئنا اليوم لندافع عن كرامة المعلمين...\"",
        "sourceName": "MTV",
        "SRR": 3.6,
        "PTS": 78,
        "dateTime": "4/18/2025 15:53",
        "admin": ""
    };

    return (
        <div className="single-post-view">
            <PostAuthNavbar />

            <div className="single-post-view-back-button-wrapper">
                <button
                    className="single-post-view-back-button"
                    onClick={() => window.history.back()} // or router (to see later)
                >
                    <i className="bi bi-arrow-left me-2"></i>
                    Back To Map
                </button>
            </div>


            <div className="single-post-wrapper">
                <PostElement postData={postData} />
            </div>
        </div>
    );
};

export default SinglePostView;
