import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import './OutletCard.css';

const OutletCard = ({ sourceName, SRR, followingStatus }) => {

    const [isFollowing, setIsFollowing] = useState(followingStatus);

    const generateStars = (SRR) => {
        const stars = [];
        const doubledRating = Math.floor(SRR*2);
        const fullStars = Math.floor(doubledRating/2)
        const hasHalfStar = doubledRating % 2 === 1;
        // for loop to put <i className="bi bi-star-fill"></i> fullStars number of times
        for (let i = 0; i < fullStars; i++) {
            stars.push(<i key={`full-${i}`} className="bi bi-star-fill custom-star"></i>);
        }

        if (hasHalfStar) {
            stars.push(<i key="half" className="bi bi-star-half custom-star"></i>);
        }       

        // for loop to put <i className="bi bi-star"></i> 5-fullStars number of times or -1 if half was added
        const remaining = 5 - fullStars - (hasHalfStar ? 1 : 0);
        for (let i = 0; i < remaining; i++) {
            stars.push(<i key={`empty-${i}`} className="bi bi-star custom-star"></i>);
        }
        
        return stars;
    };

    const mapToSRRLabel = (SRR) => {
        if (SRR >= 4) {
            return "Highly Reliable";
        } else if (SRR >= 3) {
            return "Reliable";
        } else if (SRR >= 2) {
            return "Moderately Reliable";
        } else if (SRR >= 1) {
            return "Unreliable";
        } else {
            return "Very Unreliable";
        }
    };

    const navigate = useNavigate(); // ✅ define navigate
    
    const navigateToNewsSourcePage = (sourceName) => {
        const encodedSource = encodeURIComponent(sourceName);
        navigate(`/outlet?source=${encodedSource}`);
    };

    return (
        
        <div className="outlet-card-wrapper">
            <div className="outlet-side-bar-wrapper">
                <div className="post-side-bar">
                    <div style={{ width: '140px' }}>
                        <div className="post-side-bar-source-info">
                            {/* <b>Avatar</b> */}
                            <div className="avatar mx-auto mb-2 mt-3">
                                <i className="bi bi-newspaper"></i>
                            </div>

        
                            <h3 className="post-side-bar-sourceName mb-1">{sourceName}</h3>

                            {/* Star Rating */}
                            <div className="text-warning mb-1">
                                {generateStars(SRR)}
                            </div>
                            <div className="post-side-bar-SRR"><b> {SRR} | {mapToSRRLabel(SRR)} </b></div>
                            <button
                                className={`outlet-follow-toggle-btn ${isFollowing ? 'following' : 'not-following'}`}
                                onClick={() => setIsFollowing(prev => !prev)}
                            >
                                {isFollowing ? 'Following' : 'Follow'}
                            </button>
                            <button
                                className={`outlet-follow-toggle-btn`}
                                onClick={() => navigateToNewsSourcePage(sourceName)}
                            >
                                <i className="bi bi-box-arrow-up-right" style={{ marginRight: '0.4rem' }}></i>
                                Visit Page
                            </button>
                        </div>
                    </div>

                </div>
            </div>
        </div>

    );
};

export default OutletCard;
