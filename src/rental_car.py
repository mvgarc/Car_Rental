class RentalCar:
    def __init__(self, car,price,brand):
        """
        Inicializa un objeto RentalCar con su nombre, precio y marca.
        
        :param car: Nombre del carro
        :param price: Precio de alquiler por día
        :param brand: Marca del carro
        """
        self.car = car
        self.price = price
        self.brand = brand
        self.available = True # Indica si el carro está disponible para alquilar