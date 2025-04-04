import { Link } from "react-router-dom";
import "./NavBar.css";
import { useState } from "react";



const Navbar = () => {

  const [showNav, setShowNav] = useState(false);
  const toggleNav = () => {
    setShowNav(!showNav);
  };
  return (
    <nav>
      <div className="nav-left">
        <ul>
          <li>
            <Link to="/">
              {/* <h2 className="nav-card-header">{"PromotePDX"}</h2> */}
              <img className="nav-card-header" src="/logo-circle.png" alt="logo-circle" />
            </Link>
          </li>
        </ul>
      </div>
      <div className="menu-icon" onClick={toggleNav}>
        <img className="menu-icon-svg" src="/hamburger.svg" alt="menu-icon-svg" />
      </div>
      <div className={`nav-right ${showNav && 'active'}`}>
        <ul>
          <li>
            <Link to="/" onClick={toggleNav}>Home</Link>
          </li>
          <li>
            <Link to="/about" onClick={toggleNav}>About</Link>
          </li>
          <li>
            <Link to="/events" onClick={toggleNav}>Events</Link>
          </li>
          <li>
            <Link to="/contact" onClick={toggleNav}>Contact</Link>
          </li>
        </ul>
      </div>
    </nav>
  );
};

export default Navbar;
