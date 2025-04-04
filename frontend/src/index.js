import "bootstrap/dist/css/bootstrap.min.css";
import React from "react";
import ReactDOM from "react-dom/client";
import { RouterProvider, createBrowserRouter } from "react-router-dom";
import "semantic-ui-css/semantic.min.css";
import App from "./App.js";
import "./index.css";
import reportWebVitals from "./reportWebVitals.js";
import AboutPage from "./views/AboutPage/AboutPage.js";
import Contact from "./views/ContactPage/Contact.js";
import EventCalendar from "./views/EventCalendar/EventCalendar.js";
import HomePage from "./views/HomePage/Homepage.js";

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    children: [
      {
        path: "/",
        element: <HomePage />,
      },
      {
        path: "/about",
        element: <AboutPage />,
      },
      {
        path: "/events",
        element: <EventCalendar />,
      },
      {
        path: "/contact",
        element: <Contact />,
      },
    ],
  },
]);
ReactDOM.createRoot(document.getElementById("root")).render(
  <RouterProvider router={router}>
    <App />
  </RouterProvider>
);

reportWebVitals();
