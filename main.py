from abc import ABC, abstractmethod
import time


class CarShop(ABC):
    print("Welcome to car sales company")
    print("________________________________________________")
    print("Select machine type")

    def __init__(self, data) -> None:
        self.data = data
    
    @abstractmethod
    def show_info(self):
        pass


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
        for index,methods in enumerate(payment_methods):
            print(f"{index + 1}", methods)
        return self.select(payment_methods, "Enter payment method number: ")


class CarType(CarShop): 

    def show_info(self):
        for index, item in enumerate(self.data):
            print(f"{index + 1}) {item['type']}")

    def select_car_type(self):
        while True:
            try:
                type_input = int(input("Select car type: "))
                if 1 <= type_input <= len(self.data):
                    selected_type = self.data[type_input - 1]['type']
                    print(f"You chose: {selected_type}")
                    return selected_type
                else:
                    print("Invalid machine type ID.")
            except ValueError:
                print("Invalid machine type ID.")    


class CarModel(CarShop):

    def show_info(self):
        for index, item in enumerate(self.data):
            print(f"{index + 1}) {item['model']}")

    def select_car_model(self, selected_type):
        print(f"Available models for {selected_type}:")
        while True:
            try:
                model_input = int(input("Select car model: "))
                if 1 <= model_input <= len(self.data):
                    selected_model = self.data[model_input - 1]['model']
                    print(f"You chose: {selected_model}")
                    return selected_model
                else:
                    print("Invalid machine model ID.")
            except ValueError:
                print("Invalid machine model ID.")


class CarColor(CarShop):
    def show_info(self):
        for index, color in enumerate(self.data):
            print(f"{index + 1}) {color}")

    def select_car_color(self, selected_model):
        print(f"Available colors for {selected_model}:")
        while True:
            try:
                color_input = int(input("Select car color: "))
                if 1 <= color_input <= len(self.data):
                    selected_color = self.data[color_input - 1]
                    print(f"You chose: {selected_color}")
                    return selected_color
                else:
                    print("Invalid color ID.")
            except ValueError:
                print("Invalid color ID.")


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

    car_type = CarType(car_data)
    car_type.show_info()

    selected_type = car_type.select_car_type()
    selected_models = [item['models'] for item in car_data if item['type'] == selected_type][0]

    car_model = CarModel(selected_models)
    car_model.show_info()
    
    selected_model = car_model.select_car_model(selected_type)
    car_color = CarColor(colors)
    car_color.show_info()
    selected_color = car_color.select_car_color(selected_model)
    car_price = CarPrice()
    car_price.show_info([item['price'] for item in selected_models if item['model'] == selected_model][0])
    payment_method = car_type.select_payment_method()

    if payment_method == "Credit card":
        payment = CreditPayment()
    elif payment_method == "Cash":
        payment = CashPayment()

    payment.pay()

    print("Information is being processed")
    time.sleep(10)


if __name__ == "__main__":
    main()