import React from "react";
import './PostTopBar.css'

const PostTopBar = ({headline}) => {
    return(
        <div className="post-top-bar">
            <div className="d-flex p-2 justify-content-between">
                <div className="post-top-bar-headline">
                    <strong>{headline}</strong>
                </div>
            </div>
        </div>
    );
}

export default PostTopBar;