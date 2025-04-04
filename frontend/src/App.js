import { Outlet } from "react-router-dom";
import "./App.css";
import Footer from "./components/Footer/Footer.js";
import Navbar from "./components/Nav/NavBar.js";

function App() {
  return (
    <div className="app-container">
      <>
        <Navbar />
        <Outlet />
        <Footer />
      </>
    </div>
  );
}

export default App;
