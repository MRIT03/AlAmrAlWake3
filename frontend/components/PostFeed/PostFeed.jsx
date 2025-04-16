import React, { useState } from "react";
import './PostFeed.css';
import PostUpperPart from "./PostUpperPart";
import PostBottomBar from "./PostBottomBar";

const PostFeed = () => {
  // Single source of truth for all post-related state
  const [postInfo, setPostInfo] = useState({
    city: 'Beirut',
    selectedReaction: null,
    counters: [0, 0, 0, 0, 0, 0], // index 0–5 are different reaction types
    headlines: "This is a very dumb headline but I just want to make sure it's wrapping over lines",
    body: 'Cras vulputate posuere interdum. Fusce sit amet dui ante. Integer non pellentesque magna, quis sollicitudin urna. Vestibulum in lectus ornare, posuere orci vel, faucibus arcu. Duis neque nisi, dignissim et ligula vel, tincidunt iaculis urna. Vivamus eget odio hendrerit, tincidunt libero sed, gravida nisl. Nunc eget orci odio. Suspendisse venenatis tincidunt tortor, non pellentesque tortor imperdiet id. Donec in pellentesque sem. Cras non tellus mattis augue pretium hendrerit quis dictum enim. Maecenas eget enim ut quam rutrum fringilla. Vivamus vestibulum purus non nisi convallis fringilla. Morbi pulvinar viverra neque, maximus faucibus est porta egestas. Aenean eu nibh dolor. Proin ornare turpis sit amet auctor posuere. Donec sagittis aliquam ex, eu dignissim dolor. Proin est mi, accumsan nec convallis vitae, tristique id massa.',
    sourceName: "MTV",
    RSS: 3.6,
    PTS: 40,
    flagCount: 0, // 1 = flagged, 0 = not flagged
  });

  /**
   * Handles all reactions (emoji index 0–5) and flag toggling.
   * - Clicking a reaction toggles it; removes old reaction if switching.
   * - Clicking flag toggles it independently of emoji reactions.
   */
  const handleReaction = (index) => {
    const updatedCounters = [...postInfo.counters]; // shallow copy of current counts
    let newSelectedReaction = postInfo.selectedReaction;
    let newFlagCount = postInfo.flagCount;

    if (index === 'flag') {
      // Toggle flag (0 ↔ 1)
      newFlagCount = postInfo.flagCount === 0 ? 1 : 0;
    } else {
      // Toggle selected reaction (and update counter)
      if (postInfo.selectedReaction === index) {
        updatedCounters[index]--; // remove if same reaction clicked again
        newSelectedReaction = null;
      } else {
        // Remove previous selection (if any)
        if (postInfo.selectedReaction !== null) {
          updatedCounters[postInfo.selectedReaction]--;
        }
        updatedCounters[index]++; // add new one
        newSelectedReaction = index;
      }
    }

    // Update all changes in postInfo
    setPostInfo({
      ...postInfo,
      counters: updatedCounters,
      selectedReaction: newSelectedReaction,
      flagCount: newFlagCount,
    });
  };

  return (
    <div className="post-feed">
      <PostUpperPart />
      <PostBottomBar
        counters={postInfo.counters}
        flagCount={postInfo.flagCount}
        onReact={handleReaction} // unified callback
        selectedReaction={postInfo.selectedReaction} // pass down to highlight selected emoji
        isFlagged={postInfo.flagCount > 0} // flag state derived directly from postInfo
      />
    </div>
  );
};

export default PostFeed;
