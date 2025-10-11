import { Link } from "react-router-dom";
import "./Navbar.css";
import logo from "../../assets/horoscope.png";

export default function Navbar() {
  return (
    <nav className="navbar">
      <div className="logo">
        <img src={logo} alt="Napi horoszkóp logo" className="logo-img" />
        Napi Horoszkóp
      </div>
      <ul className="nav-links">
        <li>
          <Link to="/">Főoldal</Link>
        </li>
      </ul>
      <Link className="nav-button" to="/app">
        Alkalmazás
      </Link>
    </nav>
  );
}
