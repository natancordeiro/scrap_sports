from woocommerce import API
from requests.exceptions import Timeout

def create_product(name, marca, sku, description, price, regular_price, sale_price, sizes, color, images):

    url = 'https://novo.oldfirm.com.br/' 
    ck = 'ck_6e46f21a216c31ff7cabc9d0f8390ebb236b322f'
    cs = 'cs_a6f7802da9c06b97d713e0013b5c3c2a21c63b5c' 

    wcapi = API(
        url=url,
        consumer_key=ck,
        consumer_secret=cs,
        version="wc/v3"
    )

    # Verificar se o produto já existe
    break_loop = 0
    for product in wcapi.get("products").json():
        if product['sku'] == sku:
            break_loop = 1
            return print(f"O {product['name']} já existe.")
    if break_loop == 0:
        print(f"O produto ainda não existe.")


    product = {
        "name": name,
        "sku": sku,
        "type": "simple",
        "description": description,
        "price": f"{price} BRL",
        "regular_price": f"{regular_price} BRL",
        "sale_price": f"{sale_price} BRL",
        "images": [],
        "attributes": [
            {
                "id": 18,
                "name": "Size",
                "position": 0,
                "visible": False,
                "variation": True,
                "options": 'BR ' + sizes
            },  
            {
                "id": 1,
                "name": "Color",
                "position": 2,
                "visible": True,
                "variation": False,
                "options": [ color ]
            }
        ],
    }

    # Upload product images
    for image_url in images:
            image_data = image_url
            image_name = image_url.split("/")[-1]
            image_alt = "Chuteira " + marca

            product['images'].append({
                "src": image_data, "name": image_name, "alt": image_alt
            })
    try:
        response = wcapi.post("products", product)
    except Timeout:
        print("Tempo esgotado.")
        pass        
    except Exception as e:
        print("Erro ao postar produto: ", e)

    # Imprimir a resposta
    print("Status de resposta: ", response.status_code)
    
def verificar_produto(sku_produto):
    # Infos API

    url = 'https://novo.oldfirm.com.br/' 
    ck = 'ck_6e46f21a216c31ff7cabc9d0f8390ebb236b322f'
    cs = 'cs_a6f7802da9c06b97d713e0013b5c3c2a21c63b5c' 

    wcapi = API(
        url=url,
        consumer_key=ck,
        consumer_secret=cs,
        version="wc/v3"
    )

    break_loop = 0
    for product in wcapi.get("products").json():
        if product['sku'] == sku_produto:
            print(f"O {product['name']} já existe.")
            break_loop = 1
            break
    if break_loop == 0:
        print(f"O produto ainda não existe.")

def get():
    url = 'https://novo.oldfirm.com.br/' 
    ck = 'ck_6e46f21a216c31ff7cabc9d0f8390ebb236b322f'
    cs = 'cs_a6f7802da9c06b97d713e0013b5c3c2a21c63b5c' 

    wcapi = API(
        url=url,
        consumer_key=ck,
        consumer_secret=cs,
        version="wc/v3"
    )

    for n, product in enumerate(wcapi.get("products").json()):
            print(product['attributes'])
