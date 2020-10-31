import streamlit as st
import os
import time
import re


def preprocess(message):
    return message.translate({ord(c): None for c in '.,\'\":;)(!\n\t'})


def _max_width_():
    max_width_str = f"max-width: 1300px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>
    """,
        unsafe_allow_html=True,
    )


def predict_python(message):
    #os.system("cd scripts")
    f = open("./data/python/sample.code", "w")
    f.write(message)
    f.close()
    print("Wrote code to file" + message)
    os.system("bash ./scripts/generate_python.sh -1 python2doc sample.code")
    # time.sleep(10)
    f = open("pred.txt", "r")
    doc = f.read()
    f.close()
    return doc


def predict_java(message):
    #os.system("cd scripts")
    f = open("./data/java/sample.code", "w")
    f.write(message)
    f.close()
    print("Wrote code to file" + message)
    os.system("bash ./scripts/generate_java.sh -1 java2doc sample.code")
    # time.sleep(10)
    f = open("pred.txt", "r")
    doc = f.read()
    f.close()
    return doc


_max_width_()
st.title("NeuralDoc | Automating Code Documentation using Machine Learning")
st.header("CS305 Software Engineering Mini Project, NITK, Surathkal")
st.subheader("Sai Sree Harsha (181CO146) & Aditya Sohoni (181CO203)")
#st.write("Documentation of source code is a tedious process, but nevertheless an integral part of software development. Our system, NeuralDoc automatically generates documentation for Python and Java methods at the click of a button. NeuralDoc leverages cutting edge techniques such as the Transformer and BERT to gain a deep understanding of the code and generate a high quality documentation. NeuralDoc boosts developer productivity and renders the documentation process completely painless.")

col1, col2, col3 = st.beta_columns([4, 1, 4])

with col1:
    message = st.text_area("Enter Python Code Below", height=350)
    if st.button("Analyze", key='py'):
        with st.spinner("Documenting Code, Please Wait ......."):
            prediction = predict_python(message)
            st.success(prediction)

with col3:
    message = st.text_area("Enter Java Code Below", height=350)
    if st.button("Analyze", key='java'):
        with st.spinner("Documenting Code, Please Wait ......."):
            prediction = predict_java(message)
            st.success(prediction)
