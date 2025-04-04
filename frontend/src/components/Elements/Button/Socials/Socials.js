import React from "react";
import "./Socials.css";

const SocialsButton = () => {
  return (
    <div className="main">
      <div className="up">
        <button
          className="card1"
          onClick={() =>
            window.open("https://www.instagram.com/promotepdx/", "_blank")
          }
        >
          <svg
            className="instagram"
            fillRule="nonzero"
            height="30px"
            width="30px"
            viewBox="0,0,256,256"
            xmlnsXlink="http://www.w3.org/1999/xlink"
            xmlns="http://www.w3.org/2000/svg"
          >
            <g
              style={{ mixBlendMode: "normal" }}
              textAnchor="none"
              fontSize="none"
              fontWeight="none"
              fontFamily="none"
              strokeDashoffset={0}
              strokeMiterlimit={10}
              strokeLinejoin="miter"
              strokeLinecap="butt"
              strokeWidth={1}
              stroke="none"
              fillRule="nonzero"
            >
              <g transform="scale(8,8)">
                <path d="M11.46875,5c-3.55078,0 -6.46875,2.91406 -6.46875,6.46875v9.0625c0,3.55078 2.91406,6.46875 6.46875,6.46875h9.0625c3.55078,0 6.46875,-2.91406 6.46875,-6.46875v-9.0625c0,-3.55078 -2.91406,-6.46875 -6.46875,-6.46875zM11.46875,7h9.0625c2.47266,0 4.46875,1.99609 4.46875,4.46875v9.0625c0,2.47266 -1.99609,4.46875 -4.46875,4.46875h-9.0625c-2.47266,0 -4.46875,-1.99609 -4.46875,-4.46875v-9.0625c0,-2.47266 1.99609,-4.46875 4.46875,-4.46875zM21.90625,9.1875c-0.50391,0 -0.90625,0.40234 -0.90625,0.90625c0,0.50391 0.40234,0.90625 0.90625,0.90625c0.50391,0 0.90625,-0.40234 0.90625,-0.90625c0,-0.50391 -0.40234,-0.90625 -0.90625,-0.90625zM16,10c-3.30078,0 -6,2.69922 -6,6c0,3.30078 2.69922,6 6,6c3.30078,0 6,-2.69922 6,-6c0,-3.30078 -2.69922,-6 -6,-6zM16,12c2.22266,0 4,1.77734 4,4c0,2.22266 -1.77734,4 -4,4c-2.22266,0 -4,-1.77734 -4,-4c0,-2.22266 1.77734,-4 4,-4z" />
              </g>
            </g>
          </svg>
        </button>
        <button
          className="card2"
          onClick={() =>
            window.open("https://www.youtube.com/@PromotePDX", "_blank")
          }
        >
          <svg
            className="youtube"
            xmlns="http://www.w3.org/2000/svg"
            x="0px"
            y="0px"
            width="30px"
            height="48px"
            viewBox="0 0 48 48"
          >
            <path
              fill="#FF3D00"
              d="M43.2,33.9c-0.4,2.1-2.1,3.7-4.2,4c-3.3,0.5-8.8,1.1-15,1.1c-6.1,0-11.6-0.6-15-1.1c-2.1-0.3-3.8-1.9-4.2-4C4.4,31.6,4,28.2,4,24c0-4.2,0.4-7.6,0.8-9.9c0.4-2.1,2.1-3.7,4.2-4C12.3,9.6,17.8,9,24,9c6.2,0,11.6,0.6,15,1.1c2.1,0.3,3.8,1.9,4.2,4c0.4,2.3,0.9,5.7,0.9,9.9C44,28.2,43.6,31.6,43.2,33.9z"
            ></path>
            <path fill="#FFF" d="M20 31L20 17 32 24z"></path>
          </svg>
        </button>
      </div>
      <div className="down">
        <button
          className="card3"
          onClick={() => window.open("https://promotepdx.substack.com/", "_blank")}
        >
          <svg
            className="substack"
            xmlns="http://www.w3.org/2000/svg"
            fill="currentColor"
            viewBox="-5 0 20 20"
            height="30px"
            width="30px"
          >
            <path d="M15 3.604H1v1.891h14v-1.89ZM1 7.208V16l7-3.926L15 16V7.208zM15 0H1v1.89h14z" />
          </svg>
        </button>
        <button
          className="card4"
          onClick={() => window.open("https://discord.gg/pcMeapDkeZ", "_blank")}
        >
          <svg
            className="discord"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 48 48"
            width="30px"
            height="30px"
          >
            <path d="M40,12c0,0-4.585-3.588-10-4l-0.488,0.976C34.408,10.174,36.654,11.891,39,14c-4.045-2.065-8.039-4-15-4s-10.955,1.935-15,4c2.346-2.109,5.018-4.015,9.488-5.024L18,8c-5.681,0.537-10,4-10,4s-5.121,7.425-6,22c5.162,5.953,13,6,13,6l1.639-2.185C13.857,36.848,10.715,35.121,8,32c3.238,2.45,8.125,5,16,5s12.762-2.55,16-5c-2.715,3.121-5.857,4.848-8.639,5.815L33,40c0,0,7.838-0.047,13-6C45.121,19.425,40,12,40,12z M17.5,30c-1.933,0-3.5-1.791-3.5-4c0-2.209,1.567-4,3.5-4s3.5,1.791,3.5,4C21,28.209,19.433,30,17.5,30z M30.5,30c-1.933,0-3.5-1.791-3.5-4c0-2.209,1.567-4,3.5-4s3.5,1.791,3.5,4C34,28.209,32.433,30,30.5,30z" />
          </svg>
        </button>
      </div>
    </div>
  );
};
export default SocialsButton;
