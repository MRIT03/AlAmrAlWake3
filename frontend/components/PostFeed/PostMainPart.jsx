import React from "react";
import './PostMainPart.css'
import PostTopBar from "./PostTopBar";
import PostBody from "./PostBody";

const PostMainPart = () => {
    return(
        <div className="flex-grow-1">
            <div className="post-main-part-timestamp">
                    <small className="text-muted"> <b>Very Suspicious</b> • Fri 11/4/2025 14:15</small>
            </div>
            <PostTopBar />
            <PostBody />
        </div>
    );
}

export default PostMainPart;