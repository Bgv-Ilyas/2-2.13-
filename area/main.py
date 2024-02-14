from area import add_flight
from area import display_flights_by_destination
def main():
    destinations_list = []
    while True:
        print("\n1. Добавить рейс")
        print("2. Вывести рейсы по пункту назначения")
        print("3. Выйти")
        choice = input("Выберите действие (1/2/3): ")

        if choice == '1':
            add_flight(destinations_list)
        elif choice == '2':
            display_flights_by_destination(destinations_list)
        elif choice == '3':
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите 1, 2 или 3.")

if __name__ == '__main__':
    main()
