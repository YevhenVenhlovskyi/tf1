from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

# ---------- FREE API KEY examples ---------------------

owm = OWM('48655dd4afc8f7fc78f2c0a04dd09219')    ## my own (default) key
mgr = owm.weather_manager()

city_name=input("Для перегляду погоди, введіть назву міста: ")

# Search for current weather in London (Great Britain) and get details
observation = mgr.weather_at_place(city_name)
w = observation.weather

# w.detailed_status         # 'clouds'
# w.wind()                  # {'speed': 4.6, 'deg': 330}
# w.humidity                # 87
# w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
# w.rain                    # {}
# w.heat_index              # None
# w.clouds                  # 75

print ("******************* Погода у місті {}: ***********************".format(city_name))
print ("Опади: ", w.detailed_status)
print ("Швидкість вітру: {} м/сек".format(w.wind()['speed']))
print ("Вологість: {} мм рт.ст. ".format(w.humidity))
print ("Хмарність: {} %".format(w.clouds))
## Processing of temperature dictionary
text_1=("Температура: {}\xb0C; Відчувається як: {}\xb0C; Максимальна: {}\xb0C; Мінімальна: {}\xb0C")
x=w.temperature('celsius')
print(text_1.format(x['temp'],x['feels_like'],x['temp_max'],x['temp_min']))
print ("*******************************************************************")
