import pandas as pd

df = pd.read_parquet("C:/Users/Bruno Luiz/Documents/analise.py/data/datatran.parquet")
df.to_csv("C:/Users/Bruno Luiz/Documents/analise.py/data/datatran.csv", index=False)

import duckdb
con = duckdb.connect("acidentes.db")
result = con.execute("""
                     SELECT *
                     FROM 'C:/Users/Bruno Luiz/Documents/analise.py/data/datatran.parquet'
                     LIMIT 10
                     """).df()

#print(result)

con.execute("""
            CREATE TABLE IF NOT EXISTS accidents AS
            SELECT * FROM 'C:/Users/Bruno Luiz/Documents/analise.py/data/datatran.parquet'
            """)

result = con.execute("""
                     SELECT COUNT(*)
                     FROM accidents
                     """).df()

#print(result)

result = con.execute("""
            SELECT DISTINCT estado_fisico FROM accidents;
         """).df()

#print(result)

result = con.execute("""
                     SELECT COUNT(*)
                     FROM accidents
                     WHERE estado_fisico = '�bito'
                     """).df()

#print(result)

result = con.execute("""
                     SELECT COUNT(*)
                     FROM accidents
                     WHERE estado_fisico IN ('Les�es Leves', 'Les�es Graves')
                     """).df()

#print(result)

result = con.execute("""
                     SELECT
                     CAST(SUM(CASE WHEN estado_fisico = '�bito' THEN 1 ELSE 0 END) AS INTEGER) AS mortos ,
                     CAST(SUM(CASE WHEN estado_fisico IN ('Les�es Leves', 'Les�es Graves') THEN 1 ELSE 0 END) AS INTEGER) AS feridos 
                     FROM accidents
                     """).df()
#print(result)

#total e porcentagem de mortos e feridos
result = con.execute("""
                     SELECT

                     CAST(SUM(CASE WHEN estado_fisico = '�bito' THEN 1 ELSE 0 END) AS INTEGER) AS mortos,
                     CAST(SUM(CASE WHEN estado_fisico IN ('Les�es Leves', 'Les�es Graves') THEN 1 ELSE 0 END) AS INTEGER) AS feridos,

                     COUNT(*) AS total,
                     
                     ROUND(
                     CAST(SUM(CASE WHEN estado_fisico = '�bito' THEN 1 ELSE 0 END) AS INTEGER) * 1.0 / COUNT (*) * 100, 2) AS pct_mortos,
                     ROUND(
                     CAST(SUM(CASE WHEN estado_fisico IN ('Les�es Leves', 'Les�es Graves') THEN 1 ELSE 0 END) AS INTEGER) * 1.0 / COUNT (*) * 100, 2) AS pct_feridos,
      
                     FROM accidents
                     """).df()
#print(result) 


result = con.execute("""
                     SELECT
                     EXTRACT(YEAR FROM data) AS ano,
                     COUNT(*) AS total_acidentes
                     FROM accidents
                     GROUP BY EXTRACT(YEAR FROM data)
                     ORDER BY total_acidentes DESC
                     LIMIT 1
                     """).df()
#print(result)

#ano com a maior qnt de acidentes
result = con.execute("""
                     SELECT
                     EXTRACT(YEAR FROM data) AS ano,
                     COUNT(DISTINCT id) AS total_acidentes
                     FROM accidents
                     GROUP BY EXTRACT(YEAR FROM data)
                     ORDER BY total_acidentes DESC
                     """).df()
print(result)

#descobrindo granulidade com o dataset
result = con.execute("""
                     SELECT
                     EXTRACT(YEAR FROM data) AS ano,
                     COUNT(*) AS linha,
                     COUNT(DISTINCT id) AS acidentes_unicos
                     FROM accidents
                     GROUP BY EXTRACT(YEAR FROM data)
                     ORDER BY ano
                     """).df()
#print(result)

#estados com o maior caso de acidentes
result = con.execute("""
                     SELECT
                     UF, 
                     COUNT(DISTINCT id) AS total_acidentes
                     FROM accidents
                     WHERE UF IS NOT NULL
                     GROUP BY UF 
                     ORDER BY total_acidentes DESC
                     LIMIT 10
                     """).df()
#print(result)

#estado que gera mais vitimas(incidencia, foco no volume)
result = con.execute("""
                     SELECT
                     UF,
                     COUNT(DISTINCT id) AS total_acidentes,
                     COUNT(*) AS vitimas
                      FROM accidents
                      WHERE UF IS NOT NULL
                      GROUP BY UF
                      ORDER BY total_acidentes DESC
                      LIMIT 10
                      """).df()
#print(result)

#maior média de gravidade(foco na severidade dos acidentes)
result = con.execute("""
                     SELECT
                     UF,
                     COUNT(DISTINCT id) AS total_acidentes,
                     COUNT(*) * 1.0 / COUNT(DISTINCT id) AS vitimas_por_acidente
                     FROM accidents
                     WHERE UF IS NOT NULL
                     GROUP BY UF
                     ORDER BY vitimas_por_acidente DESC
                     LIMIT 10
                     """).df()
#print(result)

result = con.execute("""
                     SELECT
                     tipo_acidente,
                     dia_semana,
                     EXTRACT(HOUR FROM horario) AS hora,
                     COUNT(DISTINCT id) AS total_acidente
                     FROM accidents
                     GROUP BY tipo_acidente, dia_semana, hora
                     ORDER BY total_acidente DESC
                     LIMIT 10
                     """).df()

#print(result)