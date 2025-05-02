import React, { useState } from "react";
import './PostElement.css';
import PostUpperPart from "./PostUpperPart";
import PostBottomBar from "./PostBottomBar";
import AdminBottomBar from "../Admin/AdminBottomBar";
import { useGlobalContext } from "../../src/context/GlobalContext";

const PostElement = ({postData}) => {

  const { isAdmin } = useGlobalContext(); // check if it's admin view

  // "متعاقدو الأساسي الرسمي: نطالب الحكومة بالعودة عن قرارها المجحف"
  // "وللمناسبة، قالت رئيسة الرابطة نسرين شاهين: \"جئنا اليوم لندافع عن كرامة المعلمين قبل أن ندافع عن حقوقهم، جئنا لندافع عن كرامة التعليم والمدرسة الرسمية بأساتذتها (متعاقدين وملاك) وبتلاميذها وأهاليهم، جئنا كيلا يتوهم أهل الباطل بانهم على حق من كثرة الصمت والخضوع والذل. فكل التحايا لكل من حضر من الشمال والجنوب والبقاع وجبل لبنان وبيروت دفاعًا عن كرامته وحقه\".\n\nتابعت: \"نعتصم اليوم بعد اضراب يومين تحذيريين، ومهلة أسبوعين ، ومن ثم الإضراب مستمر منذ أيام، بهدف إعادة اقرار المساعدة الاجتماعية التي كانت تعطى تحت مسمى بدل إنتاجية، وسلبت منا بسبب وقف سلف الخزينة وتغيير النظام المالي بدفع رواتب المعلمين في القطاع التعليمي الرسمي من قبل الحكومة. نحن مع الاصلاح والانقاذ، ولكن، هل من جيبة الأكثر فقرًا يكون الاصلاح؟ نحن مع الحس بالمسؤولية في هذه المرحلة الحساسة من تاريخ لبنان، ولكن هل للعيش شهور من دون راتب ان يترك في الانسان اي احساس؟\".\n\nأضافت: \"نعتصم اليوم امام وزارة التربية وسنمشي في مسيرة الى وزارة المالية، تزامنا مع انعقاد جلسة مجلس الوزراء،  لنقول لوزيرة التربية،  المدارس المغلقة تستدعيك لفتحها، ولنقول لوزير المالية عائلات آلاف الاساتذة يستدعونك لرصد اعتمادات المساعدة الاجتماعية، فمن يغرق القطاع التعليمي لا يمكنه انقاذ البلاد، ولنقول للحكومة مجتمعة، عليك اليوم تحمل مسؤوليتك تجاه ١٤ الف معلم متعاقد. أمَا كان بالامكان رحمة القطاع التعليمي الرسمي وعدم المساس بمكتسبات الاساتذة حتى نهاية العام الدراسي؟ انتم من اوقفتم سلف الخزينة، وانتم من قرّرتم وقف القرار الاستثنائي ببدل الانتاجية\".\n\nوقالت: \"اليوم، المدرسة الرسمية مقفلة الابواب منذ ايام، ومنذ شهر وهي تحتضر، والأساتذة يناشدون ويتأملون اي بارقة أمل، نعم، أعدت وزيرة التربية الدراسة المالية لآلية دفع المساعدة الاجتماعية، ولكنها لم ترفعها الى الحكومة، وعند المطالبة يقال: لا اعتمادات لدى وزير المالية. اقررتم زيادة لاجر الساعة وتعويض موقت لتعويض بدل الانتاجية خلال اشهر التعليم، لتصبح الساعة 8.2$ وحتى تاريخه ليرة واحدة لم تدخل جيبة الاساتذة. قلتم هناك  اموال مرصودة ستحول لصناديق المدارس، وحتى اللحظة اكتر من 2000 استاذ على حساب الصناديق جيوبهم فارغة. قلتم إن الاساتذة المستعان بهم لهم حقوق، ولكن علاقتهم مع اليونيسف، كيف ذلك؟ اساتذة يعلمون لبنانيين بالمدارس الوطنية، كيف لا يكون لهم حق عند وزيرة التربية، واليونيسف تحدد مصيرهم؟ واساتذة الاجرائي على بند المساهمات متروكين للحنان المنان لتتوفر اعتماداتهم. والمعاش الشهري ينتظرونه على الرغم من انهم شهور بلا قبض، ولكنهم (ناطرينو)\"."
  // This is a very dumb headline but I just want to make sure it's wrapping over lines
  // 'Cras vulputate posuere interdum. Fusce sit amet dui ante. Integer non pellentesque magna, quis sollicitudin urna. Vestibulum in lectus ornare, posuere orci vel, faucibus arcu. Duis neque nisi, dignissim et ligula vel, tincidunt iaculis urna. Vivamus eget odio hendrerit, tincidunt libero sed, gravida nisl. Nunc eget orci odio. Suspendisse venenatis tincidunt tortor, non pellentesque tortor imperdiet id. Donec in pellentesque sem. Cras non tellus mattis augue pretium hendrerit quis dictum enim. Maecenas eget enim ut quam rutrum fringilla. Vivamus vestibulum purus non nisi convallis fringilla. Morbi pulvinar viverra neque, maximus faucibus est porta egestas. Aenean eu nibh dolor. Proin ornare turpis sit amet auctor posuere. Donec sagittis aliquam ex, eu dignissim dolor. Proin est mi, accumsan nec convallis vitae, tristique id massa.'
  
  const [postInfo, setPostInfo] = useState(postData);
  
  const postTime = new Date(postInfo.dateTime);
  const now = new Date();
  const oneHourPassed = (now - postTime) > 60 * 60 * 1000; 

  const handleReaction = (index) => {
    const updatedCounters = [...postInfo.counters]; // shallow copy of current counts
    let newSelectedReaction = postInfo.selectedReaction;
    let newFlagCount = postInfo.flagCount;

    if (index === 6) {
      if(updatedCounters[7] === 0){
        updatedCounters[6]++;
        updatedCounters[7] = 1;
      }
      else{
        updatedCounters[6]--;
        updatedCounters[7] = 0;
      }
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

  // TO-DO Command #C

  return (
    <div className="post-element">
      
      <PostUpperPart 
        sourceName = {postInfo.sourceName} 
        city = {postInfo.city} 
        admin = {postInfo.admin}
        dateTime = {postInfo.dateTime}
        headline = {postInfo.headline}
        oneHourPassed={oneHourPassed}
        body = {postInfo.body}
        PTS = {postInfo.PTS}
        SRR = {postInfo.SRR} />

      {/* Conditionally render AdminBottomBar or PostBottomBar based on IIsAdmin */}
      {isAdmin ? (
        <AdminBottomBar
          counters={postInfo.counters}
          oneHourPassed={oneHourPassed} 
          onReact={handleReaction} // child-to-parent callback
          selectedReaction={postInfo.selectedReaction} // mutEx
        />
      ) : (
        <PostBottomBar
          counters={postInfo.counters}
          oneHourPassed={oneHourPassed} 
          onReact={handleReaction} // child-to-parent callback
          selectedReaction={postInfo.selectedReaction} // mutual exclusion
        />
      )}
    </div>
  );
};

export default PostElement;
