# IMDb - Visualização e Predição

## Objetivo do Projeto

Este projeto tem como objetivo criar uma interface interativa para visualização de dados e predição de notas IMDb de filmes, utilizando técnicas de ciência de dados e aprendizado de máquina. O backend realiza o processamento e predição, enquanto o frontend permite a interação do usuário.

## Como Instalar e Rodar

1. **Clone o repositório:**
   ```bash
   git clone <url-do-repositorio>
   ```
2. **Instale as dependências do backend:**
   ```bash
   cd src
   pip install -r ../requirements.txt
   ```
3. **Instale as dependências do frontend:**
   ```bash
   cd ../frontend
   npm install
   ```
4. **Execute o backend:**
   ```bash
   cd ../src
   python app.py
   ```
5. **Execute o frontend:**
   ```bash
   cd ../frontend
   npm start
   ```

## Explicações dos Notebooks e Modelo

- **notebooks/EDA.ipynb**: Análise exploratória dos dados, visualizações e estatísticas principais.
- **notebooks/Modelagem.ipynb**: Processo de modelagem, seleção de variáveis e treinamento do modelo de regressão.
- **notebooks/Predicao_Exemplo.ipynb**: Exemplos de uso do modelo para predição de notas IMDb.
- **notebooks/Texto_Overview.ipynb**: Análise e limpeza do campo de sinopse dos filmes.

O modelo final é salvo em `models/imdb_model.pkl` e utilizado pelo backend para realizar predições a partir dos dados enviados pelo frontend.
