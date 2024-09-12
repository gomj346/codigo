import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Funciones de señales continuas
def señal_continua_1(t):
    return 2 - np.abs(t)

def señal_continua_2(t):
    return np.piecewise(t, [t < -2, (t >= -2) & (t < 1), (t >= 1) & (t < 3), t >= 3],
                        [0, lambda t: 2, lambda t: 1 - t, 0])

# Secuencias discretas
def secuencia_discreta_1():
    return np.array([0, 0, 0, 0, 0, -3, 0, 5, 4, -2, -4, -1, 2, 5, 7, 4, -2, 0, 0, 0, 0])

def secuencia_discreta_2():
    n = np.arange(-10, 11)
    x = np.zeros_like(n, dtype=float)
    x[(n >= -5) & (n <= 0)] = (2/3)**n[(n >= -5) & (n <= 0)]
    x[(n >= 1) & (n <= 5)] = (8/5)**n[(n >= 1) & (n <= 5)]
    return n, x

# Configuración de Streamlit
st.title("Laboratorio: Transformación de Señales")
st.write("Generación de señales continuas y discretas")

# Menú de selección de señal
tipo_señal = st.selectbox("Selecciona el tipo de señal", ["Continua 1", "Continua 2", "Discreta 1", "Discreta 2"])

# Generar señales y graficar
if tipo_señal == "Continua 1":
    t = np.linspace(-10, 10, 400)
    y = señal_continua_1(t)
    plt.plot(t, y)
    plt.title("Señal Continua 1")
    plt.xlabel("t")
    plt.ylabel("x(t)")
    st.pyplot(plt.gcf())
    plt.clf()

elif tipo_señal == "Continua 2":
    t = np.linspace(-10, 10, 400)
    y = señal_continua_2(t)
    plt.plot(t, y)
    plt.title("Señal Continua 2")
    plt.xlabel("t")
    plt.ylabel("x(t)")
    st.pyplot(plt.gcf())
    plt.clf()

elif tipo_señal == "Discreta 1":
    n = np.arange(-10, 11)
    x = secuencia_discreta_1()
    plt.stem(n, x, use_line_collection=True)
    plt.title("Secuencia Discreta 1")
    plt.xlabel("n")
    plt.ylabel("x[n]")
    st.pyplot(plt.gcf())
    plt.clf()

elif tipo_señal == "Discreta 2":
    n, x = secuencia_discreta_2()
    plt.stem(n, x, use_line_collection=True)
    plt.title("Secuencia Discreta 2")
    plt.xlabel("n")
    plt.ylabel("x[n]")
    st.pyplot(plt.gcf())
    plt.clf()

