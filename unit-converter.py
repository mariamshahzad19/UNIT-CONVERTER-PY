import streamlit as st

st.title("Unit Converter App")
st.markdown("### Converts  Length, Weight, And Time Instantly")
st.write("Welcome! Select a category, enter a value, and get the converted result in real-time")

Category = st.selectbox("Chose a category", ["Length", "Weight", "Time"])

def convert_units(category, value ,unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371
        
        elif category == "Weight":
            if unit == "Kilograms to pounds":
                return value * 2.20462
            elif unit == "Pounds to kilograms":
                return value / 2.20462
            elif category == "Time":
                if unit == "Seconds to minutes":
                    return value / 60
                elif unit == "Minutes to seconds":
                    return value * 60
                elif unit == "Minutes to hours":
                    return value / 60
                elif unit == "Hours to minutes":
                    return value * 60
                elif unit == "Hours to days":
                    return value / 24 
                elif unit == "Days to hours":
                    return value *24
                
if Category == "Length":
    unit =st.selectbox("Slect Conversation",["Miles to Kilometers","Kilometers to Miles",])
elif Category == "Weight":
    unit =st.selectbox("Slect Conversation",["Kilograms to pounds","Pounds to kilgrams"])

elif Category == "Time":
    unit =st.selectbox("Slect Conversation",["seconds to minutes","Minutes to seconds" ,"Minutes to hours","Hours to minutes"])

value = st.number_input("Enter the value to convert")

if st.button("Convert"):
             
    result = convert_units(Category,value,unit)
    st.success("The result is {result:2f}")
