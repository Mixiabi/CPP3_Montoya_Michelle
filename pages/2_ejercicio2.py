from code import interact
import os
from numpy import integer
import streamlit as st
from tenacity import retry_never

st.title('Ejercicio 02')
'''
Crear un Array que almacene los valores múltiplos de X
entre 0 y 100. Retornar la cantidad de datos que se almacenaron.
Retornar la sumatoria de los datos del array.
'''
# '''
# Que realice los diferentes métodos de ordenación de arrays utilizando las funciones:\n
# ✨ Relleno de un array.\n
# ✨ Copia un array a otro.\n
# ✨ Mostrar en pantalla todos los valores.\n
# ✨ Ordenar por burbuja.\n
# '''
def metodo_array():
    st.session_state
    return None

def main():
    st.header('Múltiplos de "x"')
    
    num = st.text_input("Ingresa un número:")
    
    if num:
        
        try:
            numero_entero = int(num)
            
            st.write(f"Número ingresado: {numero_entero}")
            
        except ValueError:
            
            st.error("Por favor, ingresa un número válido.")
            
    else:
        
        st.warning("El campo no puede estar vacío.")

if __name__ == "__main__":
    main()