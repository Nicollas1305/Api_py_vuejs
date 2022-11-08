import pandas as pd


data = pd.read_csv("Relatorio_cadop.csv", parse_dates=True, sep=';', encoding='latin-1')
data.columns = data.columns.str.strip()

#print(data["CNPJ"])
search = data[data["Nome Fantasia"]=="BRASIL ODONTO PLANO DE SAUDE"]
print(search)
