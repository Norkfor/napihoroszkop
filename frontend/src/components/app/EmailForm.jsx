import { useState } from "react";
import "./EmailForm.css";

const EmailForm = ({ name = "", month = "", day = "" }) => {
  const [email, setEmail] = useState("");
  const [errors, setErrors] = useState({});
  const [loading, setLoading] = useState(false);
  const [success, setSuccess] = useState("");

  const validateEmail = (email) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);

  const handleSubmit = async () => {
    const newErrors = {};

    if (!name.trim()) newErrors.name = "Adj meg egy nevet!";
    if (!month) newErrors.month = "Add meg a hónapot!";
    if (!day) newErrors.day = "Add meg a napot!";

    if (!email.trim()) newErrors.email = "Adj meg egy e-mail címet!";
    else if (!validateEmail(email))
      newErrors.email = "Érvényes e-mailt adj meg!";

    setErrors(newErrors);
    setSuccess("");

    if (Object.keys(newErrors).length > 0) return;

    setLoading(true);
    try {
      const res = await fetch("http://localhost:6100/api/send-horoscope", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          name,
          email,
          birth_month: parseInt(month),
          birth_day: parseInt(day),
        }),
      });

      const data = await res.json();

      if (res.ok) {
        setSuccess(data.message || "Sikeres feliratkozás!");
        setEmail("");
      } else {
        setErrors({ submit: data.detail || "Hiba történt a feliratkozáskor." });
      }
    } catch {
      setErrors({ submit: "Hálózati hiba, próbáld újra." });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="form-inner">
      <div className="input-wrapper">
        {errors.email && <p className="error-text">{errors.email}</p>}
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          className={errors.email ? "input-error" : ""}
        />
      </div>
      {errors.submit && <p className="error-text">{errors.submit}</p>}
      {success && <p className="success-text">{success}</p>}
      <button
        className="email-button"
        onClick={handleSubmit}
        disabled={loading}
      >
        {loading ? "Küldés..." : "Feliratkozom"}
      </button>
    </div>
  );
};

export default EmailForm;
