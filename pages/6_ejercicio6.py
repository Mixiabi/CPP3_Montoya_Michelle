from numpy import empty
import streamlit as st
import time
from estilo import pg_bg_pgs

st.markdown(pg_bg_pgs, unsafe_allow_html=True)
st.title('Ejercicio 6')
'''
**Dado N calcular: (1^1) + (2^2) + (3^3) + ... + (N^N)**
'''
def calcular(n):
    """Calcula la suma de i^i desde 1 hasta n."""
    if not n or  n == '':
        return '🚨 **El campo no puede estar vacío**'
    
    try:
        n = int(n)
        suma = 0
        for i in range(1, n + 1):
            suma += i ** i
        return suma
    except ValueError:
        return '🚨 **Ingrese un valor válido**'


def main():
    # Inicializar el estado de 'numero' y 'respuesta' en session_state
    if 'numero' not in st.session_state:
        st.session_state['numero'] = ''
    if 'respuesta' not in st.session_state:
        st.session_state['respuesta'] = None

    numero = st.text_input('Ingresa un número', st.session_state['numero'])

    if st.button('Calcular'):
        respuesta = calcular(numero)
        st.session_state['respuesta'] = respuesta
        st.session_state['numero'] = numero

    if st.session_state['respuesta'] is not None:
        if isinstance(st.session_state['respuesta'], str):
            st.error(st.session_state['respuesta'])
        else:
            st.write(f'Resultado: {st.session_state["respuesta"]:.2f}')


    if st.button('Reiniciar'):
        st.session_state['numero'] = ''
        st.session_state['respuesta'] = None
        st.experimental_rerun()


if __name__ == "__main__":
    main()
