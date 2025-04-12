import React from "react";
import './PostTopBar.css'

const PostTopBar = () => {
    return(
        <div className="post-top-bar">
            <div className="d-flex p-2 justify-content-between">
                <div className="post-top-bar-headline">
                    <strong>This is a very dumb headline but I just want to make sure it's wrapping over lines</strong>
                </div>
            </div>
        </div>
    );
}

export default PostTopBar;