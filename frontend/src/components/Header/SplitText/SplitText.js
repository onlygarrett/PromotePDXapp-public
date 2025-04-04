import React, { useState, useEffect, useRef } from "react";
import "./SplitText.css"; // Import the CSS file

const SplitText = () => {
  const texts = [
    "",
    "Live Music",
    "Shows",
    "Local Artists",
    "Venues",
    "Portland",
    "",
  ];

  const morphTime = 1; // seconds
  const cooldownTime = 0.6; // seconds

  const [textIndex, setTextIndex] = useState(0);
  const [fraction, setFraction] = useState(1);
  const [isAnimating, setIsAnimating] = useState(true);
  const [styles, setStyles] = useState({ style1: {}, style2: {} });

  const requestRef = useRef();
  const previousTimeRef = useRef();
  const cooldownRef = useRef(0);
  const morphRef = useRef(morphTime);

  const updateStyles = (frac) => {
    // If we're at the last text, set final styles
    if (textIndex === texts.length - 1) {
      setStyles({
        style1: {
          filter: "blur(0px)",
          opacity: "100%",
        },
        style2: {
          filter: "blur(100px)",
          opacity: "0%",
        },
      });
      return;
    }

    const blur1 = Math.min(8 / (1 - frac) - 8, 100);
    const opacity1 = Math.pow(1 - frac, 0.4) * 100;

    const blur2 = Math.min(8 / frac - 8, 100);
    const opacity2 = Math.pow(frac, 0.4) * 100;

    setStyles({
      style1: {
        filter: `blur(${isNaN(blur1) ? 100 : blur1}px)`,
        opacity: `${isNaN(opacity1) ? 0 : opacity1}%`,
      },
      style2: {
        filter: `blur(${isNaN(blur2) ? 100 : blur2}px)`,
        opacity: `${isNaN(opacity2) ? 0 : opacity2}%`,
      },
    });
  };

  useEffect(() => {
    const animate = (time) => {
      if (textIndex === texts.length - 1) {
        setIsAnimating(false);
        updateStyles(1);
        return;
      }

      if (previousTimeRef.current != undefined) {
        const dt = (time - previousTimeRef.current) / 1000; // Convert to seconds

        cooldownRef.current -= dt;

        if (cooldownRef.current <= 0) {
          morphRef.current -= dt;
          let fractionValue = morphRef.current / morphTime;

          if (fractionValue <= 0) {
            fractionValue = 0;
            cooldownRef.current = cooldownTime;
            morphRef.current = morphTime;

            if (textIndex >= texts.length - 2) {
              setTextIndex(texts.length - 1);
            } else {
              setTextIndex(textIndex + 1);
            }
          }
          setFraction(fractionValue);
          updateStyles(fractionValue);
        } else {
          morphRef.current = morphTime;
          setFraction(1);
          updateStyles(1);
        }
      }
      previousTimeRef.current = time;
      if (isAnimating) {
        requestRef.current = requestAnimationFrame(animate);
      }
    };

    requestRef.current = requestAnimationFrame(animate);
    return () => cancelAnimationFrame(requestRef.current);
  }, [isAnimating, textIndex]);

  return (
    <div id="container">
      {/* <span className="text1" style={styles.style1}> */}
      {/*   {texts[textIndex]} */}
      {/* </span> */}
      {/* <span className="text2" style={styles.style2}> */}
      {/*   {texts[(textIndex + 1) % texts.length] || ""} */}
      {/* </span> */}
      {textIndex === texts.length - 1 ? (
        <img className="main-card-header-text-svg" src="/Container-Tan.svg" alt="Container Tan" />
      ) : (
        <>
          <span className="text1" style={styles.style1}>
            {texts[textIndex]}
          </span>
          <span className="text2" style={styles.style2}>
            {texts[(textIndex + 1) % texts.length] || ""}
          </span>
        </>
      )}
      <svg className="filters">
        <defs>
          <filter id="threshold">
            <feColorMatrix
              in="SourceGraphic"
              type="matrix"
              values="
              1 0 0 0 0
              0 1 0 0 0
              0 0 1 0 0
              0 0 0 255 -140"
            />
          </filter>
        </defs>
      </svg>
    </div>
  );
};

export default SplitText;
