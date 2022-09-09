from multiprocessing.sharedctypes import Value
import streamlit as st
import requests
from datetime import datetime

API_KEY = "4a39c4159c2baebee624d9f03d854bbd"

def find_current_weather(city):
    base_url  = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    weather_data = requests.get(base_url).json()
    try:
        general = weather_data['weather'][0]['main']
        icon_id = weather_data['weather'][0]['icon']
        temperature = round(weather_data['main']['temp'])
        icon = f"http://openweathermap.org/img/wn/{icon_id}@2x.png"
        wind_speed = weather_data['wind']["speed"]
        hmdt = weather_data['main']['humidity']
        max_temp = weather_data['main']['temp_max']
    except KeyError:
        st.error("City Not Found")
        st.stop()
    return general,temperature,icon,wind_speed,hmdt,max_temp





def main():
    st.header("Find the Weather")
    city = st.text_input("Enter the City").lower()
    if st.button("Find"):

        general,temperature,icon,wind_speed,hmdt,max_temp= find_current_weather(city)

        date = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

        st.write("#### Weather stats for : {},  {}".format(city.upper(), date))
        col_1,col_2,col_3 = st.columns(3)
        with col_1:
            st.metric(label = "Temperature", value=f"{temperature}°C")
            st.metric(label = "Humidity", value=f"{hmdt}%")
        with col_2:
            st.metric(label = "Weather description", value=f"{general}")
            st.image(icon)
        with col_3:
            st.metric(label = "Wind Speed", value=f"{wind_speed}kmph")
            st.metric(label = "Max Temperature", value=f"{max_temp}")
            
    



    
if __name__ == '__main__':
    main()

