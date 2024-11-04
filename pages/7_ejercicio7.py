from math import exp
import time
import streamlit as st
from estilo import pg_bg_pgs

st.markdown(pg_bg_pgs,unsafe_allow_html=True)
st.title('Ejercicio 7')
'''
Dado N notas de un estudiante calcular: Cuantas
notas tiene desaprobados. Cuantos aprobados. El promedio
de todas las notas.
'''
def calcular_notas(notas):
    desaprobados = len([nota for nota in notas if nota < 11])
    aprobados = len(notas) - desaprobados
    promedio = sum(notas) / len(notas) if notas else 0
    return desaprobados, aprobados, promedio

def main():
    notas_input = st.text_area("Ingresa las notas separadas por comas (Ejemplo: 15, 8, 12, 10)")
    if st.button("Calcular"):
        try:
            notas = [float(nota.strip()) for nota in notas_input.split(",") if nota.strip()]
            desaprobados, aprobados, promedio = calcular_notas(notas)
            st.write(f"Cantidad de notas desaprobadas: {desaprobados}")
            st.write(f"Cantidad de notas aprobadas: {aprobados}")
            st.write(f"Promedio de todas las notas: {promedio:.2f}")
        
        except ValueError:
            st.error("🚨 Por favor, ingresa solo números separados por comas.")

if __name__ == "__main__":
    main()