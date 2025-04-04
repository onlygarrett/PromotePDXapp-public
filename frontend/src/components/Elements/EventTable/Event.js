import React from "react";
import SpotlightCard from "../../Cards/SpotlightCard/SpotlightCard.js";
import EventInfoButton from "../Button/EventInfoButton/EventButton.js";
import "./Event.css";

function Event({ event: { id, artist, date, venue, link, time } }) {
  const maxLength = 90;
  const fontSize = artist.length > maxLength ? "25px" : "30px";

  const isLinkEmpty = !link || link.trim() === "";

  return (
    <li key={id} className="event-card">
      <SpotlightCard className="custom-spotlight-card" spotlightColor="#cdbda6">
        <i className="fa fa-lock"></i>
        <h1 className="event-artist" style={{ fontSize }}>
          {artist}
        </h1>
        <h2 className="event-date">{date}</h2>

        <p className="event-venue">{venue}</p>
        <p className="event-time">{time}</p>

        <div className="tooltip-container">
          <EventInfoButton
            className="btn"
            link={isLinkEmpty ? undefined : link}
            disabled={isLinkEmpty}
          >
            Watch
          </EventInfoButton>
          {isLinkEmpty && (
            <span className="tooltip-text">No link available</span>
          )}
        </div>
      </SpotlightCard>
    </li>
  );
}

export default Event;
