from engine.pro_direect import ProDirect
import schedule
import time

"""Extrai os dados de todas as chuteiras do site prodirectsports."""
def main():        
    p = ProDirect()

    libra = p.cotacao_libra()
    print(f"Cotação atual da libra: R${str(libra).replace('.', ',')}")

    try:
        p.scraping_chuteiras(1, 29)
    except Exception as e:
        print(e)
    finally:
        p.close()

if __name__ == '__main__':

    # agendar a execução da função todos os dias às 9 da manhã
    # schedule.every().day.at("04:00").do(main())

    # # loop para executar a verificação da agenda
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)

    main()
    