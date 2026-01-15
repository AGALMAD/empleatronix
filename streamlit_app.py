import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title("Empleatronix")
st.write("Todos los datos sobre los empleados de la aplicación.")

#Muestra la tabla con los datos de los empleados
df = pd.read_csv("./data/employees.csv")
df

st.divider()

# Filtros para el aspecto visual del diagrama en una misma columna
col1, col2, col3 = st.columns(3)

color = col1.color_picker(
    "Elige un color para las barras",
    "#123bc2")

show_names = col2.toggle(
    "Mostrar el nombre",
    value=True)

show_salary = col3.toggle(
    "Mostrar el sueldo en la barra",
    value=False)


# Diagrama de barras del sueldo de los empleados
fig, ax = plt.subplots(figsize=(8, 6))
ax.barh(df["full name"], df["salary"], color=color)
ax.margins(x=0.1, y=0.05)

if not show_names:
    ax.set_yticks([])

if show_salary:
    for i, salary in enumerate(df["salary"]):
        ax.text(
            salary + 50,
            i,
            f"{salary} €",
            va="center",
            fontsize=10
        )


st.pyplot(fig)

# Footer
st.caption("© Alejandro Gálvez Madueño - CPIFP Alan Turing")
