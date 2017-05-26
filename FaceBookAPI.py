# import facebook
# graph = facebook.GraphAPI(access_token='EAACEdEose0cBAGW4gNQM7ae64dyZCBrtDnZCJ2kERrrBENmPLXa57a2nZC0ToWZCwdHuzd3cRlkU6yGPRIqbuNGwZCpTSCZC2yf6o32Mg4oxuZBdwBM7L96v3vnmLku3kfHkZC0xj8TZC1zh79pHOhg0MhmlifDBSuCWEi47FSbJlXA7rfHVQZCT050SG1BvAc8ZA8N6Oj2h49AHilW7halxSZCI1bE8C9sH2woZD', version='2.9')
# # graph = facebook.GraphAPI(page_access_token)
# graph.put_object("926447064079499", "feed", message='Good Night!!'
#                                                     'sent using facebook API SDK')
import pyowm

owm = pyowm.OWM('797d4e58182603744d65cac86625d912')  # You MUST provide a valid API key


# Will it be sunny tomorrow at this time in Milan (Italy) ?
forecast = owm.daily_forecast("Amritsar,India")
tomorrow = pyowm.timeutils.tomorrow()
forecast.will_be_sunny_at(tomorrow)  # Always True in Italy, right? ;-)

# Search for current weather in London (UK)
observation = owm.weather_at_place('Amritsar,India')
w = observation.get_weather()
print(w)                      # <Weather - reference time=2013-12-18 09:20,
                              # status=Clouds>

# Weather details
l=w.get_wind()                  # {'speed': 4.6, 'deg': 330}
print(l)
l=w.get_humidity()              # 87
print(l)
w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
print(l)
# Search current weather observations in the surroundings of
# lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
observation_list = owm.weather_around_coords(-22.57, -43.12)