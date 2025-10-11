import "./Card.css";

export default function Card({ Icon, title, text }) {
  return (
    <div className="card">
      {Icon && <Icon />}
      <h4 className="card-title">{title}</h4>
      <p className="card-text">{text}</p>
    </div>
  );
}
