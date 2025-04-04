import "../../App.css";
import AboutBody from "../../components/Body/About/AboutBody.js";
import MainCard from "../../components/Cards/MainCard/MainCard.js";

const AboutPage = () => {
  return (
    <div className="App" style={{ "text-align": "unset" }}>
      <MainCard header={"About Page"} />
      <AboutBody />
    </div>
  );
};

export default AboutPage;
