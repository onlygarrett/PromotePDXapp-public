import { useState, useEffect } from "react";
import axios from "axios";
import MainCard from "../../components/Cards/MainCard/MainCard.js";
import Events from "../../components/Elements/EventTable/Events.js";
import DateRangePicker from "@wojtekmaj/react-daterange-picker";
import "@wojtekmaj/react-daterange-picker/dist/DateRangePicker.css";
import "react-calendar/dist/Calendar.css";

const EventCalendar = () => {
  const [events, setEvents] = useState([]);
  const [venues, setVenues] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1); // Total number of pages
  const [searchQuery, setSearchQuery] = useState(""); // Search input state
  const [dateRange, setDateRange] = useState([null, null]); // Date range state

  const [venueQuery, setVenueQuery] = useState(""); // Venue input state
  const [debouncedQuery, setDebouncedQuery] = useState(""); // Debounced query state
  const [sortBy, setSortBy] = useState("date"); // Default sort field
  const [order, setOrder] = useState("asc"); // Default order

  useEffect(() => {
    const handler = setTimeout(() => {
      setDebouncedQuery(searchQuery); // Update debounced value after delay
    }, 300); // Delay of 300ms

    return () => {
      clearTimeout(handler); // Clear timeout if input changes quickly
    };
  }, [searchQuery]); // Runs whenever searchQuery changes

  useEffect(() => {
    fetch("https://promotepdx.com/api/venues/")
      .then((response) => response.json())
      .then((data) => setVenues(data));
  }, []);

  // Fetch events when any filter changes
  useEffect(() => {
    fetchEvents(1); // Always start at page 1 when filters change
  }, [debouncedQuery, dateRange, sortBy, order, venueQuery]); // Dependency array

  const fetchEvents = (page = 1) => {
    let query = `?page=${page}`;
    if (debouncedQuery) query += `&artist=${debouncedQuery}`;

    if (dateRange && dateRange[0])
      query += `&start_date=${dateRange[0].toISOString().split("T")[0]}`;
    if (dateRange && dateRange[1])
      query += `&end_date=${dateRange[1].toISOString().split("T")[0]}`;

    if (venueQuery) query += `&venue=${venueQuery}`;
    query += `&sort_by=${sortBy}&order=${order}`;

    axios
      .get(`https://promotepdx.com/api/events/${query}`)
      .then((res) => {
        setEvents(res.data.results);
        setTotalPages(Math.ceil(res.data.count / 32));
        setCurrentPage(page); // Update current page
      })
      .catch((err) => {
        console.log(err);
      });
  };

  const handleNextPage = () => {
    if (currentPage < totalPages) {
      fetchEvents(currentPage + 1, searchQuery); // Fetch next page
    }
  };

  const handlePrevPage = () => {
    if (currentPage > 1) {
      fetchEvents(currentPage - 1, searchQuery); // Fetch previous page
    }
  };

  // Clear all filters
  const handleClearFilters = () => {
    setSearchQuery(""); // Clear artist search
    setDateRange([null, null]); // Clear date range

    setSortBy("date"); // Reset sort
    setVenueQuery(""); // Remove venue filter
    fetchEvents(1); // Reset fetch with no filters
  };

  const handleSearch = (e) => {
    setSearchQuery(e.target.value);
    fetchEvents(1, e.target.value); // Search from page 1
  };
  const handleDateChange = (range) => {
    setDateRange(range);
    fetchEvents(1); // Fetch events with the new date range
  };

  return (
    <div className="App">
      <MainCard header={"Upcomings Events"} />
      <div className="filters">
        <input
          type="text"
          placeholder="Search by artist name..."
          value={searchQuery}
          onChange={handleSearch}
        />
        <select
          className="venue-select"
          value={venueQuery}
          onChange={(e) => setVenueQuery(e.target.value)}
        >
          <option value="">All Venues</option>
          {venues.map((venue, index) => (
            <option key={index} value={venue}>
              {venue}
            </option>
          ))}
        </select>

        <div className="date-picker-container">
          <DateRangePicker
            onChange={handleDateChange}
            value={dateRange}
            allowPartialRange={true}
          />
        </div>
        <select
          value={sortBy}
          onChange={(e) => setSortBy(e.target.value)} // Update sort field
        >
          <option value="artist">Artist</option>
          <option value="date">Date</option>
        </select>
        <button className="clear-button" onClick={handleClearFilters}>
          <span className="X"></span>
          <span className="Y"></span>
          <div className="clear-close">Close</div>
        </button>
      </div>
      <div className="App">
        <Events events={events} />
        <div className="pagination-controls">
          <button
            className="pagination-button"
            onClick={handlePrevPage}
            disabled={currentPage === 1}
          >
            Previous
          </button>
          <span className="pagination-counter">
            Page {currentPage} of {totalPages}
          </span>
          <button
            className="pagination-button"
            onClick={handleNextPage}
            disabled={currentPage === totalPages}
          >
            Next
          </button>
        </div>
      </div>
    </div>
  );
};

export default EventCalendar;
