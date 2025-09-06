import React, { useState } from 'react';
import './FormularioFilme.css';

const FormularioFilme = () => {
  const [dados, setDados] = useState({
    Released_Year: '',
    Runtime: '',
    Meta_score: '',
    Gross: '',
    No_of_Votes: '',
    Certificate: '',
    Genre: '',
    Overview_clean: ''
  });

  const [nota, setNota] = useState<number | null>(null);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    setDados({ ...dados, [e.target.name]: e.target.value });
  };

  const handleSubmit = async () => {
    const response = await fetch('http://localhost:5000/model/predict', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(dados)
    });
    const result = await response.json();
    setNota(result.predicted_rating);
  };

  return (
  <div className="form-container">
    <h2>Previsão de Nota IMDB</h2>
    <input name="Released_Year" placeholder="Ano de lançamento" onChange={handleChange} />
    <input name="Runtime" placeholder="Duração (min)" onChange={handleChange} />
    <input name="Meta_score" placeholder="Meta Score" onChange={handleChange} />
    <input name="Gross" placeholder="Faturamento" onChange={handleChange} />
    <input name="No_of_Votes" placeholder="Nº de votos" onChange={handleChange} />
    <input name="Certificate" placeholder="Classificação" onChange={handleChange} />
    <input name="Genre" placeholder="Gênero" onChange={handleChange} />
    <textarea name="Overview_clean" placeholder="Sinopse limpa" onChange={handleChange} />
    <button onClick={handleSubmit}>Prever Nota</button>
    {nota !== null && <p className="result">Nota prevista: {nota}</p>}
  </div>
  );
};

export default FormularioFilme;
