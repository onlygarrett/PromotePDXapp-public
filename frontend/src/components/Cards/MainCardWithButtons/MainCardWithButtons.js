import { Link } from "react-router-dom";
import NormalButton from "../../../components/Elements/Button/NormalButton/NormalButton.js";
import "./MainCardWithButtons.css";

function MainCardWithButtons({ header, buttons }) {
  return (
    <div className="main-card-with-buttons-wrapper">
      <div className="main-card-content">
        <div className="main-card-header">
          <div className="main-card-header-text">
            GO-TO PLACE FOR YOUR NEXT LIVE SHOW IN PDX
          </div>
          <img className="main-card-header-text-svg" src="/Container-Tan.svg" alt="Container Tan" />

        </div>
        <div className="button-wrapper">
          {buttons.map((button, index) =>
            button === "Event Calendar" ? (
              <Link key={`link_item_${index}`} to="/events">
                <NormalButton
                  key={`button_item_${index}`}
                  index={`button_item_${index}`}
                  class="btn"
                  text={button}
                ></NormalButton>
              </Link>
            ) : (
              <NormalButton
                key={`button_item_${index}`}
                index={`button_item_${index}`}
                class="btn"
                text={button}
              ></NormalButton>
            )
          )}
        </div>
      </div>
    </div>
  );
}

export default MainCardWithButtons;
