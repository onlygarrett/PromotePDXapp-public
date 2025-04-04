import { Image } from "react-bootstrap";
import "./AboutBody.css";

const AboutBody = () => {
  return (
    <div id="pdx-about-body" className="pdx-about-body">
      <div className="content-container">
        <div className="about-content">
          Promote PDX was founded by Casey DeArmon and Mackenna Bell in 2022 out
          of love for Portland and its amazing music scene. From DIY house shows
          to arenas, our goal is to help our community find live music easily,
          all while supporting local artists and venues.
        </div>
        <div className="about-content">
          Our team grew in 2023 to include Nat Schmidlin. Nat helps the team
          improve show tracking and create content with his background in
          concert photography/videography.
        </div>
        <div className="about-content">
          We cannot be more thankful for your continued support over the past
          two years. As we grow and evolve, we hope to always provide an easy
          way to find your next show and your new favorite band.
        </div>
        <div className="about-content">
          & as always - support your local venues and bands! Buy tickets! Buy
          drinks! Buy merch!
        </div>
      </div>
      <div className="about-image-container">
        <Image
          className="about-image"
          src={`${process.env.PUBLIC_URL}/fam.JPG`}
          alt="fam"
          rounded
          fluid
        />
      </div>
    </div>
  );
};

export default AboutBody;
