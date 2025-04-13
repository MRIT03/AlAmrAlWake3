import React from "react";
import './PostFeed.css'
import PostUpperPart from "./PostUpperPart";
import PostBottomBar from "./PostBottomBar";

const PostFeed = () => {
    return(
        <div> {/* bottom margin of 1rem */}
            <div className="post-feed">
                <div>
                    <PostUpperPart />
                    <PostBottomBar />
                </div>
            </div>
        </div>
    );
}

export default PostFeed;