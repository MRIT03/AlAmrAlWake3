import React from "react";
import './PostMainPart.css'
import PostTopBar from "./PostTopBar";
import PostBody from "./PostBody";

const PostMainPart = ({city, dateTime, headline, body, admin, oneHourPassed, PTS}) => {

    const mapToPTSLabel = (oneHourPassed, admin, PTS) => {
        if (!oneHourPassed) {
            return "Recent";
        }
        if (admin !== "") { // if forced by the admin after 1 hr
            return admin;
        }
        if (PTS >= 80) {
            return "Not Suspicious";
        } else if (PTS >= 50) {
            return "Suspicious";
        } else if (PTS >= 20) {
            return "Very Suspicious";
        } else {
            return "Critically Suspicious";
        }
    };
    

    return(
        <div className="flex-grow-1">
            <div className="d-flex justify-content-between ms-2">
                <div className="post-main-part-location">
                        <small className="text-muted">  <b> 📍 {city} </b> </small>
                </div>
                <div className="post-main-part-PTS-timestamp">
                        <small className="text-muted"> <b>{mapToPTSLabel(oneHourPassed, admin, PTS)}</b> • 🕗 {dateTime}</small>
                </div>
            </div>
            <PostTopBar headline = {headline} />
            <PostBody body = {body} />
        </div>
    );
}

export default PostMainPart;