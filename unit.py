import streamlit as st

# Unit conversion functions

# Length conversions
def convert_length(value, from_unit, to_unit):
    length_units = {
        'meters': 1,
        'kilometers': 0.001,
        'centimeters': 100,
        'millimeters': 1000,
        'inches': 39.3701,
        'feet': 3.28084,
        'yards': 1.09361
    }
    return value * length_units[to_unit] / length_units[from_unit]

# Weight conversions
def convert_weight(value, from_unit, to_unit):
    weight_units = {
        'kilograms': 1,
        'grams': 1000,
        'milligrams': 1000000,
        'pounds': 2.20462,
        'ounces': 35.274
    }
    return value * weight_units[to_unit] / weight_units[from_unit]

# Temperature conversions
def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'Celsius' and to_unit == 'Fahrenheit':
        return (value * 9/5) + 32
    elif from_unit == 'Celsius' and to_unit == 'Kelvin':
        return value + 273.15
    elif from_unit == 'Fahrenheit' and to_unit == 'Celsius':
        return (value - 32) * 5/9
    elif from_unit == 'Fahrenheit' and to_unit == 'Kelvin':
        return (value - 32) * 5/9 + 273.15
    elif from_unit == 'Kelvin' and to_unit == 'Celsius':
        return value - 273.15
    elif from_unit == 'Kelvin' and to_unit == 'Fahrenheit':
        return (value - 273.15) * 9/5 + 32
    return value  # In case of the same units

# Injecting custom CSS for styling the app
def apply_custom_css():
    custom_css = """
    <style>
    body {
        background-color: #f4f4f9;
        color: #333;
    }
    .stButton>button {
        background-color: #0073e6;
        color: white;
        font-size: 16px;
        border-radius: 5px;
        padding: 10px;
    }
    .stButton>button:hover {
        background-color: #005bb5;
    }
    .css-1d391kg {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stSidebar {
        background-color: #2a2a2a;
        color: white;
        padding: 20px;
    }
    .stTextInput>div>input {
        background-color: #e0e0e0;
        border: 1px solid #ccc;
        padding: 10px;
        border-radius: 4px;
    }
    .stTextInput>div>input:focus {
        border-color: #0073e6;
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

# Streamlit app layout
def app():
    apply_custom_css()  # Apply custom CSS

    st.title("Unit Converter By Syed Ahmed Hassa")
    st.subheader("Convert between different units of measurement.Creating the project of Quarter 3!")

    # Sidebar for selecting categories
    category = st.sidebar.selectbox("Select Conversion Category", ["Length", "Weight", "Temperature"])

    # Input fields for the user
    value = st.number_input("Enter value to convert", min_value=0.0, step=0.1)

    # Conversion logic for each category
    if category == "Length":
        from_unit = st.selectbox("From Unit", ['meters', 'kilometers', 'centimeters', 'millimeters', 'inches', 'feet', 'yards'])
        to_unit = st.selectbox("To Unit", ['meters', 'kilometers', 'centimeters', 'millimeters', 'inches', 'feet', 'yards'])
        result = convert_length(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} is equal to {result} {to_unit}")

    elif category == "Weight":
        from_unit = st.selectbox("From Unit", ['kilograms', 'grams', 'milligrams', 'pounds', 'ounces'])
        to_unit = st.selectbox("To Unit", ['kilograms', 'grams', 'milligrams', 'pounds', 'ounces'])
        result = convert_weight(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} is equal to {result} {to_unit}")

    elif category == "Temperature":
        from_unit = st.selectbox("From Unit", ['Celsius', 'Fahrenheit', 'Kelvin'])
        to_unit = st.selectbox("To Unit", ['Celsius', 'Fahrenheit', 'Kelvin'])
        result = convert_temperature(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} is equal to {result} {to_unit}")

if __name__ == "__main__":
    app()
