import "./WhySection.css";
import MessageIcon from "../../assets/icons/MessageIcon";
import EuroIcon from "../../assets/icons/EuroIcon";
import BoltIcon from "../../assets/icons/BoltIcon";
import Card from "./Card";

export default function WhySection() {
  return (
    <section className="section-why">
      <div className="why-title">
        <h3 className="heading-tertiary">Miért érdemes kipróbálni?</h3>
        <h2 className="heading-secondary">
          Fedezd fel a horoszkópod rejtelmeit
        </h2>
        <p className="heading-text">
          A napi horoszkóp segít megérteni a körülötted zajló eseményeket és
          azok hatását az életedre. Fedezd fel, mit tartogat számodra a jövő!
        </p>
      </div>
      <div className="cards-container">
        <Card
          Icon={MessageIcon}
          title="Személyre szabott üzenet"
          text="Minden nap új üzenetet kapsz a csillagjegyed alapján, csak neked."
        />
        <Card
          Icon={BoltIcon}
          title="Gyors és egyszerű"
          text="Csak válaszd ki a csillagjegyed, és azonnal megkapod a napi horoszkópot."
        />
        <Card
          Icon={EuroIcon}
          title="Ingyenes használat"
          text="Az alkalmazás teljesen ingyenes, regisztráció nélkül."
        />
      </div>
    </section>
  );
}
