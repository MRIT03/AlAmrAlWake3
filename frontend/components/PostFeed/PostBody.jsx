import React, { useState } from "react";
import './PostBody.css';

const PostBody = ({ body }) => {
    const [expanded, setExpanded] = useState(false);

    const toggleExpanded = () => setExpanded(!expanded);

    const maxChars = 300; // tweak for your font/size to fit ~4 lines
    const shouldTruncate = body.length > maxChars;
    const displayText = !expanded && shouldTruncate
        ? body.substring(0, maxChars).trim() + '... '
        : body;

    return (
        <div className="post-body me-2 p-1">
            <p>
                {displayText}
                {shouldTruncate && (
                    <span className="post-body-see-more-link" onClick={toggleExpanded}>
                        {expanded ? 'See less' : 'See more'}
                    </span>
                )}
            </p>
        </div>
    );
};

export default PostBody;
