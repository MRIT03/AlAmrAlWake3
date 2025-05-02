import React, { useState } from "react";
import 'bootstrap-icons/font/bootstrap-icons.css';
import './AdminBottomBar.css';

const AdminBottomBar = ({ counters, onReact, selectedReaction, oneHourPassed }) => {

    // TO-DO Command #A

    // State to track which flag action ("Verify" or "Fake News") is selected
    const [selectedFlag, setSelectedFlag] = useState(null);

    // Handle button click to toggle mutual exclusivity between "Verify" and "Fake News"
    const handleFlagClick = (flag) => {
        if (selectedFlag === flag) {
            setSelectedFlag(null);  // Deselect if already selected
        } else {
            setSelectedFlag(flag);  // Select the clicked flag
        }
    };

    const reactions = [
        { icon: "hand-thumbs-up", fillIcon: "hand-thumbs-up-fill", label: "Like", color: "blue", counter: counters[0] },
        { icon: "heart", fillIcon: "heart-fill", label: "Love", color: "purple", counter: counters[1] },
        { icon: "emoji-surprise", fillIcon: "emoji-surprise-fill", label: "Wow", color: "green", counter: counters[2] },
        { icon: "lightbulb", fillIcon: "lightbulb-fill", label: "Insightful", color: "goldenrod", counter: counters[3] },
        { icon: "emoji-tear", fillIcon: "emoji-tear-fill", label: "Sad", color: "deepskyblue", counter: counters[4] },
        { icon: "emoji-angry", fillIcon: "emoji-angry-fill", label: "Angry", color: "red", counter: counters[5] },
    ];

    return (
        <div className="post-bottom-bar px-4 py-3">
            <div className="d-flex justify-content-between align-items-center flex-wrap">
                <div className="d-flex flex-wrap gap-3">
                    {reactions.map((reaction, index) => {
                        const isSelected = selectedReaction === index;
                        const iconClass = reaction.fillIcon;
                        const colorClass = `reaction-${reaction.label.toLowerCase()}`;

                        return (
                            <div key={index} className="d-flex align-items-center">
                                <button
                                    className="admin-reaction-btn"
                                    onClick={null}
                                    disabled
                                    title={reaction.label}
                                >
                                    <i className={`bi bi-${iconClass}`}></i>
                                </button>

                                <span className="ms-2 text-muted small">{reaction.counter}</span>
                            </div>
                        );
                    })}
                </div>

                {/* Flag section */}
                {oneHourPassed && (
                    <div className="admin-actions">
                        <button
                            className={`flag-verify ${selectedFlag === 'verify' ? 'active' : ''}`}
                            onClick={() => handleFlagClick('verify')}
                        >
                            Verify
                        </button>
                        <button
                            className={`flag-fake ${selectedFlag === 'fake' ? 'active' : ''}`}
                            onClick={() => handleFlagClick('fake')}
                        >
                            Fake News
                        </button>
                        <button className="flag-delete">Delete</button>
                    </div>
                )}
            </div>
        </div>
    );
};

export default AdminBottomBar;
