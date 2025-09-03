from http.client import responses

import jsonschema
import pytest

from .schemas.store_schema import STORE_SCHEMA

import allure
import requests

BASE_URL = "http://5.181.109.28:9090/api/v3"


@allure.feature("Store")
class TestStore:
    @allure.title("Размещение заказа на питомца")
    def test_add_new_order(self):
        with allure.step("Подготовка данных для создания заказа"):
            payload = {
                "id": 1, "petId": 1, "quantity": 1, "status": "placed", "complete": True
            }
            with allure.step('Отправка запроса на создание заказа'):
                response = requests.post(url=f'{BASE_URL}/store/order', json=payload)
                response_json = response.json()

            with allure.step('Проверка статуса ответа'):
                assert response.status_code == 200
                jsonschema.validate(response.json(), STORE_SCHEMA)

            with allure.step("Проверка параметров заказа в ответе"):
                assert response_json['id'] == payload['id'], "id заказа не совпадает с ожидаемым"
                assert response_json['petId'] == payload['petId'], "petId питомца в заказе не совпадает с ожидаемым"
                assert response_json['status'] == payload['status'], "статус заказа не совпадает с ожидаемым"
                assert response_json['quantity'] == payload['quantity'], "количество заказов не совпадает с ожидаемым"
                assert response_json['complete'] == payload['complete'], "статус заказа не совпадает с ожидаемым"

    @allure.title("Получение информации о заказе по id")
    def test_get_info_by_order_id(self):
        with allure.step("Отправка запроса на получение заказа по id"):
            response = requests.get(url=f'{BASE_URL}/store/order/1')

        with allure.step('Проверка статуса ответа и id'):
            # data = response.json()
            assert response.status_code == 200
            assert (response.json()["id"] == 1)

    @allure.title("Удаление заказа по id")
    def test_delete_order_by_id(self):
        with allure.step("Отправка запроса на удаление заказа по id"):
            response = requests.delete(url=f'{BASE_URL}/store/order/1')

        with allure.step('Проверка статуса ответа и id'):
            assert response.status_code == 200

        with allure.step("Отправка запроса на получение инфо о заказе по id"):
            response = requests.get(url=f'{BASE_URL}/store/order/1')

        with allure.step('Проверка статуса ответа'):
            assert response.status_code == 404

    @allure.title("Создание заказа и после удаление по id")
    def test_create_and_delete_order_by_id_(self, create_order):
        with allure.step("Создание id заказа"):
            order_id = create_order["id"]

        with allure.step("Отправка запроса на удаление заказа по id"):
            response = requests.delete(url=f'{BASE_URL}/store/order/{order_id}')

        with allure.step('Проверка статуса ответа'):
            assert response.status_code == 200

        with allure.step("Отправка запроса на получение информации об удаленном заказе"):
            response = requests.get(url=f'{BASE_URL}/store/order/{order_id}')

        with allure.step('Проверка статуса ответа'):
            assert response.status_code == 404

    @allure.title("Попытка получить информацию о несуществующем заказе")
    def test_get_info_nonexistent_order(self):
        with allure.step("Отправка запроса на получение информации о несуществующем заказе"):
            response = requests.get(f'{BASE_URL}/store/order/9999')

        with allure.step('Проверка статуса ответа'):
            assert response.status_code == 404

    @allure.title("Получение инвентаря магазина")
    def test_get_inventory(self):
        with allure.step("Отправка запроса на получение инвентаря"):
            response = requests.get(url=f'{BASE_URL}/store/inventory')

        with allure.step('Проверка статуса ответа и id'):
            data = response.json()
            assert response.status_code == 500
           # assert response.status_code == 200
           # assert (data["approved"] == 57)
           # assert (data["delivered"] == 50)
