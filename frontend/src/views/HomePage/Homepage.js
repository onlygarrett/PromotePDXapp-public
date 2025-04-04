import "../../App.css";
import HomeBody from "../../components/Body/Home/HomeBody.js";
import MainCardWithButtons from "../../components/Cards/MainCardWithButtons/MainCardWithButtons.js";
import Carousel from "../../components/Elements/Carousel/Carousel.js";

const HomePage = () => {
  return (
    <div className="App">
      <MainCardWithButtons
        header={"GO-TO PLACE FOR YOUR NEXT LIVE SHOW IN PDX"}
        buttons={["Event Calendar", "Submit to Calendar"]}
      />
      {/* <HomeBody Carousel={Carousel} /> */}
    </div>
  );
};
export default HomePage;
