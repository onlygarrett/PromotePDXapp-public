import React, { useEffect, useState } from "react";
import { Carousel } from "react-bootstrap";
import fetchPostsData from "./carousel-config.js";
import "./carousel.css";
import CarouselItem from "./CarouselItem.js";
const CarouselCard = () => {
  const [postsData, setPostsData] = useState([]);
  const [loading, setLoading] = useState(false);

  const generateImageElements = async () => {
    setLoading(true); // Set loading to true before fetching
    const data = await fetchPostsData(); // Fetch the data
    const elements = data.map((post) => (
      <CarouselItem
        key={post.id}
        postLink={post.permalink}
        imgUrl={post.media_url}
        imgTitle={post.index}
      />
    ));
    setPostsData(elements); // Store the list of <img> elements
    setLoading(false); // Set loading to false after processing
  };

  useEffect(() => {
    generateImageElements(); // Generate the image elements on mount
  }, []);

  return (
    <>
      <Carousel indicators={false} fade={true} interval={1000 * 6}>
        {postsData.map((post, index) => (
          <Carousel.Item key={`carousel__item_${index}`}>{post}</Carousel.Item>
        ))}
      </Carousel>
    </>
  );
};
export default CarouselCard;
