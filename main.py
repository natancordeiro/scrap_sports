from engine.pro_direect import ProDirect
import pandas as pd
import schedule
import time

"""Extrai os dados de todas as chuteiras do site prodirectsports."""
def main():        
    p = ProDirect()

    libra = p.cotacao_libra()
    print(f"Cotação atual da libra: R${str(libra).replace('.', ',')}")

    try:
        dados = p.scraping_chuteiras(1, 1)
        printar_dados(dados)

    except Exception as e:
        print(e)
    finally:
        p.close()

def printar_dados(dados):
    df = pd.DataFrame(dados)
    df.columns = ['Titulo', 'Marca', 'Preço', 'Tamanhos', 'Cor', 'Descrição']
    styled_table = df.style.set_table_styles([{'selector': 'th', 'props': [('background-color', 'gray'), ('color', 'white')]}])
    print(styled_table)

if __name__ == '__main__':
    # agendar a execução da função todos os dias às 9 da manhã
    schedule.every().day.at("04:00").do(main())

    # loop para executar a verificação da agenda
    while True:
        schedule.run_pending()
        time.sleep(1)
