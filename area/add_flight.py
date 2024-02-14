def add_flight(destinations):
    destination = input("Введите пункт назначения: ")
    flight_number = input("Введите номер рейса: ")
    plane_type = input("Введите тип самолета: ")

    flight_info = {
        'название пункта назначения': destination,
        'номер рейса': flight_number,
        'тип самолета': plane_type
    }

    destinations.append(flight_info)
    destinations.sort(key=lambda x: x['номер рейса'])
    print("Информация о рейсе добавлена.")