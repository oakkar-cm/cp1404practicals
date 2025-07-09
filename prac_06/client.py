from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(fuel=180)  # Using keyword to be explicit
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    bmw = Car("BMW", 100)
    bmw.add_fuel(20)
    print(f"{bmw.name} has fuel: {bmw.fuel}")
    bmw.drive(130)
    print(bmw)


if __name__ == '__main__':
    main()

