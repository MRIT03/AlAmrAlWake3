import React from "react";
import 'bootstrap-icons/font/bootstrap-icons.css';
import './PostSideBar.css'

const PostSideBar = () => {
    return(
        <div className="post-side-bar">
                <div style={{ width: '160px' }}>
                    <div className="post-side-bar-source-info">
                        {/* <b>Avatar</b> */}
                        <div className="rounded-circle bg-secondary mx-auto mb-2 mt-3" style={{ width: '50px', height: '50px' }}></div>
      
                        <h3>MTV</h3>

                        {/* Star Rating */}
                        <div className="text-warning mb-1">
                            <i className="bi bi-star-fill"></i>
                            <i className="bi bi-star-fill"></i>
                            <i className="bi bi-star-fill"></i>
                            <i className="bi bi-star-half"></i>
                            <i className="bi bi-star"></i>
                        </div>
                        <div><b> 3.6 | Reliable </b></div>
                    </div>
                </div>

        </div>
    );
}

export default PostSideBar;