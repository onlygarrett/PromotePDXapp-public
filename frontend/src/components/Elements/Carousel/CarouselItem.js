import React from "react";
import { Image } from "react-bootstrap";
import "./carousel.css";
function CarouselItem({ imgUrl, imgTitle, postLink }) {
  const handleClick = () => {
    window.open(postLink, "_blank");
  };
  return (
    <Image
      src={imgUrl}
      style={{ cursor: "pointer" }}
      alt={imgTitle}
      onClick={handleClick}
      rounded
      fluid
      width={450}
      height={450}
    />
  );
}

export default CarouselItem;
