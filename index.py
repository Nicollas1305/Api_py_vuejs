import pandas as pd
from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Api no AR'

class Consulta:
    def encontrar_arquivo(caminho, dado):
        linha_completa = ''

        if caminho[-4:] == '.csv':
            caminho = f'{caminho}'
        else:
            caminho = f'{caminho}.csv'
            
        with open(caminho, 'r') as arquivo:
            for linha in arquivo:
                linha = linha.strip('\n')
                if linha_completa == '':
                    if dado in linha.split():
                        linha_completa = linha
                    else:
                        registro_list = linha_completa.split()
                        registro_dict = {
                            'RegistroANS': registro_list[1],
                            'CNPJ': registro_list[2],
                            'Razão Social': registro_list[3],
                            'Nome Fantasia': registro_list[3],
                            'Modalidade': registro_list[4],
                            'Logradouro': registro_list[5],
                            'Número': registro_list[6],
                            'Complemento': registro_list[7],
                            'Bairro': registro_list[8],
                            'Cidade': registro_list[9],
                            'UF': registro_list[10],
                            'CEP': registro_list[11],
                            'DDD': registro_list[12],
                            'Telefone': registro_list[13],
                            'FAX': registro_list[14],
                            'Endereço eletrônico': registro_list[15],
                            'Representante': registro_list[16],
                            'Cargo Representante': registro_list[17],
                            'Data Refistro ANS': registro_list[18],
                        }
        #return registro_dict
        Consulta.imprimir_arquivo(registro_dict)

    def imprimir_arquivo(registro):
        for key, value in registro.items():
            print(f'{key}>>> {value: <12}')

caminho = str(input('Nome do arquivo: ')).lower().strip()
dado = str(input('CNPJ: ')).title().strip()
Consulta.encontrar_arquivo(caminho, dado)

table = pd.read_csv('Relatorio_cadop.csv', sep='|', encoding='latin-1')

print(table)


app.run()