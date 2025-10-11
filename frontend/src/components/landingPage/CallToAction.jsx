import "./CallToAction.css";

export default function CallToAction() {
  return (
    <section className="section-cta">
      <div className="cta-title">
        <h3 className="heading-tertiary">próbáld ki</h3>
        <h2 className="heading-secondary">
          Kezdd el a napi horoszkópod felfedezését még ma!
        </h2>
        <p className="heading-text">
          Csatlakozz a több ezer elégedett felhasználóhoz, és tudd meg, mit
          tartogat számodra a jövő!
        </p>
      </div>
      <a className="cta-button" href="#app">
        Indítsd el az alkalmazást &#8594;
      </a>
    </section>
  );
}
