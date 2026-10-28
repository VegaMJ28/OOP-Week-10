import streamlit as st
from PIL import Image

#create my Resume

#col1, col2 = st.columns((4,5))

#with col1:
    #st.title("Maria Jesus Vega")
    #st.header("Cybersecurity Major")

#with col2:
    #image = Image.open('coolcat1.jpeg')
    #st.image(image, width=200)


st.title("Maria Jesus Vega")
st.header("Freshman at John Brown University")

st.markdown("About Me:")
st.text("I am studying cybersecurity at John Brown University")
st.divider()

st.markdown("Qualifications")
st.text("High School Diploma")
st.divider()

st.markdown("Work Experience")
st.text("UCMAS (Elemental A&B) Tutor")
st.divider()

st.markdown("Projects")
st.text("App in progress: AXIS")
st.divider()

st.markdown("Contact me:")
st.text("email: marijesusv28@gmail.com")
st.divider()

st.markdown("**Contact me:**")
userName = st.text_input("Your Name:")
userEmailId = st.text_input("Email ID:")
userMessage = st.text_area("Your Message:")
st.button("Send Message")

st.balloons()
st.snow()
