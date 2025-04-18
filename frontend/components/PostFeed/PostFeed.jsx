import React, { useState, useEffect } from 'react';
import PostElement from './PostElement';

const PostFeed = () => {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
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
