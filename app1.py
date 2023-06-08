import streamlit as st
import pickle
import numpy as np


# Import The 
pipe = pickle.load(open("pipe.pkl","rb"))
df = pickle.load(open("df.pkl","rb"))

st.title("Mayank Laptop Price Predictor")

# brand
Company = st.selectbox("Brand",df["Company"].unique())

# Type of Laptop
type = st.selectbox("Type",df["TypeName"].unique())

# Ram
ram = st.selectbox("Ram(in GB)",[2,4,6,8,12,16,24,32])

# Weight
weight = st.number_input("Weight Of the Laptop")

# Touch Screen
touchscreen = st.selectbox("Touchscreen",["No","Yes"])

# IPS
ips = st.selectbox("IPS",["NO","Yes"])

#  screen size
screen_size = st.number_input("Screen Size")

# Resolution
resolution = st.selectbox("Screen resolution",["1920x1080","1366x768",
"1600x900","3840x2160","3200x1800","2880x1800","2560x1600","2560x1440",
 "2340x1440"])

# Cpu
cpu = st.selectbox("Brand",df["Cpu Brand"].unique())

# hdd
hdd = st.selectbox("HDD(in GB)",[0,128,256,512,1824,2848])

ssd = st.selectbox("SSD(in GB)",[0,8,128,256,512,1824,2848])

gpu = st.selectbox("GPU",df["Gpu Brand"].unique())

os = st.selectbox("OS",df["Os"].unique())

if st.button("Predict Price"):
    ppi = None
    if touchscreen == "Yes":
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == "Yes":
        ips = 1
    else:
        ips = 0

    X_res  = int(resolution.split('x')[0])
    Y_res = int(resolution.split("x")[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5/screen_size

    query = np.array([Company,type,ram,weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu,os])

    query = query.reshape(1,12)
    st.title("THe predicted price of this configuration is "+str(int(np.exp(pipe.predict(query))[0])))