import React from "react";
import 'bootstrap-icons/font/bootstrap-icons.css';
import './PostBottomBar.css';

const PostBottomBar = () => {
    const reactions = [
        { icon: "hand-thumbs-up", label: "Like" },
        { icon: "heart", label: "Love" },
        { icon: "hand-index-thumb", label: "Support" },
        { icon: "lightbulb", label: "Insightful" },
        { icon: "emoji-frown", label: "Sad" },
        { icon: "emoji-angry", label: "Angry" },
    ];

    return (
        <div className="post-bottom-bar px-4 py-3">
            <div className="d-flex justify-content-between align-items-center flex-wrap">
                {/* Reactions section */}
                <div className="d-flex flex-wrap gap-3">
                    {reactions.map((reaction, index) => (
                        <div key={index} className="d-flex align-items-center">
                            <button
                                className="btn btn-outline-secondary rounded-circle d-flex align-items-center justify-content-center"
                                style={{ width: '40px', height: '40px' }}
                            >
                                <i className={`bi bi-${reaction.icon}`}></i>
                            </button>
                            <span className="ms-2 text-muted small">0</span>
                        </div>
                    ))}
                </div>

                {/* Flag section */}
                <div className="d-flex align-items-center mt-3 mt-md-0">
                    
                    <button
                        className="btn btn-outline-danger d-flex align-items-center"
                        style={{ borderRadius: '20px', padding: '4px 10px' }}
                    >
                        <i className="bi bi-flag me-2"></i>
                        Flag as suspicious
                    </button>

                    <span className="ms-2 text-muted small">0</span>
                </div>
            </div>
        </div>
    );
};

export default PostBottomBar;
