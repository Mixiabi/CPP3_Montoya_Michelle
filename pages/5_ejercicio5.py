import time
import streamlit as st
from estilo import pg_bg_pgs

st.markdown(pg_bg_pgs, unsafe_allow_html=True)

st.title('**Ejercicio 05**')
'''
Algoritmo que pida números hasta que se introduzca un "0". 
Debido a que se imprima la suma y la media de todos los números introducidos.
'''
def calcula_lista(numero):
    if 'numeros' not in st.session_state:
        st.session_state['numeros'] = []
    
    if numero is not None:
        st.session_state['numeros'].append(numero)

def reiniciar():
    st.session_state['numeros'].clear()
    st.success('🟢 **Cálculo Reiniciado.**')

def main():
    st.header('Calcula Suma & Media de valores')
    
    nuevo_numero = st.number_input('**Ingrese valores (0 para terminar):**', value=0.0, format='%.f')

    if nuevo_numero != 0:
        calcula_lista(nuevo_numero)
        st.write(f'Lista de números ingresados: {st.session_state["numeros"]}')
    
    if st.button('**Mostrar Resultados**'):
        if st.session_state['numeros']:
            suma = sum(st.session_state['numeros'])
            media = suma / len(st.session_state['numeros'])
            st.write(f'**Suma de los números:** {suma:.2f}')
            st.write(f'**Media de los números:** {media:.2f}')
        else:
            st.warning("🚨 **No hay números para calcular**")

    if st.button('**Reiniciar**'):
        reiniciar()

if __name__ == "__main__":
    main()