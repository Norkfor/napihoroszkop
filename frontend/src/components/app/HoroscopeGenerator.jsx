import { useState } from "react";
import "./HoroscopeGenerator.css";
import EmailForm from "./EmailForm";

const HoroscopeGenerator = () => {
  const [name, setName] = useState("");
  const [month, setMonth] = useState("");
  const [day, setDay] = useState("");
  const [errors, setErrors] = useState({});
  const [quote, setQuote] = useState("");
  const [showQuote, setShowQuote] = useState(false);
  const [loading, setLoading] = useState(false);
  const [showEmail, setShowEmail] = useState(false);

  const validate = () => {
    const newErrors = {};
    if (!name.trim()) newErrors.name = "Adj meg egy nevet!";
    if (!month) newErrors.month = "Add meg a hónapot!";
    else if (month < 1 || month > 12)
      newErrors.month = "A hónap 1 és 12 között lehet.";
    if (!day) newErrors.day = "Add meg a napot!";
    else if (day < 1 || day > 31) newErrors.day = "A nap 1 és 31 között lehet.";

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleGenerate = async () => {
    if (!validate()) {
      setShowQuote(false);
      setQuote("");
      return;
    }

    setLoading(true);
    setQuote("");
    setShowQuote(false);

    try {
      const res = await fetch("http://localhost:6100/api/send-horoscope", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          name,
          email: "teszt@email.com", // ide az email inputból jöhet
          birth_month: parseInt(month),
          birth_day: parseInt(day),
        }),
      });

      const data = await res.json();

      if (res.ok) {
        // API sikeres válasz
        setQuote(data.message || "Horoszkópod itt jelenik meg!");
        setShowQuote(true);
      } else {
        // API hibás válasz
        setQuote(data.detail || "Hiba történt az API híváskor.");
        setShowQuote(true);
      }
    } catch (err) {
      console.error(err);
      setQuote("Hálózati hiba, próbáld újra.");
      setShowQuote(true);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <section className="section-horoscope">
        <h1 className="horoscope-title">Mire Készít Fel Ma a Kozmosz?</h1>
        <h3 className="horoscope-subtitle">
          A kozmosz csak akkor suttog a füledbe, ha tudja, mikor születtél. Add
          meg a születési dátumod, és fedezd fel a Rád szabott Napi Kozmikus
          Üzenetet!
        </h3>

        <div className="horoscope-form">
          <label className="input-label">Név</label>
          <div className="input-wrapper">
            {errors.name && <p className="error-text">{errors.name}</p>}
            <input
              type="text"
              placeholder="Név"
              value={name}
              onChange={(e) => setName(e.target.value)}
              className={errors.name ? "input-error" : ""}
            />
          </div>

          <label className="input-label">Születési dátum</label>
          <div className="input-group">
            <div className="input-wrapper">
              {errors.month && <p className="error-text">{errors.month}</p>}
              <input
                type="number"
                min="1"
                max="12"
                value={month}
                onChange={(e) => setMonth(e.target.value)}
                className={`horoscope-input ${
                  errors.month ? "input-error" : ""
                }`}
                placeholder="HH"
              />
            </div>
            <span className="date-separator">/</span>
            <div className="input-wrapper">
              {errors.day && <p className="error-text">{errors.day}</p>}
              <input
                type="number"
                min="1"
                max="31"
                value={day}
                onChange={(e) => setDay(e.target.value)}
                className={`horoscope-input ${errors.day ? "input-error" : ""}`}
                placeholder="NN"
              />
            </div>
          </div>
        </div>

        <button
          className="horoscope-button"
          onClick={() => {
            setShowEmail(true);
            handleGenerate();
          }}
          disabled={loading}
        >
          {loading ? "Betöltés..." : "Mutasd a horoszkópom ✨"}
        </button>

        {showQuote && (
          <div className="horoscope-quote">
            <span>{quote}</span>
          </div>
        )}
      </section>

      {showEmail && (
        <section className="section-email">
          <h2 className="email-title">
            Fedezd fel minden nap a horoszkópod üzenetét!
          </h2>
          <p className="email-subtitle">
            Iratkozz fel hírlevelünkre, és minden reggel egy személyre szabott,
            inspiráló horoszkóp üzenet vár rád.
          </p>
          <EmailForm name={name} month={month} day={day} />
        </section>
      )}
    </div>
  );
};

export default HoroscopeGenerator;
