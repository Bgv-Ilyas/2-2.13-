def display_flights_by_destination(destinations):
    search_destination = input("Введите пункт назначения для поиска: ")
    matching_flights = [
        (flight['номер рейса'], flight['тип самолета'])
        for flight in destinations
        if flight['название пункта назначения'] == search_destination
    ]

    if matching_flights:
        print(f"Рейсы в пункт назначения '{search_destination}':")
        for flight_number, plane_type in matching_flights:
            print(f"Номер рейса: {flight_number}, Тип самолета: {plane_type}")
    else:
        print(f"Рейсов в пункт назначения '{search_destination}' не найдено.")
