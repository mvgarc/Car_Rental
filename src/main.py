from rental_car import RentalCar
from user import User

# Crear instancias de carros
car1 = RentalCar("Toyota Corolla", 50, "Toyota")
car2 = RentalCar("Ford Fiesta", 40, "Ford")
car3 = RentalCar("Honda Civic", 60, "Honda")

# Crear una instancia de usuario
user1 = User("Maria", 1)

# Menú de interacción
while True:
    print("\n--- Sistema de Alquiler de Carros ---")
    print("1. Alquilar un carro")
    print("2. Devolver un carro")
    print("3. Ver carros alquilados")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        print("\nCarros disponibles para alquilar:")
        for car in [car1, car2, car3]:
            if car.available:
                print(f"- {car.car} ({car.brand}) - ${car.price}/día")

        carro_a_alquilar = input("Escribe el nombre del carro que quieres alquilar: ")

        if carro_a_alquilar == car1.car:
            user1.borrow_car(car1)
        elif carro_a_alquilar == car2.car:
            user1.borrow_car(car2)
        elif carro_a_alquilar == car3.car:
            user1.borrow_car(car3)
        else:
            print("Carro no encontrado o no disponible.")

    elif opcion == "2":
        print("\nCarros que has alquilado:")
        for car in user1.borrowed_cars:
            print(f"- {car.car} ({car.brand})")

        carro_a_devolver = input("Escribe el nombre del carro que quieres devolver: ")

        if carro_a_devolver == car1.car:
            user1.return_car(car1)
        elif carro_a_devolver == car2.car:
            user1.return_car(car2)
        elif carro_a_devolver == car3.car:
            user1.return_car(car3)
        else:
            print("No tienes ese carro para devolver.")

    elif opcion == "3":
        if user1.borrowed_cars:
            print("\nCarros alquilados:")
            for car in user1.borrowed_cars:
                print(f"- {car.car} ({car.brand})")
        else:
            print("\nNo has alquilado ningún carro.")

    elif opcion == "4":
        print("Gracias por usar el sistema de alquiler de carros.")
        break

    else:
        print("Opción no válida, por favor selecciona una opción del 1 al 4.")