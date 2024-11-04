import random
import streamlit as st
from estilo import pg_bg_pgs

st.markdown(pg_bg_pgs, unsafe_allow_html=True)
st.title('Ejercicio 9')
'''
Crea un array de números donde le indicamos por teclado
el tamaño del array, rellenaremos el array con números entre
0 y 9, y mostraremos la media de todos los valores.
'''

def rellenar_array(tamaño):
    """Rellena el array con números aleatorios entre 0 y 9."""
    return [random.randint(0, 9) for _ in range(tamaño)]

def calcular_media(valores):
    """Calcula la media de los valores en el array."""
    if len(valores) == 0:
        return 0
    return sum(valores) / len(valores)

def main():
    tamaño_array = st.number_input('**Ingresa la dimensión del array (entre 1 y 100):**', min_value=1, max_value=100, value=10)
    if st.button('Rellenar el Array'):
        array_valores = rellenar_array(tamaño_array)
        media = calcular_media(array_valores)
        st.write(f'Array generado: {array_valores}')
        st.write(f'Media de los valores: {media:.2f}')
    if st.button('Reiniciar'):
        st.session_state.clear()
        st.success('La calculadora ha sido reiniciada. Ingresa un nuevo tamaño del array.')

if __name__ == "__main__":
    main()
