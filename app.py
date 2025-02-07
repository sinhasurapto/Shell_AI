import pandas as pd      
import numpy as np       
import pickle
import streamlit as st    

# Columns
columns = ['temperature_2_m_above_gnd', 'relative_humidity_2_m_above_gnd',
       'mean_sea_level_pressure_MSL', 'total_precipitation_sfc',
       'snowfall_amount_sfc', 'total_cloud_cover_sfc',
       'high_cloud_cover_high_cld_lay', 'medium_cloud_cover_mid_cld_lay',
       'low_cloud_cover_low_cld_lay', 'shortwave_radiation_backwards_sfc',
       'wind_speed_10_m_above_gnd', 'wind_direction_10_m_above_gnd',
       'wind_speed_80_m_above_gnd', 'wind_direction_80_m_above_gnd',
       'wind_speed_900_mb', 'wind_direction_900_mb',
       'wind_gust_10_m_above_gnd', 'angle_of_incidence', 'zenith', 'azimuth',
       'generated_power_kw']

# Load the model
pickle_in = open('lr.pkl', 'rb')
model = pickle.load(pickle_in)

# Load the scaler
pickle_in_scaler = open('sc.pkl', 'rb')
scaler = pickle.load(pickle_in_scaler)

# Function to perform prediction
def predict(data_frame):
    scaled_data = scaler.transform(data_frame)
    prediction = model.predict(scaled_data)
    return prediction[0]


# Function to accept inputs and predict from inputs
def main():
    # Set up the application
    st.title('Solar Power Predictor')
    html_temp = '''
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;"> Solar Power Prediction App </h2>
    </div>
    '''
    st.markdown(html_temp, unsafe_allow_html = True)

    # Specify the inputs
    st.write("Please enter values for all the parameters (if not default)!!!")
    temperature_2_m_above_gnd = st.text_input("Temperature 2 metres above ground") 
    relative_humidity_2_m_above_gnd = st.text_input("Relative humidity 2 metres above ground") 
    mean_sea_level_pressure_MSL = st.text_input("Mean sea level pressure") 
    total_precipitation_sfc = st.text_input("Total precipitation")
    snowfall_amount_sfc = st.text_input("Snowwfall")
    total_cloud_cover_sfc = st.text_input("Total cloud cover")
    high_cloud_cover_high_cld_lay = st.text_input("High cloud cover")
    medium_cloud_cover_mid_cld_lay = st.text_input("Medium cloud cover")
    low_cloud_cover_low_cld_lay = st.text_input("Low cloud cover")
    shortwave_radiation_backwards_sfc = st.text_input("Shortwave radiation") 
    wind_speed_10_m_above_gnd = st.text_input("Wind speed 10 metres above ground") 
    wind_direction_10_m_above_gnd = st.text_input("Wind direction 10 metres above ground") 
    wind_speed_80_m_above_gnd = st.text_input("Wind speed 80 metres above ground") 
    wind_direction_80_m_above_gnd = st.text_input("Wind direction 80 metres above ground") 
    wind_speed_900_mb = st.text_input("Wind speed at 900 mbar") 
    wind_direction_900_mb = st.text_input("Wind direction at 900 mbar") 
    wind_gust_10_m_above_gnd = st.text_input("Wind gusts 10 metres above ground") 
    angle_of_incidence = st.text_input("Angle of incidence") 
    zenith = st.text_input("Zenith") 
    azimuth = st.text_input("Azimuth") 

    # Combine into an input data
    data_dict = {
        'temperature_2_m_above_gnd': [temperature_2_m_above_gnd],
        'relative_humidity_2_m_above_gnd': [relative_humidity_2_m_above_gnd],
        'mean_sea_level_pressure_MSL': [mean_sea_level_pressure_MSL],
         'total_precipitation_sfc': [total_precipitation_sfc],
         'snowfall_amount_sfc': [snowfall_amount_sfc],
         'total_cloud_cover_sfc': [total_cloud_cover_sfc],
         'high_cloud_cover_high_cld_lay': [high_cloud_cover_high_cld_lay],
         'medium_cloud_cover_mid_cld_lay': [medium_cloud_cover_mid_cld_lay],
         'low_cloud_cover_low_cld_lay': [low_cloud_cover_low_cld_lay],
         'shortwave_radiation_backwards_sfc': [shortwave_radiation_backwards_sfc],
         'wind_speed_10_m_above_gnd': [wind_speed_10_m_above_gnd],
         'wind_direction_10_m_above_gnd': [wind_direction_10_m_above_gnd],
         'wind_speed_80_m_above_gnd': [wind_speed_80_m_above_gnd],
         'wind_direction_80_m_above_gnd': [wind_direction_80_m_above_gnd],
         'wind_speed_900_mb': [wind_speed_900_mb],
         'wind_direction_900_mb': [wind_direction_900_mb],
         'wind_gust_10_m_above_gnd': [wind_gust_10_m_above_gnd],
         'angle_of_incidence': [angle_of_incidence],
         'zenith': [zenith],
         'azimuth': [azimuth]
    }
    df = pd.DataFrame(data_dict)

    # Predict button
    if st.button('Predict'):
        result = predict(df)
        st.success(f"Solar power output is {result} kilowatt.")

# Run the application
if __name__=='__main__': 
    main() 




