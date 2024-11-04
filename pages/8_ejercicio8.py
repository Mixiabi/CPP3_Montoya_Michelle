import streamlit as st
from estilo import pg_bg_pgs

st.markdown(pg_bg_pgs, unsafe_allow_html=True)
st.title('**Ejercicio 8**')
'''
Crea un array de 10 posiciones de números con valores pedidos por teclado. 
Muestra por consola el índice y el valor al que corresponde. Mostrar al final la sumatoria.
'''

def obtener_numeros(input_text):
    try:
        numeros = [float(num.strip()) for num in input_text.split(',')]
        return numeros
    except ValueError:
        st.error('🚨 **Ingrese solo números válidos separados por comas.**')
        return []

def calcular_suma(numeros):
    return sum(numeros)

def main():
    st.write("Ingrese exactamente 10 números separados por comas:")
    if 'numeros' not in st.session_state:
        st.session_state.numeros = []

    input_text = st.text_input('Números:', value=', '.join(map(str, st.session_state.numeros)))

    if st.button('Mostrar Resultados', key='mostrar_resultados'):
        st.session_state.numeros = obtener_numeros(input_text)

        if len(st.session_state.numeros) != 10:
            st.error('🚨 **Por favor, ingrese exactamente 10 números.**')
        else:
            st.write("Índices y valores correspondientes:")
            for index, valor in enumerate(st.session_state.numeros):
                st.write(f'Índice {index}: Valor {valor}')
            suma_total = calcular_suma(st.session_state.numeros)
            st.write(f'Suma total: {suma_total}')

    if st.button('Reiniciar', key='reiniciar'):
        st.session_state.numeros = []

# Llamar a la función main una sola vez al inicio
if __name__ == "__main__":
    main()
