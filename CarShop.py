from abc import ABC, abstractmethod

class ShowroomCars(ABC):

    @abstractmethod
    def viwer_info(self):
        pass

    @abstractmethod
    def select(self):
        pass


class TypeCars(ShowroomCars):
    pass


class ModelCars():
    pass


class ColorCars():
    pass


class PriceCars():
    pass

class Payment(ABC):
    pass


def main():
    pass


if __name__ == "__main__":
    main()