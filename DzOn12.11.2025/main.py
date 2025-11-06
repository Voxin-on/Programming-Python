import requests

city = input("Введите название города: ")
api="8099b7b090552315b53adc6aa6dd7c37"

response = requests.get("http://api.openweathermap.org/data/2.5/weather", params={"q": city,
                                                                                  "appid": api,
                                                                                  "units": "metric",
                                                                                  "lang": "ru"})

if response.status_code == 200:
    info = response.json()

    print(f"\nГород: {info['name']}")
    print(f"Погода: {info['weather'][0]['description']}")
    print(f"Температура: {info['main']['temp']}°C")
    print(f"Ощущается как: {info['main']['feels_like']}°C")
    print(f"Влажность: {info['main']['humidity']}%")
    print(f"Скорость ветра: {info['wind']['speed']} м/с")
    print(f"Облачность: {info['clouds']['all']}%")
else:
    print(f"\nНе удалось получить данные")