import { useState } from "react";
import "./EmailForm.css";

const EmailForm = () => {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [errors, setErrors] = useState({});

  const validateEmail = (email) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);

  const handleSubmit = () => {
    const newErrors = {};

    if (!name.trim()) newErrors.name = "Adj meg egy nevet!";
    else if (name.trim().length < 2) newErrors.name = "A név túl rövid!";

    if (!email.trim()) newErrors.email = "Adj meg egy e-mail címet!";
    else if (!validateEmail(email))
      newErrors.email = "Érvényes e-mailt adj meg!";

    setErrors(newErrors);

    if (Object.keys(newErrors).length === 0) {
      console.log({ name, email });
    }
  };

  return (
    <div className="form-inner">
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
      <button className="email-button" onClick={handleSubmit}>
        Feliratkozom
      </button>
    </div>
  );
};

export default EmailForm;
