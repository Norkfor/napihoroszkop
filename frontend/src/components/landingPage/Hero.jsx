import "./Hero.css";
import heroImg from "../../assets/hero-img.jpg";

export default function Hero() {
  return (
    <section className="hero">
      <div className="hero-left">
        <h1 className="hero-title">Fedezd fel a napi horoszkópod!</h1>
        <p className="hero-subtitle">
          Fedezd fel a világegyetem bölcsességét személyre szabott, naponta
          kézbesített horoszkóp-idézetekkel. Szerezz bepillantást a napodba, a
          kapcsolataidba és a személyes fejlődésedbe
        </p>
        <a className="hero-button" href="app">
          Próbáld ki most
        </a>
      </div>
      <div className="hero-right">
        <img
          src={heroImg}
          alt="Horoszkóp illusztráció"
          className="hero-image"
        />
      </div>
    </section>
  );
}
