import streamlit as st
from estilo import pg_bg_pgs

st.markdown(pg_bg_pgs,unsafe_allow_html=True)

st.header('Ejercicio 03')
'''
**Que realice los diferentes métodos de ordenación de arrays utilizando las funciones:**\n
✨ **Relleno de un array.**\n
✨ **Copia un array a otro.**\n
✨ **Mostrar en pantalla todos los valores.**\n
✨ **Ordenar por burbuja.**\n
'''
import streamlit as st
import time

def rellenar_array(valores_texto):
    try:
        array = [float(valor) for valor in valores_texto.split()]
        return array
    except ValueError:
        st.error('🚨 **Ingrese solo números válidos.**')
        return []

def copiar_array(array_original):
    return array_original.copy()

def mostrar_valores(array):
    for index, valor in enumerate(array):
        st.write(f'Índice {index}: Valor {valor}')

def ordenar_burbuja(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

def main():
    st.title('Ejercicio 03: Ordenación de Arrays')

    if 'array' not in st.session_state:
        st.session_state.array = []
    valores_texto = st.text_input('Ingrese valores separados por espacios para rellenar el array:')
    
    if st.button('Rellenar Array'):
        st.session_state.array = rellenar_array(valores_texto)

    if st.button('Copiar Array'):
        if st.session_state.array:
            copia = copiar_array(st.session_state.array)
            mensaje = st.empty()
            mensaje.success("Array copiado con éxito.")
            time.sleep(1)
            mensaje.empty()
        else:
            st.error('🚨 **El array está vacío. Rellene primero el array.**')

    if st.button('Mostrar Valores'):
        if st.session_state.array:
            st.write("Valores en el array:")
            mostrar_valores(st.session_state.array)
        else:
            st.error('🚨 **El array está vacío. Rellene primero el array.**')

    if st.button('Ordenar por Burbuja'):
        if st.session_state.array:
            st.session_state.array = ordenar_burbuja(st.session_state.array)
            st.write("Array ordenado por el método de burbuja:")
            mostrar_valores(st.session_state.array)
        else:
            st.error('🚨 **El array está vacío. Rellene primero el array.**')

    if 'copia' in st.session_state:
        st.write("Array Copiado:")
        mostrar_valores(st.session_state.copia)

if __name__ == "__main__":
    main()
