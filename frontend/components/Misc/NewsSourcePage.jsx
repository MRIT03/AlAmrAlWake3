import React, { useState, useEffect } from "react";
import './NewsSourcePage.css';

import PostFeed from "../PostFeed/PostFeed";
import PostAuthNavbar from "../Navigation/PostAuthNavbar";
import { useLocation } from "react-router-dom";

// point this at your backend (or "" if you use a CRA proxy)
const API_BASE_URL = process.env.REACT_APP_API_URL || "http://localhost:5120";

const NewsSourcePage = () => {
  const location = useLocation();
  const sourceNameFromQuery = new URLSearchParams(location.search).get("source");

  // TODO: pull real userId & real sourceId mapping here
  const userId   = 1;
  const sourceId = 42;

  const [sourceInfo, setSourceInfo]   = useState(null);
  const [isFollowing, setIsFollowing] = useState(false);

  // fetch initial follow state
  useEffect(() => {
    if (!sourceNameFromQuery) return;

    const fetchFollowState = async () => {
      try {
        const url = `${API_BASE_URL}/api/User/FollowsSource?userId=${userId}&sourceId=${sourceId}`;
        const res = await fetch(url, { method: "GET" });

        if (!res.ok) {
          console.error("Error fetching follow state:", res.statusText);
          return;
        }

        const follows = await res.json(); // true|false
        setSourceInfo({ sourceName: sourceNameFromQuery });
        setIsFollowing(follows);
      } catch (err) {
        console.error("Fetch error:", err);
      }
    };

    fetchFollowState();
  }, [sourceNameFromQuery, userId, sourceId]);

  // call this when the user clicks "Follow"
  const handleFollow = async () => {
    if (isFollowing) return;  // do nothing if already following

    try {
      const url = `${API_BASE_URL}/api/User/Follow?userId=${userId}&sourceId=${sourceId}`;
      const res = await fetch(url, { method: "POST" });

      if (res.ok) {
        setIsFollowing(true);
      } else {
        console.error("Failed to follow:", res.status, res.statusText);
      }
    } catch (err) {
      console.error("Follow error:", err);
    }
  };

  if (!sourceInfo) {
    return <div className="news-source-page-wrapper">Loading...</div>;
  }

  return (
    <div className="news-source-page-wrapper">
      <PostAuthNavbar />

      <div className="outlet-container">
        <i className="bi bi-newspaper news-source-page-avatar"></i>
        <h4 className="news-outlet-name">{sourceInfo.sourceName}</h4>

        <button
          className={`follow-toggle-btn ${isFollowing ? 'following' : 'not-following'}`}
          onClick={handleFollow}
        >
          {isFollowing ? 'Following' : 'Follow'}
        </button>
      </div>

      <PostFeed /> {/* TODO: filter posts by source */}
    </div>
  );
};

export default NewsSourcePage;
