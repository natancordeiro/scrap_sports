from engine.browser import *

from googletrans import Translator
from bs4 import BeautifulSoup
from functools import partial
from time import sleep
import requests
import os

class ProDirect(Browser):
    def __init__(self, socks5=None, terminal=False, chromedriver=None, remote=None, path_directory_browser=None, inconginto=False):
        super().__init__(socks5, terminal, chromedriver, remote, path_directory_browser, inconginto)
        self.base_url = 'https://www.prodirectsport.com/soccer/l/adults/departments-boots/activity-football/brand-adidas_asics_diadora_mizuno_new-balance_nike_puma_umbro/?s=10_10point5_7point5_8_8point5_9_9point5&st=latest'
        
    def esperar_elemento(self, by, element, webdriver):
        return super().esperar_elemento(by, element, webdriver)
    
    def download_image(self, src, filename):
        name = filename.replace('/', '_')
        response = requests.get(src)
        with open(f"{self.dir_tmp}/{name}", "wb") as file:
            file.write(response.content)

    def tradutor(self, texto_em_ingles):
        tradutor = Translator()
        texto = texto_em_ingles
        traducao = tradutor.translate(texto, dest='pt')

        return traducao.text

    def uk_to_br_shoe_sizes(self, marca=str, uk_sizes=list):
        if marca == "Nike":
            uk_to_br_sizes = {
                "4": "35.5",
                "4.5": "36",
                "5": "36.5",
                "5.5": "37",
                "6": "38",
                "6.5": "39",
                "7": "39.5",
                "7.5": "40",
                "8": "40.5",
                "8.5": "41",
                "9": "42",
                "9.5": "42.5",
                "10": "43",
                "10.5": "43.5",
                "11": "44",
                "11.5": "45",
                "12": "46",
                "12.5": "46.5",
                "13": "47",
                "13.5": "47.5",
                "14": "48",
            }

        elif marca == "Adidas":
            uk_to_br_sizes = {
                "4": "35.5",
                "4.5": "36",
                "5": "36.5",
                "5.5": "36.5",
                "6": "37",
                "6.5": "38",
                "7": "39",
                "7.5": "39.5",
                "8": "40",
                "8.5": "40.5",
                "9": "41",
                "9.5": "42",
                "10": "42.5",
                "10.5": "43",
                "11": "44",
                "11.5": "44.5",
                "12": "45",
                "12.5": "46",
                "13": "46.5",
                "13.5": "47",
                "14": "48",
            }

        elif marca == "Puma":
            uuk_to_br_sizes = {
                "4": "35.5",
                "4.5": "36",
                "5": "36.5",
                "5.5": "36.5",
                "6": "37",
                "6.5": "38",
                "7": "38.5",
                "7.5": "39.5",
                "8": "40",
                "8.5": "40.5",
                "9": "41",
                "9.5": "42",
                "10": "42.5",
                "10.5": "43",
                "11": "44",
                "11.5": "44.5",
                "12": "45",
                "12.5": "46",
                "13": "46.5",
                "13.5": "47",
                "14": "48",
            }

        elif marca == "Mizuno":
            uk_to_br_sizes = {
                "4": "35.5",
                "4.5": "36",
                "5": "36.5",
                "5.5": "37",
                "6": "38",
                "6.5": "39",
                "7": "39.5",
                "7.5": "40",
                "8": "40.5",
                "8.5": "41",
                "9": "42",
                "9.5": "42.5",
                "10": "43",
                "10.5": "43.5",
                "11": "44",
                "11.5": "45",
                "12": "46",
                "12.5": "46.5",
                "13": "47",
                "13.5": "47.5",
                "14": "48",
            }
        elif marca == "Diadora":
            uk_to_br_sizes = {
                "4": "35.5",
                "4.5": "36",
                "5": "36.5",
                "5.5": "36.5",
                "6": "37",
                "6.5": "38",
                "7": "39",
                "7.5": "39.5",
                "8": "40",
                "8.5": "40.5",
                "9": "41",
                "9.5": "42",
                "10": "42.5",
                "10.5": "43",
                "11": "44",
                "11.5": "44.5",
                "12": "45",
                "12.5": "46",
                "13": "46.5",
                "13.5": "47",
                "14": "48",
            }
        elif marca == "Lotto":
            uk_to_br_sizes = {
                "4": "35.5",
                "4.5": "36",
                "5": "36.5",
                "5.5": "36.5",
                "6": "37",
                "6.5": "38",
                "7": "39",
                "7.5": "39.5",
                "8": "40",
                "8.5": "40.5",
                "9": "41",
                "9.5": "42",
                "10": "42.5",
                "10.5": "43",
                "11": "44",
                "11.5": "44.5",
                "12": "45",
                "12.5": "46",
                "13": "46.5",
                "13.5": "47",
                "14": "48",
            }
        else:
            uk_to_br_sizes = {
                "4": "35.5",
                "4.5": "36",
                "5": "36.5",
                "5.5": "37",
                "6": "38",
                "6.5": "39",
                "7": "39.5",
                "7.5": "40",
                "8": "40.5",
                "8.5": "41",
                "9": "42",
                "9.5": "42.5",
                "10": "43",
                "10.5": "43.5",
                "11": "44",
                "11.5": "45",
                "12": "46",
                "12.5": "46.5",
                "13": "47",
                "13.5": "47.5",
                "14": "48",
            }

        br_sizes = []
        for size in uk_sizes:
            br_sizes.append(size)
        return br_sizes

    def scrap_images(self):
        imagens = []
        self.wdw.until(partial(self.esperar_elemento, By.CSS_SELECTOR, 'div[class="ml-thumbnails__wrapper"]'))
        index = 1

        # Carrocel de imagens
        div_imgs = self.driver.find_element(By.CSS_SELECTOR, 'div[class="ml-thumbnails__wrapper"]')
        images = div_imgs.find_elements(By.CSS_SELECTOR, 'img')

        for n, img in enumerate(images):
            src = img.get_attribute("src")
            imagens.append(src)
            index += 1
        return imagens

    def cotacao_libra(self):
        url_cotacao = 'https://hgbrasil.com/status/finance'
        response = requests.get(url_cotacao)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            cotacoes = soup.find_all("h3", class_="font-weight-normal text-white mb-2")
            libra = cotacoes[2].text.split()[1]
            
            libra = libra.replace(",", ".")
            return float(libra)
        else:
            print("Não foi possível ler o HTML da página.")

    def convert_price(self, preco_em_libras=float, cotacao_atual=True):

        if cotacao_atual:
            # Pegando cotação atual da Libra 
            _cotacao_libra = self.cotacao_libra()
        else:
            print("Usando a cotação referência: R$6,42")
            _cotacao_libra = 6.42

        #  ---- Formulas ----
        # De £1 a £45
        if preco_em_libras <= 45:
            preco_convertido = (preco_em_libras * (1 - 0.17) + 14 + 10) * (1 + 0.052) * _cotacao_libra
        
        # De £46 a £60
        if preco_em_libras >= 46 and preco_em_libras <= 60:
            preco_convertido = (preco_em_libras * (1 - 0.10) + 17 + 15) * (1 + 0.052) * _cotacao_libra
        
        # De £61 a £80
        if preco_em_libras >= 61 and preco_em_libras <= 80:
            preco_convertido = (preco_em_libras * (1 - 0.10) + 17 + 20) * (1 + 0.052) * _cotacao_libra

        # De £81 a £100
        if preco_em_libras >= 81 and preco_em_libras <= 100:
            preco_convertido = (preco_em_libras * (1 - 0.10) + 17 + 25) * (1 + 0.052) * _cotacao_libra
        
        # De £101 a £130
        if preco_em_libras >= 101 and preco_em_libras <= 130:
            preco_convertido = (preco_em_libras * (1 - 0.10) + 22 + 28) * (1 + 0.052) * _cotacao_libra

        # De £131 a £160
        if preco_em_libras >= 131 and preco_em_libras <= 160:
            preco_convertido = (preco_em_libras * (1 - 0.10) + 22 + 32) * (1 + 0.052) * _cotacao_libra
        
        # De £161 a £200
        if preco_em_libras >= 161 and preco_em_libras <= 200:
            preco_convertido = (preco_em_libras * (1 - 0.10) + 22 + 35) * (1 + 0.052) * _cotacao_libra
        
        # De £201 a £350
        if preco_em_libras >= 201 and preco_em_libras <= 350:
            preco_convertido = (preco_em_libras * (1 - 0.10) + 22 + 43) * (1 + 0.052) * _cotacao_libra
     
        num_formatado = "R$%.2f" %preco_convertido
        return num_formatado

    def extrair_marca(self, nome_produto=str):
        if "adidas" in nome_produto.lower():
            marca = "Adidas"
        elif "asics" in nome_produto.lower():
            marca = "Asics"
        elif "nike" in nome_produto.lower():
            marca = "Nike"
        elif "mizuno" in nome_produto.lower():
            marca = "Mizuno"
        elif "new balance" in nome_produto.lower():
            marca = "New Balance"
        elif "puma" in nome_produto.lower():
            marca = "Puma"
        elif "umbro" in nome_produto.lower():
            marca = "Umbro"
        elif "diadora" in nome_produto.lower():
            marca = "Diadora"
        elif "lotto" in nome_produto.lower():
            marca = "Lotto"
        else:
            print("Marca não identificada.")
            marca = ''
        print("Marca: ", marca)
        return marca

    def scraping_chuteiras(self, inicial_page= int, total_pages=int):
        print("iniciando raspagem de dados.")
        dados = []

        # Abrir página
        self.driver.get(self.base_url + "&pg=" + str(inicial_page))
        print("Navegando para: ", self.driver.title)
        sleep(1)

        print(f"Serão raspadas um total de {total_pages} páginas.")

        for page in range(inicial_page, total_pages+1):
            print(f"Iniciando {inicial_page}/{total_pages}")
            self.wdw.until(partial(self.esperar_elemento, By.CSS_SELECTOR, 'div[class="lister-grid__content"]'))

            div_chuteiras = self.driver.find_element(By.CSS_SELECTOR, 'div[class="lister-grid__content"]')
            chuteiras = div_chuteiras.find_elements(By.CSS_SELECTOR, 'div[data-id]')

            try:
                self.driver.find_element(By.CSS_SELECTOR, 'a[class="z-close"]').click()
            except:
                pass
  
            # Para cadachuteira na página, entrar e extrair os dados
            for chuteira in range(0, len(chuteiras)):
                dados_chuteira = []

                # Pegar dados das chuteiras
                div_chuteiras = self.driver.find_element(By.CSS_SELECTOR, 'div[class="lister-grid__content"]')
                chuteiras = div_chuteiras.find_elements(By.CSS_SELECTOR, 'div[data-id]')

                # Entrar na página
                self.wdw.until(partial(self.esperar_elemento, By.CSS_SELECTOR, 'div[class="lister-grid__item "]'))
                self.action.scroll_to_element(chuteiras[chuteira])
                self.action.scroll_by_amount(0, 50)
                self.action.perform()
                sleep(0.2)
                chuteiras[chuteira].click()

                # Esperar carregar página
                self.wdw.until(partial(self.esperar_elemento, By.CSS_SELECTOR, 'button[data-id="218547736"]'))

                # Se aparecer um erro na página
                if len(self.driver.find_elements(By.CSS_SELECTOR, 'h1[class="content__title"]')) == 1:

                    # Página de erro
                    print("Desculpe! Parece haver um problema em algum lugar com a ProDirect. Voltando a página inicial...")
                    self.driver.back()

                    # Enquanto não estiver pagination na tela, espera
                    while len(self.driver.find_elements(By.CSS_SELECTOR, 'div[class="pagination__summary"]')) == 0:
                        continue

                    continue

                # Se abrir pop-up newsltr, fechar.
                if len(self.driver.find_elements(By.CSS_SELECTOR, 'button[class="newsltr__close js-newsltr-close"]')) == 1:
                    botao = self.driver.find_element(By.CSS_SELECTOR, 'button[class="newsltr__close js-newsltr-close"]')
                    try:
                        botao.click()
                        sleep(1.5)
                    except:
                        pass

                # Descrição
                self.wdw.until(partial(self.esperar_elemento, By.CSS_SELECTOR, 'div[class="ml-tab-content__copy"]'))
                self.wdw.until(partial(self.esperar_elemento, By.CSS_SELECTOR, 'button[data-id="1557958961"]'))

                try:
                    self.driver.find_element(By.CSS_SELECTOR, 'button[data-id="1557958961"]').click()
                    sleep(0.5)
                except:
                    pass

                description = self.driver.find_element(By.CSS_SELECTOR, 'div[class="ml-tab-content__copy"]').text
                descricao = self.tradutor(description)
                descricao = descricao.replace('bota', 'chuteira').replace('botas', 'chuteiras').replace('Bota', 'Chuteira').replace('Botas', 'Chuteiras')

                # Guardando variavel Features
                aba_features = self.driver.find_element(By.CSS_SELECTOR, 'button[data-id="218547736"]')
                aba_features.click()

                # Scrap dados
                sku_produto = self.driver.find_element(By.CSS_SELECTOR, 'ul[class="ml-tab-content__list"]').text.split()[2]

                # Nome do produto
                titulo_produto = self.driver.find_element(By.CSS_SELECTOR, 'h1[class="ml-meta__title"]').text.split('\n')[0].replace('bota', 'chuteira').replace('botas', 'chuteiras').replace('Bota', 'Chuteira').replace('Botas', 'Chuteiras')
                
                # Marca
                marca = self.extrair_marca(titulo_produto)

                # Numeros disponíveis
                tamanhos_disponiveis = []
                div_sizes = self.driver.find_element(By.CSS_SELECTOR, 'div[class="ml-size__sizes"]')
                sizes = div_sizes.find_elements(By.CSS_SELECTOR, 'button[class="ml-size__size qa-size-item"]')
                for size in sizes:
                    tamanhos_disponiveis.append(size.text)
                tamanhos = self.uk_to_br_shoe_sizes(marca, tamanhos_disponiveis)

                try:
                    color = self.driver.find_element(By.CSS_SELECTOR, 'h1[class="ml-meta__title"]').text.split('\n')[1]
                except:
                    color = ''
                departament = self.driver.find_element(By.CSS_SELECTOR, 'div[class="ml-meta__department"]').text
                departamento = self.tradutor(departament).replace('bota', 'chuteira').replace('botas', 'chuteiras').replace('Bota', 'Chuteira').replace('Botas', 'Chuteiras')

                # Preços
                price = self.driver.find_element(By.CSS_SELECTOR, 'div[class="ml-prices__price"]').text.split('£')[1]
                price_float = float(price)

                preco = self.convert_price(price_float)

                try:
                    # Se for promoção
                    preco_original = self.driver.find_element(By.CSS_SELECTOR, 'div[class="ml-prices__price ml-prices__price--original"]').text
                    valor_promocao = self.driver.find_element(By.CSS_SELECTOR, 'div[class="ml-prices__price ml-prices__price--saving"]').text.split(' ')[1]

                    print(f'Preco: £{price}, convetido: {preco}, preco original: {preco_original}, promo: {valor_promocao}')
                    print("Produto promocional")
                    
                except:
                    print("Produto Comum")
                    print(f'Preço: £{price} | Convetido: {preco}')
                    pass

                # Postando na loja
                imgs = self.scrap_images()

                dados_chuteira.append(titulo_produto)
                dados_chuteira.append(marca)
                dados_chuteira.append(preco)
                dados_chuteira.append(tamanhos)
                dados_chuteira.append(color)
                dados_chuteira.append(descricao)

                # Voltar
                self.driver.back()
                tamanhos_disponiveis = []

                # Enquanto não estiver pagination na tela, espera
                while len(self.driver.find_elements(By.CSS_SELECTOR, 'div[class="pagination__summary"]')) == 0:
                    continue

                print(f'dados da {chuteira+1}° chuteira: {titulo_produto} extraídos. Page: {page}/{total_pages}\n')
                dados.append(dados_chuteira)

            if chuteira+1 > total_pages:
                print("Raspagem finalizada.")
                break

            # Ir para a próxima página
            link = f"{self.base_url}&pg={page+1}"
            self.driver.get(link)

            # Esperar 
            while self.driver.current_url != link:
                continue

        return dados

    def close(self):
        self.driver.quit()

    def __del__(self):
        return super().__del__()
