import streamlit as st
import pandas as pd


st.title("Empleatronix")
st.write("Todos los datos sobre los empleados de la aplicación.")

df = pd.read_csv("./data/employees.csv")

df

st.divider()