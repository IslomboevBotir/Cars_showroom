from abc import ABC, abstractmethod
import time


class CarShop:
    print("Welcome to car sales company")
    print("____________________________")
    print("Select machine type")

    def __init__(self, data) -> None:
        self.data = data

    def select(self, options, prompt):
        while True:
            try:
                choice = int(input(prompt))
                if 1 <= choice <= len(options):
                    return options[choice - 1]
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Invalid input.")

    def select_payment_method(self):
        print("Select payment method:")
        payment_methods = ["Credit card", "Cash"]
        for index, methods in enumerate(payment_methods):
            print(f"{index + 1}) {methods}")
        return self.select(payment_methods, "Enter payment method number: ")


class CarType(CarShop):

    def show_info(self):
        print("Select car type:")
        for index, item in enumerate(self.data):
            print(f"{index + 1}) {item['type']}")

    def select_car_type(self):
        selected_type = self.select([item['type'] for item in self.data], "Enter type number:")
        print(f"You chose: {selected_type}")
        return selected_type


class CarModel(CarShop):

    def show_info(self, models):
        print("Select car model:")
        for index, model in enumerate(models):
            print(f"{index + 1}) {model['model']}")

    def select_car_model(self, models):
        selected_model = self.select(models, "Enter model number:")
        print(f"You chose: {selected_model['model']}")
        return selected_model
    

class CarColor(CarShop):

    def show_info(self, colors):
        print("Select car color:")
        for index, color in enumerate(colors):
            print(f"{index + 1}) {color}")

    def select_car_color(self, colors):
        selected_color = self.select(colors, "Enter color number:")
        print(f"You chose: {selected_color}")
        return selected_color


class CarPrice:

    def show_info(self, selected_price):
        print(f"Price: ${selected_price}")


class PaymentMethod(ABC):

    @abstractmethod
    def pay(self):
        pass


class CreditPayment(PaymentMethod):

    def pay(self):
        print("Payment by Credit card")


class CashPayment(PaymentMethod):

    def pay(self):
        print("Payment by Cash")


def main():
# Информация о типах, моделях и ценах автомобилей
    car_data = [
        {
            'type': "Sedan",
            'models': [
                {'model': "Toyota Camry", 'price': 25000},
                {'model': "Skoda Superb", 'price': 22000},
                {'model': "Volkswagen Polo Sedan", 'price': 21000},
            ]
        },
        {
            'type': "Hatchback",
            'models': [
                {'model': "Nissan Leaf", 'price': 30000},
                {'model': "Audi A1", 'price': 28000},
                {'model': "MINI Hatch", 'price': 27000},
            ]
        },
        {
            'type': "Coupe",
            'models': [
                {'model': "Audi A5", 'price': 35000},
                {'model': "Hyundai Genesis", 'price': 32000},
                {'model': "Infiniti G37", 'price': 33000},
            ]
        },
        {
            'type': "Minivan",
            'models': [
                {'model': "Toyota Vellfire", 'price': 28000},
                {'model': "Toyota Alphard", 'price': 29000},
                {'model': "Toyota Prius Alpha", 'price': 27000},
            ]
        },
        {
            'type': "Suv",
            'models': [
                {'model': "Lexus RX450h", 'price': 42000},
                {'model': "Lexus LX570", 'price': 45000},
                {'model': "Infiniti FX37", 'price': 43000},
            ]
        },
    ]

    colors = ["Black", "White", "Grey"]

    car_shop = CarShop(car_data)
    car_type = CarType(car_data)
    car_model = CarModel(car_data)
    car_color = CarColor(colors)
    car_price = CarPrice()
    payment_method = PaymentMethod

    car_type.show_info()
    selected_type = car_type.select_car_type()
    selected_models = []
    for item in car_data:
        if item['type'] == selected_type:
            selected_models = item['models']
    car_model.show_info(selected_models)
    selected_model = car_model.select_car_model(selected_models)
    car_color.show_info(colors)
    selected_color = car_color.select_car_color(colors)
    car_price.show_info([item['price'] for item in selected_models if item['model'] == selected_model['model']][0])

    payment_method = car_shop.select_payment_method()

    if payment_method == "Credit card":
        payment = CreditPayment()
    elif payment_method == "Cash":
        payment = CashPayment()

    payment.pay()
    
    print("Information is being processed")
    print("______________________________")
    time.sleep(5)
    print("Congratulations on placing your order")

    
if __name__ == "__main__":
    main()
