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

        if car.available:
            car.borrow()
            self.borrowed_cars.append(car)