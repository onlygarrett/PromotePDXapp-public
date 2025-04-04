import React from "react";
import "./EventButton.css";
function EventInfoButton({ link, disabled }) {
  const handleClick = () => {
    if (!disabled && link) {
      window.open(link, "_blank");
    }
  };

  return (
    <button
      className={`btn ${disabled ? "btn-disabled" : ""}`}
      onClick={handleClick}
      disabled={disabled}
    >
      <span>Event Info</span>
    </button>
  );
}
export default EventInfoButton;
