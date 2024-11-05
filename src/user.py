class User:
    def __init__(self,name,user_id):
        """
        Inicializa un objeto User con un nombre y un ID de usuario.
        
        :param name: Nombre del usuario
        :param user_id: ID único del usuario
        """
        self.name = name
        self.user_id = user_id
        self.borrowed_cars = [] # Lista para rastrear los carros alquilados por el usuario

    def borrow_car(self,car):
        """
        Permite al usuario alquilar un carro si está disponible.
        
        :param car: Instancia de la clase RentalCar
        """
        if car.available:
            car.borrow()
            self.borrowed_cars.append(car)
            print(f"{self.name} ha alquilado el carro {car.car}")
        else:
            print(f"{self.name} no puede alquilar el carro {car.car}, no está disponible")