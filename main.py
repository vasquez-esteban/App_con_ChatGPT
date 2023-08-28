import streamlit as st

def temperature_conversion(input_value, conversion_type):
    if conversion_type == "Celsius to Fahrenheit":
        result = (input_value * 9/5) + 32
        return f"{input_value} Celsius is equal to {result:.2f} Fahrenheit"
    elif conversion_type == "Fahrenheit to Celsius":
        result = (input_value - 32) * 5/9
        return f"{input_value} Fahrenheit is equal to {result:.2f} Celsius"
    elif conversion_type == "Celsius to Kelvin":
        result = input_value + 273.15
        return f"{input_value} Celsius is equal to {result:.2f} Kelvin"
    elif conversion_type == "Kelvin to Celsius":
        result = input_value - 273.15
        return f"{input_value} Kelvin is equal to {result:.2f} Celsius"

def length_conversion(input_value, conversion_type):
    if conversion_type == "Feet to Meters":
        result = input_value * 0.3048
        return f"{input_value} Feet is equal to {result:.2f} Meters"
    elif conversion_type == "Meters to Feet":
        result = input_value / 0.3048
        return f"{input_value} Meters is equal to {result:.2f} Feet"
    elif conversion_type == "Inches to Centimeters":
        result = input_value * 2.54
        return f"{input_value} Inches is equal to {result:.2f} Centimeters"
    elif conversion_type == "Centimeters to Inches":
        result = input_value / 2.54
        return f"{input_value} Centimeters is equal to {result:.2f} Inches"

def weight_conversion(input_value, conversion_type):
    if conversion_type == "Pounds to Kilograms":
        result = input_value * 0.453592
        return f"{input_value} Pounds is equal to {result:.2f} Kilograms"
    elif conversion_type == "Kilograms to Pounds":
        result = input_value / 0.453592
        return f"{input_value} Kilograms is equal to {result:.2f} Pounds"
    elif conversion_type == "Ounces to Grams":
        result = input_value * 28.3495
        return f"{input_value} Ounces is equal to {result:.2f} Grams"
    elif conversion_type == "Grams to Ounces":
        result = input_value / 28.3495
        return f"{input_value} Grams is equal to {result:.2f} Ounces"

def volume_conversion(input_value, conversion_type):
    if conversion_type == "Gallons to Liters":
        result = input_value * 3.78541
        return f"{input_value} Gallons is equal to {result:.2f} Liters"
    elif conversion_type == "Liters to Gallons":
        result = input_value / 3.78541
        return f"{input_value} Liters is equal to {result:.2f} Gallons"
    elif conversion_type == "Cubic Inches to Cubic Centimeters":
        result = input_value * 16.3871
        return f"{input_value} Cubic Inches is equal to {result:.2f} Cubic Centimeters"
    elif conversion_type == "Cubic Centimeters to Cubic Inches":
        result = input_value / 16.3871
        return f"{input_value} Cubic Centimeters is equal to {result:.2f} Cubic Inches"

def time_conversion(input_value, conversion_type):
    if conversion_type == "Hours to Minutes":
        result = input_value * 60
        return f"{input_value} Hours is equal to {result:.2f} Minutes"
    elif conversion_type == "Minutes to Seconds":
        result = input_value * 60
        return f"{input_value} Minutes is equal to {result:.2f} Seconds"
    elif conversion_type == "Days to Hours":
        result = input_value * 24
        return f"{input_value} Days is equal to {result:.2f} Hours"
    elif conversion_type == "Weeks to Days":
        result = input_value * 7
        return f"{input_value} Weeks is equal to {result:.2f} Days"

def speed_conversion(input_value, conversion_type):
    if conversion_type == "Miles per Hour to Kilometers per Hour":
        result = input_value * 1.60934
        return f"{input_value} Miles per Hour is equal to {result:.2f} Kilometers per Hour"
    elif conversion_type == "Kilometers per Hour to Meters per Second":
        result = input_value * 1000 / 3600
        return f"{input_value} Kilometers per Hour is equal to {result:.2f} Meters per Second"
    # Add similar cases for other speed conversions

def area_conversion(input_value, conversion_type):
    if conversion_type == "Square Meters to Square Feet":
        result = input_value * 10.7639
        return f"{input_value} Square Meters is equal to {result:.2f} Square Feet"
    elif conversion_type == "Square Feet to Square Meters":
        result = input_value / 10.7639
        return f"{input_value} Square Feet is equal to {result:.2f} Square Meters"
    # Add similar cases for other area conversions

def energy_conversion(input_value, conversion_type):
    if conversion_type == "Joules to Calories":
        result = input_value * 0.239006
        return f"{input_value} Joules is equal to {result:.2f} Calories"
    elif conversion_type == "Calories to Kilojoules":
        result = input_value * 0.004184
        return f"{input_value} Calories is equal to {result:.2f} Kilojoules"
    # Add similar cases for other energy conversions

def pressure_conversion(input_value, conversion_type):
    if conversion_type == "Pascals to Atmospheres":
        result = input_value / 101325
        return f"{input_value} Pascals is equal to {result:.9f} Atmospheres"
    elif conversion_type == "Atmospheres to Pascals":
        result = input_value * 101325
        return f"{input_value} Atmospheres is equal to {result:.2f} Pascals"
    # Add similar cases for other pressure conversions

def data_size_conversion(input_value, conversion_type):
    if conversion_type == "Megabytes to Gigabytes":
        result = input_value / 1024
        return f"{input_value} Megabytes is equal to {result:.2f} Gigabytes"
    elif conversion_type == "Gigabytes to Terabytes":
        result = input_value / 1024
        return f"{input_value} Gigabytes is equal to {result:.2f} Terabytes"

st.title("Universal Converter App")

conversion_options = [
    "Temperature",
    "Length",
    "Weight/Mass",
    "Volume",
    "Time",
    "Speed",
    "Area",
    "Energy",
    "Pressure",
    "Data Size"
]

selected_conversion = st.selectbox("Select Conversion Category", conversion_options)

if selected_conversion == "Temperature":
    temperature_options = [
        "Celsius to Fahrenheit",
        "Fahrenheit to Celsius",
        "Celsius to Kelvin",
        "Kelvin to Celsius"
    ]
    selected_temperature_conversion = st.selectbox("Select Temperature Conversion", temperature_options)
    input_value = st.number_input("Enter value for conversion")
    result = temperature_conversion(input_value, selected_temperature_conversion)
    st.write(result)
    
elif selected_conversion == "Length":
    length_options = [
        "Feet to Meters",
        "Meters to Feet",
        "Inches to Centimeters",
        "Centimeters to Inches"
    ]
    selected_length_conversion = st.selectbox("Select Length Conversion", length_options)
    input_value = st.number_input("Enter value for conversion")
    result = length_conversion(input_value, selected_length_conversion)
    st.write(result)

elif selected_conversion == "Weight/Mass":
    weight_options = [
        "Pounds to Kilograms",
        "Kilograms to Pounds",
        "Ounces to Grams",
        "Grams to Ounces"
    ]
    selected_weight_conversion = st.selectbox("Select Weight Conversion", weight_options)
    input_value = st.number_input("Enter value for conversion")
    result = weight_conversion(input_value, selected_weight_conversion)
    st.write(result)

elif selected_conversion == "Volume":
    volume_options = [
        "Gallons to Liters",
        "Liters to Gallons",
        "Cubic Inches to Cubic Centimeters",
        "Cubic Centimeters to Cubic Inches"
    ]
    selected_volume_conversion = st.selectbox("Select Volume Conversion", volume_options)
    input_value = st.number_input("Enter value for conversion")
    result = volume_conversion(input_value, selected_volume_conversion)
    st.write(result)

elif selected_conversion == "Time":
    time_options = [
        "Hours to Minutes",
        "Minutes to Seconds",
        "Days to Hours",
        "Weeks to Days"
    ]
    selected_time_conversion = st.selectbox("Select Time Conversion", time_options)
    input_value = st.number_input("Enter value for conversion")
    result = time_conversion(input_value, selected_time_conversion)
    st.write(result)

elif selected_conversion == "Speed":
    speed_options = [
        "Miles per Hour to Kilometers per Hour",
        "Kilometers per Hour to Meters per Second"
        # Add other speed conversion options
    ]
    selected_speed_conversion = st.selectbox("Select Speed Conversion", speed_options)
    input_value = st.number_input("Enter value for conversion")
    result = speed_conversion(input_value, selected_speed_conversion)
    st.write(result)

elif selected_conversion == "Area":
    area_options = [
        "Square Meters to Square Feet",
        "Square Feet to Square Meters"
        # Add other area conversion options
    ]
    selected_area_conversion = st.selectbox("Select Area Conversion", area_options)
    input_value = st.number_input("Enter value for conversion")
    result = area_conversion(input_value, selected_area_conversion)
    st.write(result)

elif selected_conversion == "Energy":
    energy_options = [
        "Joules to Calories",
        "Calories to Kilojoules"
        # Add other energy conversion options
    ]
    selected_energy_conversion = st.selectbox("Select Energy Conversion", energy_options)
    input_value = st.number_input("Enter value for conversion")
    result = energy_conversion(input_value, selected_energy_conversion)
    st.write(result)

elif selected_conversion == "Pressure":
    pressure_options = [
        "Pascals to Atmospheres",
        "Atmospheres to Pascals"
        # Add other pressure conversion options
    ]
    selected_pressure_conversion = st.selectbox("Select Pressure Conversion", pressure_options)
    input_value = st.number_input("Enter value for conversion")
    result = pressure_conversion(input_value, selected_pressure_conversion)
    st.write(result)

elif selected_conversion == "Data Size":
    data_size_options = [
        "Megabytes to Gigabytes",
        "Gigabytes to Terabytes"
        # Add other data size conversion options
    ]
    selected_data_size_conversion = st.selectbox("Select Data Size Conversion", data_size_options)
    input_value = st.number_input("Enter value for conversion")
    result = data_size_conversion(input_value, selected_data_size_conversion)
    st.write(result)

# Add similar blocks for the other conversion categories

