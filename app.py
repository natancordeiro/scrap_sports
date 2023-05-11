from engine.pro_direect import ProDirect
import schedule
import time

def main():        
    p = ProDirect()

    libra = p.cotacao_libra()
    print(f"Cotação atual da libra: R${str(libra).replace('.', ',')}")

    try:
        p.scraping_chuteiras(1, 29)
    except KeyboardInterrupt:
        print("saindo..")
        p.close()
    except Exception as e:
        print("Ocorreu um erro inesperado: ", e)

main()

# # agendar a execução da função todos os dias às 9 da manhã
# schedule.every().day.at("04:00").do(main())

# # loop para executar a verificação da agenda
# while True:
#     schedule.run_pending()
#     time.sleep(1)
