import streamlit as st
import webbrowser
st.sidebar.image("https://www.linkpicture.com/q/WhatsApp-Image-2020-07-10-at-1.21.58-AM.jpeg", caption=None, width=150, use_column_width=False, clamp=False, channels='RGB', format='JPEG')
st.sidebar.title("Suryansh Jain")
st.sidebar.markdown("Pick a section :")

sections=["About me","Work Experience","Projects","Extra-curricullar"]
picked=st.sidebar.radio("Pick a section",sections)
#streamlit.image("", caption=None, width=None, use_column_width=False, clamp=False, channels='RGB', format='JPEG')'''
if picked=="About me":
    st.title("**_About me_**")
    aboutmeSubSection=["Personal info","Education","Skills","Certifications"]
    subsection=st.radio("Pick a subsection",aboutmeSubSection)
    if subsection=="Personal info":
        st.subheader("**_Suryansh Jain_**")
        st.markdown("**_Email_** - suryanshjain531@gmail.com")
        st.markdown("**_Phone_** - 7574922552")
        st.markdown("**_LinkedIn_** - https://www.linkedin.com/in/suryansh-jain-b10a2117b/")
    if subsection=="Education":
        st.subheader("**_Education_**")
        st.success("1. B.Tech Electronics and Communication Engineering - VIT University, Vellore")
        st.info("**_CGPA - 8.83_**")
        st.success("2. Senior Secondary - St. Ann's School, Ahmedabad")
        st.info("**_Percentage - 85.4_**")
        st.success("3. Higher Secondary Secondary - Delhi International School, Indore")
        st.info("**_CGPA - 10_**")
    elif subsection=="Skills":
        st.info("Python")
        st.info("SAS")
        st.info("SQL")
        st.info("Data Ananlysis and Visualization")
        st.info("Git & Github")
        st.info("Regex")
    elif subsection=="Certifications":
        st.info("Professional Certificate - SAS Visual Business Analytics")
        st.text("offered by SAS through Coursera")
        st.image("https://www.linkpicture.com/q/Coursera-UHPFH9DXH6KP_page-0001.jpg", caption=None, width=500, use_column_width=False, clamp=False, channels='RGB', format='JPEG')
        st.info("Specialization - Introduction to Scripting in Python")
        st.text("offered by Rice University through Coursera")
        st.image("https://www.linkpicture.com/q/Coursera-SPFP46VVHCE8_page-0001.jpg", caption=None, width=500, use_column_width=False, clamp=False, channels='RGB', format='JPEG')
        st.info("Course - Using Python to Interact with the Operating System")
        st.text("offered by Google through Coursera")
        st.image("https://www.linkpicture.com/q/Coursera-LZ3SLBZLF6RE_page-0001.jpg", caption=None, width=500, use_column_width=False, clamp=False, channels='RGB', format='JPEG')
elif picked=="Work Experience":
    st.title("**_Work Experience_**")
    st.success("Summer Intern - Bharti Airtel Ltd.")
    st.success(" May'18 - Jun'18")
    st.info("Worked as a part of network management team.")
    st.info("Analyzed data and generated insights from sites across the city to identify poor network coverage.")
    st.image("https://www.linkpicture.com/q/WhatsApp-Image-2020-07-10-at-2.14.54-AM.jpeg", caption="Developed a GUI using VBA in Excel", width=500, use_column_width=False, clamp=False, channels='RGB', format='JPEG')
    st.image("https://www.linkpicture.com/q/WhatsApp-Image-2020-07-10-at-2.17.33-AM.jpeg", caption="Certificate", width=500, use_column_width=False, clamp=False, channels='RGB', format='JPEG')
elif picked=="Projects":
    st.title("**_Projects_**")
    st.subheader("**_1. Advanced Path Finding Algorithm - Python_**")
    st.info("Implemented A * algorithm to calculate shortest path between any two given points that works in practice 1000s (up to 25000) of times faster than the classical Dijkstra's algorithm on real-world road networks.")
    st.subheader("**_2. Covid19 Data Analysis - Python_**")
    st.markdown("https://covid-19-s.herokuapp.com/")
    st.info("Developed an interactive webpage to view plots of the number of Covid19 cases in India. Added controls to view state-wise data.")
    st.subheader("**_3. Ball Beam Balance - Arduino_**")
    st.info("Built a PID control system that could effectively balance a ball on a metal beam using a motor input to control the angle of the beam")
    st.subheader("**_4. Card reading trick - Python_**")
    st.info("Implemented an algorithm to encode 4 out of the 5 cards picked by the player so as to guess the fifth card.")
    st.subheader("**_5. Hand Gesture Controlled Robot - Arduino_**")
    st.info("Created a robot in the form of a wheelchair which works through inputs provided with the movement of arm of differently-abled people.")
elif picked=="Extra-curricullar":
    st.subheader("**_Positions of responsibility_**")
    st.markdown("**_Co-founder_**")
    st.markdown("The Comedy Club, VIT")
    st.subheader("**_Interests_**")
    st.markdown("Formula 1, Tech Reviews, Improv Comedy")
    st.subheader("**_Languages_**")
    st.markdown("English & Hindi - Full working proficiency.")
    st.markdown("Chinese, French & Japanese - Elementary proficiency")
else:
    st.markdown("**_hey there_**")
    ""
    "please pick a section from the sidebar to see more"
