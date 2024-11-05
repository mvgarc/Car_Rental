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
    
    def return_car(self, car):
        """
        Permite al usuario devolver un carro previamente alquilado.
        
        :param car: Instancia de la clase RentalCar
        """
        if car in self.borrowed_cars:
            car.return_car()
            self.borrowed_cars.remove(car)
            print(f"{self.name} ha devuelto el carro {car.car}")
        else:
            print(f"{self.name} no tiene el carro {car.car} para devolver")