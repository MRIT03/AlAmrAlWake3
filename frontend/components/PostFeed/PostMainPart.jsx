import React from "react";
import './PostMainPart.css'
import PostTopBar from "./PostTopBar";
import PostBody from "./PostBody";

const PostMainPart = () => {
    return(
        <div className="flex-grow-1">
            <div className="d-flex justify-content-between ms-2">
                <div className="post-main-part-location">
                        <small className="text-muted">  <b> 📍 Byblos </b> </small>
                </div>
                <div className="post-main-part-PTS-timestamp">
                        <small className="text-muted"> <b>Very Suspicious</b> • Fri 11/4/2025 14:15</small>
                </div>
            </div>
            <PostTopBar />
            <PostBody />
        </div>
    );
}

export default PostMainPart;