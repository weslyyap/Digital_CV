# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 22:39:01 2023

@author: weihau.yap
"""
#from os.path2 import dirname, abspath
from pathlib import Path
from PIL import Image
import json
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import pandas as pd
import numpy as np
import requests

def Get_Directory():
    current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
    print(current_dir)
    css = current_dir / "styles" / "main.css"
    #css = "C:/Users/Weihau.yap/.spyder-py3/Eresume/Digital-CV/styles/main.css"
    #resume = "C:/Users/Weihau.yap/.spyder-py3/Eresume/Digital-CV/assets/resume.pdf"
    resume = current_dir / "assets" / "resume.pdf"
    #profile_pic = "C:/Users/Weihau.yap/.spyder-py3/Eresume/Digital-CV/assets/pic.png"
    profile_pic = current_dir / "assets" / "pic.png"
    return css, resume, profile_pic
    
def Load_Assets(css, resume, profile_pic):
    # --- LOAD CSS, PDF & PROFIL PIC ---
    print(css)
    print(resume)
    print(profile_pic)
    with open(css) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
    with open(resume, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    profile_pic = Image.open(profile_pic)
    return PDFbyte, profile_pic
    
def Setup():
        # --- GENERAL SETTINGS ---
    PAGE_TITLE = "Digital CV | Yap Wei Hau"
    PAGE_ICON = ":wave:"
    NAME = "Yap Wei Hau"
    DESCRIPTION = """
    RnD Engineer, understanding new products by gaining actionable insights through data.
    """
    EMAIL = "1weslyyap1@gmail.com"
    SOCIAL_MEDIA = {
        "LinkedIn": "https://linkedin.com/in/wei-hau-yap",
        "GitHub": "https://github.com/weslyyap",
    }
    PROJECTS = {
        "🏆 Wine Cultivars Class Classifier Model - Cloud Deployment on Render": "https://wine-machine-learning-streamlit-app.onrender.com", #"https://github.com/weslyyap/Wine_MachineLearning-DataScience",
        "🏆 Optical Character Recognition using Neutal Networks - Machine Learning in .NET Framework (C#)": "https://youtu.be/3egaMfE9388",
        #"🏆 Security Analysis and Construction of Confidence Bits on a Secured Iris Recognition System - Final Year Project": " ",
    }

    return PAGE_TITLE, PAGE_ICON, NAME, DESCRIPTION, EMAIL, SOCIAL_MEDIA, PROJECTS

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    
#Set up front end
#Webpage config
PAGE_TITLE = "Digital CV | Yap Wei Hau"
PAGE_ICON = ":wave:"

st.set_page_config(page_title = PAGE_TITLE, page_icon = PAGE_ICON, layout = "wide")
css, resume, profile_pic = Get_Directory()
PDFbyte, profile_pic = Load_Assets(css, resume, profile_pic)
PAGE_TITLE, PAGE_ICON, NAME, DESCRIPTION, EMAIL, SOCIAL_MEDIA, PROJECTS = Setup()
st.title("Get To Know Me!")
st.write("---")

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label = " 📄 Download Resume",
        data = PDFbyte,
        file_name = resume,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 2 Years expereince collecting and extracting useful insights from data
- ✔️ Fast learner that like to apply learnt knowledge and buid it on something new
- ✔️ Eager to remove and automate labour work
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas, Numpy), SQL, C# 
- 📊 Data Visulization: Matplotlib, Seaborn, Plotly
- 📚 Modeling: Logistic Regression, Linear Regression, Decision Trees
- 🗄️ Database: MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**RnD Engineer | Akribis Systems Pte Ltd**")
st.write("03/2022 - Present")
st.write(
    """
- ► Developed C# PC based apps for precision measurement data acquisition that automated the process and reduced the total cycle time by 50%
- ► Data manipulation (Numpy and Pandas) and data cleaning of all test data sets before built MySQL local database
- ► Built the data pipeline to present the test data results on 3rd party Cloud Platform, Tulip subscirbed by company
- ► GitHub implementation version control
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**LabVIEW Programmer | Fuji Master Engineering Sdn. Bhd.**")
st.write("06/2020 - 02/2022")
st.write(
    """
- ► Built NI LabVIEW application for production and manufacturing line with real time data logging feature based on customers' requirements
- ► Data cleaning for test data sets before store in MySQL local database
- ► Python OpenCV for in house Vision System Development
"""
)

# --- JOB 3
# st.write('\n')
# st.write("🚧", "**Data Analyst | Chegg**")
# st.write("04/2015 - 01/2018")
# st.write(
#     """
# - ► Devised KPIs using SQL across company website in collaboration with cross-functional teams to achieve a 120% jump in organic traﬃc
# - ► Analyzed, documented, and reported user survey results to improve customer communication processes by 18%
# - ► Collaborated with analyst team to oversee end-to-end process surrounding customers' return data
# """
# )


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
st.write("🏆 Security Analysis and Construction of Confidence Bits on a Secured Iris Recognition System - Final Year Project")