# from celery import shared_task
# from pcp.models import Product, Shop, Price
# from bs4 import BeautifulSoup
# import requests
# import django
# django.setup()
#
# @shared_task
# def refresh_products_prices():
#     products = Product.objects.all()
#     for product in products:
#         url = product.url
#         soup = get_data(url)
#         lista = parse(soup)
#         loadup(lista, product)
#
#
# def get_data(url):
#     r = requests.get(url)
#     if r.status_code != 200:
#         print('Nie można pobrać danych!: ', r.status_code)
#     else:
#         soup = BeautifulSoup(r.text, "html.parser")
#         print(soup.title.text)
#     return soup
#
#
# def parse(soup):
#     products_list = []
#     records = soup.find_all("div", {
#         "class": "product-offer__container clickable-offer js_offer-container-click js_product-offer"})
#     for item in records:
#         product = {
#             "sklep": item.find('a', {"class": "store-logo go-to-shop"}).img['alt'],
#             'cena': item.find('span', {"class": "price-format nowrap"}).text.replace("zł", ""),
#             "link": "https://www.ceneo.pl"+item.find('a', {"class": "button button--primary button--flex go-to-shop"})['href'],
#         }
#         products_list.append(product)
#     return products_list
#
#
# def loadup(products_list, product):
#     for item in products_list:
#         shop, created = Shop.objects.get_or_create(name=item['shop'], product=product, product_url=item['link'])
#         price = Price.objects.create(shop=shop, price=item['price'])
