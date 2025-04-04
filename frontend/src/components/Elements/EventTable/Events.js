import React from "react";
import "./Event.css";
import Event from "./Event.js";

function Events({ events }) {
  return (
    <div className="events-list-container">
      <ul className="events-list">
        {events.map((event) => (
          <Event key={event.id} event={event} />
        ))}
      </ul>
    </div>
  );
}

export default Events;
