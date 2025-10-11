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
          <a href="#home">Főoldal</a>
        </li>
      </ul>
      <a className="nav-button" href="#">
        Próbáld ki az alkalmazást
      </a>
    </nav>
  );
}
