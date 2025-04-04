import React, { Suspense } from "react";
import CarouselCard from "../../Elements/Carousel/Carousel.js";
import "./HomeBody.css";
function Loading() {
  return <h2>Loading...</h2>;
}
const HomeBody = () => {
  return (
    <Suspense fallback={<Loading />}>
      <div id="pdx-home-body" className="pdx-home-body">
        <CarouselCard />
      </div>
    </Suspense>
  );
};

export default HomeBody;
