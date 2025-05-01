import React, { useState, useEffect } from 'react';
import axios from "axios";
import './PostFeed.css';
import PostElement from './PostElement';

const PostFeed = ({ filterOutlet = false }) => {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:5120/api/Posts/GetFeedPosts") // 
      .then(response => {
        setPosts(response.data);
      })
      .catch(error => {
        console.error("Error fetching posts:", error);
      })
  }, []);
  
  if(!filterOutlet){ 
    useEffect(() => {})
  }
  // else{ TO-DO Query #5 Change Port Number

  // }

  useEffect(() => { // MANUAL FETCHING FROM POSTS.JSON
    fetch('/posts.json')
      .then(res => {
        if (!res.ok) throw new Error("Failed to load posts");
        return res.json();
      })
      .then(data => setPosts(data))
      .catch(err => console.error("Error loading posts:", err));
  }, []);
  
  return (
    <div>
      {posts.map((post, index) => (
        <PostElement key={index} postData={post} />
      ))}
    </div>
  );
};

export default PostFeed;
