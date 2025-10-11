import "./Footer.css";

export default function Footer() {
  return (
    <footer className="footer">
      <p>
        Made with ❤️ by{" "}
        <a
          href="https://github.com/kilozdazolik"
          target="_blank"
          rel="noopener noreferrer"
        >
          kilozdazolik
        </a>{" "}
        &{" "}
        <a
          href="https://github.com/Norkfor"
          target="_blank"
          rel="noopener noreferrer"
        >
          Norkfor
        </a>
      </p>
      <p>2025 - Napi Horoszkóp</p>
      <div className="footer-links">
        <a href="#why">Impresszum</a>
        <a href="#app">Adatkezelés</a>
      </div>
    </footer>
  );
}
