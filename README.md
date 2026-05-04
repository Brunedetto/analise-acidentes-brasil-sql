# analise-acidentes-brasil-sql
Análise de acidentes de trânsito no Brasil utilizando SQL e dados da PRF

# 🚧 Análise de Acidentes de Trânsito no Brasil (PRF)

Este projeto tem como objetivo explorar e analisar dados de acidentes de trânsito no Brasil utilizando SQL.

A base utilizada é pública, disponibilizada pela Polícia Rodoviária Federal (PRF).

---

## 📊 Objetivo

Responder perguntas importantes como:

- Qual o total de acidentes ao longo dos anos?
- Qual o número de mortos e feridos?
- Qual o percentual de gravidade dos acidentes?
- Quais estados possuem mais ocorrências?
- Onde os acidentes são mais graves?
- Quais tipos de acidentes são mais frequentes?

---

## 🗂️ Fonte dos dados

Dados públicos da PRF (Polícia Rodoviária Federal)

---

## 🛠️ Tecnologias utilizadas

- Python
- DuckDB
- SQL
- Pandas

---

## 🔍 Etapas da análise

### 1. Tratamento inicial dos dados

- Leitura do arquivo `.parquet`
- Conversão para `.csv`
- Conexão com DuckDB

---

### 2. Identificação de inconsistências

Durante a análise, foi identificado um problema:

👉 O total de acidentes em 2024 estava acima de 600 mil, um valor incoerente.

---

### ⚠️ Problema encontrado

A base de dados não possui uma linha por acidente, mas sim:

👉 **uma linha por vítima envolvida**

Isso gera duplicidade na contagem de acidentes.

---

### ✅ Solução aplicada

Para corrigir isso, foi utilizada a seguinte abordagem:

```sql
COUNT(DISTINCT id)

Assim, cada acidente passou a ser contado apenas uma vez.

📈 Principais análises

📅 Série histórica
Análise da evolução dos acidentes ao longo dos anos

👉 Resultado:
2011 foi o ano com maior número de acidentes (192.322)

📍 Análise por estado (UF)
Estados com mais acidentes
Estados com mais vítimas

👉 Destaque:
Minas Gerais lidera em volume total de acidentes e vítimas

⚠️ Gravidade dos acidentes
Cálculo de vítimas por acidente

👉 Insight importante:
Estados com menor número de acidentes podem ter maior gravidade

Exemplo:

Amazonas apresentou maior média de vítimas por acidente
🚗 Tipos de acidentes
Identificação dos mais frequentes

👉 Resultado:
Colisão traseira é o tipo mais comum

📊 Principais métricas
Total de acidentes
Total de vítimas
Quantidade de mortos
Quantidade de feridos
Percentual de mortos
Percentual de feridos
Média de vítimas por acidente
🚀 Próximos passos
Construção de dashboard no Power BI
Visualização interativa dos dados
Criação de storytelling com insights
📌 Autor

Bruno Luiz

📎 Observação

Este projeto faz parte do meu desenvolvimento na área de análise de dados.
