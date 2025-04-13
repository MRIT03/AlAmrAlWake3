import React from "react";
import './PostBody.css'

const PostBody = () => {

    const actual_content = "Cras vulputate posuere interdum. Fusce sit amet dui ante. Integer non pellentesque magna, quis sollicitudin urna. Vestibulum in lectus ornare, posuere orci vel, faucibus arcu. Duis neque nisi, dignissim et ligula vel, tincidunt iaculis urna. Vivamus eget odio hendrerit, tincidunt libero sed, gravida nisl. Nunc eget orci odio. Suspendisse venenatis tincidunt tortor, non pellentesque tortor imperdiet id. Donec in pellentesque sem. Cras non tellus mattis augue pretium hendrerit quis dictum enim. Maecenas eget enim ut quam rutrum fringilla. Vivamus vestibulum purus non nisi convallis fringilla. Morbi pulvinar viverra neque, maximus faucibus est porta egestas. Aenean eu nibh dolor. Proin ornare turpis sit amet auctor posuere. Donec sagittis aliquam ex, eu dignissim dolor. Proin est mi, accumsan nec convallis vitae, tristique id massa."

    return(
        <div className="post-body">
            <div className="me-2 p-1">
                <p>{actual_content}</p>
            </div>
        </div>
    );
}

export default PostBody;