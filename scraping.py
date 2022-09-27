from bs4 import BeautifulSoup
import requests
import pandas


# URL do Site (Seed - semente do crawler)
URL = "https://www.lidl.co.uk/food-offers"

headers = {
    'User-Agent':
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}  # Cabeçalho de Requisição para evitar cód 403 - Proibido
# https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status/403

site = requests.get(
    URL, headers=headers
)  # Site é a variável que irá guardar as informações desejadas da requisição web.

bs = BeautifulSoup(
    site.content, 'html.parser'
)  # bs é a variável que irá guardar toda a html. O parser faz o encode para html.

try:
    products = bs.find('div', class_='nuc-m-flex-container__container')

    names, prices = [], []

    for name in products.find_all('h3', class_='ret-o-card__headline'):
        name = name.get_text().replace('\n', '')
        names.append(name)
    for price in products.find_all('span', class_='lidl-m-pricebox__price'):
        price = price.get_text().replace('£', '').replace('.', ',').strip()
        prices.append (price)

except:
    price = ''
    print('Valor não encontrado.')

df = pandas.DataFrame(
    {
        "Nome": names,
        "Preço": prices
    })

print(df)

df.to_excel("lidl.xlsx") 