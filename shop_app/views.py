from django.shortcuts import render
from django.http import HttpResponse
import logging
from shop_app.models import Client, Order, Product

logger = logging.getLogger(__name__)                # переменная для логирования

def main(request):
    page_main = """
        <div>
            <ul>
                <li><a href="http://127.0.0.1:8000/shop/clients/">список всех клиентов</a></li>
                <li><a href="http://127.0.0.1:8000/shop/products/">список всех товаров</a></li>
                 <li><a href="http://127.0.0.1:8000/shop/orders/">список всех заказов</a></li>
            </ul>
        </div>
        <form action='http://127.0.0.1:8000/' target="_blank">
            <button>Начальная страница</button>
        </form>
        <br>
        <footer>
            <div>
                <p> Контакты: Россия, Воронеж, ул. Люзикова</p>
            </div>
        </footer>
        """
    logger.info(f'Страница "Главная" успешно открыта')

    return HttpResponse(page_main)


# вывод всех товаров
def products(request):
    list_products = []
    products = Product.objects.all()                        #получение данных из табл Product  БД
    for product in products:
        list_products.append(product)
    logger.info(f'Страница "Список продуктов" успешно открыта')
    return HttpResponse(list_products)


#вывод списка всех клиентов
def clients(request):
    list_clients = []
    clients = Client.objects.all()
    for client in clients:
        list_clients.append(client)
    logger.info(f'Страница "Список клиентов" успешно открыта')
    return HttpResponse(list_clients)


# вывод заказа по  id
def order(request, id_order: int):
    orders = Order.objects.filter(pk=id_order).first()
    return HttpResponse(orders, orders.products)


#вывод списка заказов
def orders(request):
    list_orders = []
    string = ''
    orders = Order.objects.all()
    for order in orders:
        list_orders.append(order)
        string += str(order) + '\n'
    return HttpResponse(string)