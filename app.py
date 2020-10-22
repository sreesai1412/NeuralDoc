import streamlit as st
import os
import time
import re

def preprocess(message):
    return message.translate({ord(c): None for c in '.,\'\":;)(!\n\t'})

def predict(message):
    #os.system("cd scripts")
    f = open("./data/python/sample.code", "w")
    f.write(message)
    f.close()
    print("Wrote code to file" + message)
    os.system("bash ./scripts/generate.sh -1 code2jdoc sample.code")
    # time.sleep(10)
    f = open("pred.txt", "r")
    doc = f.read()
    f.close()
    return doc


st.title("AutoDoc")
st.subheader("NITK, Surathkal")
st.header("CS305 Software Engineering Mini Project")
st.subheader("Sai Sree Harsha (181CO146) & Aditya Sohoni (181CO203)")
st.title("Automating Code Documentation using Machine Learning")
message = st.text_area("Enter Code Below", height=350)
message = preprocess(message)
if st.button("Analyze"):
    with st.spinner("Analyzing the text …"):
        prediction = predict(message)
        st.success(prediction)
