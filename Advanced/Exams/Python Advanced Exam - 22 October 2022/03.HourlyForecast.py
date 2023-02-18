# def forecast(*args):
#     locations = {}

#     for i in args:
#         if(i[0] not in locations):
#             locations[i[0]] = i[1]

#     sortedTown = {k: v for k, v in sorted(locations.items(), key=lambda x: (x[1], x[0]))}
    
#     sunny = ""
#     cloudy = ""
#     rainy = ""

#     for k, v in sortedTown.items():
#         if(v == "Sunny"):
#             sunny += f"{k} - {v}\n"
#         elif(v == "Cloudy"):
#             cloudy += f"{k} - {v}\n"
#         elif(v == "Rainy"):
#             rainy += f"{k} - {v}\n"

#     return sunny + cloudy + rainy




def forecast(*args):
    result = []

    def weather(typeOfWeather):
        sortedWeather = list(filter(lambda x: x[1] == typeOfWeather, args))
        [result.append(f"{el[0]} - {el[1]}") for el in sorted(sortedWeather, key=lambda x: (x[0]))]

    weather("Sunny")
    weather("Cloudy")
    weather("Rainy")

    return '\n'.join(result)


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))