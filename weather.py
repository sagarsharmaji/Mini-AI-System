import pyowm, datetime
from S_to_T import SpeakText

api_key = '7338e7357146d6c783067cc3a4b5bd03'    #your API Key here as string
owm = pyowm.OWM(api_key).weather_manager()     # Use API key to get data

def print_weather(data):
    ref_time = datetime.datetime.fromtimestamp( data.ref_time ).strftime('%Y-%m-%d %H:%M')
    # print( f"Time\t\t: {  ref_time }" )
    # print( f"Overview\t: { data.detailed_status}" )
    # print( f"Wind Speed\t: { data.wind()}" )
    # print( f"Humidity\t: { data.humidity}" )
    # print( f"Temperature\t: { data.temperature('celsius')}" )
    # print( f"Rain\t\t: { data.rain}" )
    # print("\n")
    SpeakText("Your Weather Details for the Date..") 
    SpeakText(ref_time)
    SpeakText("Overview.")
    SpeakText(data.detailed_status)
    SpeakText("Wind Speed details.")
    SpeakText(data.wind())
    SpeakText("Humidity is.")
    SpeakText(data.humidity)
    SpeakText("Temperature Details.")
    SpeakText(data.temperature('celsius'))

def get_current_weather():
    weather_api = owm.weather_at_place('Pune')  # give where you need to see the weather
    weather_data = weather_api.weather          # get out data in the mentioned location

    # print("***Current Weather***")
    print_weather( weather_data )
    # print("\n")

# def get_forecast_weather():
#     print("***5 day forecast Weather***")
#     for item in owm.forecast_at_place('Pune', '3h').forecast:
#         print_weather( item )

if __name__ == '__main__':
    get_current_weather()
    # get_forecast_weather()