import streamlit as st
import time
from PIL import Image



st.title("Machine Learning Model Deployment at the server!")

# header
st.header("Introduction: This is a heading")

# subheading
st.subheader("This is a Subheader")

# text data
st.text("This is text")

# read input from the user
input_text = st.text_input("Type something", "type here...")
st.text(input_text)

input_text = st.text_area("Enter here", "this is large text area")

## markdown
st.markdown("This text is __really important__")
st.markdown("###### This is heading")
st.markdown("""
            1. First
            2. Second
            3. Third
            """)

# Button
button = st.button("Click Me")
if button:
    st.text("I am clicked!")
    st.info("I am clicked!!! Snap me fast!!!")
    st.toast("I am going to disappear")
    st.warning("This warning")
    st.error("This is error")



# Image 
st.image("https://mms.businesswire.com/media/20200616005364/en/798639/23/Streamlit_Logo_%281%29.jpg", width=100, )

# Check box
flag = st.checkbox("Select me")
st.write(flag)

if flag:
    img = Image.open("./foto_linkedin.png")
    st.image(img)


# radio button
selection = st.radio("Choose your model", ['NLP', 'Image', 'Audio'])
st.write(selection)

# select box
selection = st.selectbox("Choose your model", ["NLP", "Image", "Audio"])
st.write(selection)

# Multi select 
selection = st.multiselect("Choose your model", ["NLP", "Image", "Audio"])
st.write(selection)

# Loading spinner
with st.spinner("Downloading... Please wait!"):
    st.write("downloading the model here")
    time.sleep(10)
    
st.subheader("Model downloaded")

# select numerical value from the given list
slider = st.slider("Set Threshold", 0.0, 1.0, step=0.01)
st.write(slider)

