import React from "react";
import './PostUpperPart.css'
import PostSideBar from "./PostSideBar";
import PostMainPart from "./PostMainPart";

const PostUpperPart = () => {
    return(
        <div className="d-flex">
            <PostSideBar />
            <PostMainPart />
        </div>
    );
}

export default PostUpperPart;