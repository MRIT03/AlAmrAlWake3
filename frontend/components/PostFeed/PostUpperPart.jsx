import React from "react";
import './PostUpperPart.css'
import PostSideBar from "./PostSideBar";
import PostMainPart from "./PostMainPart";

const PostUpperPart = ({ city, dateTime, sourceName, headline, body, admin, oneHourPassed, PTS, SRR }) => {
    return(
        <div className="d-flex">
            <PostSideBar 
                sourceName = {sourceName} 
                SRR = {SRR} />

            <PostMainPart 
                city = {city} 
                dateTime = {dateTime} 
                headline = {headline}
                body = {body}
                oneHourPassed = {oneHourPassed}
                admin = {admin}
                PTS = {PTS} />
        </div>
    );
}

export default PostUpperPart;