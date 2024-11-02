import time
import streamlit as st
from estilo import pg_bg_pgs

st.markdown(pg_bg_pgs,unsafe_allow_html=True)

st.title('Ejercicio 05')
'''
Algoritmo que pida números hasta que se introduzca un
" 0 ". Debe imprimir la suma y la media de todos los números
introducidos.
'''
def calculaLista(numero):
    if 'numeros' not in st.session_state:
        st.session_state['numeros'] = []
    if not numero:

        return "🚨 **Campo no debe estar vacío**"
    try:
        st.session_state['numeros'].append(numero)
    except ValueError:
        return 'Datos no validos'

def reiniciar():
    aviso = st.info('Calculo Reiniciado ...')
    time.sleep(1.5)
    aviso.empty()
    st.session_state['numeros'].clear()

def main():
    st.header('Calcula Suma & Media de valores')
    nuevoNumero = st.number_input('**Ingrese valores:**',value=None,format='%.f')

    if nuevoNumero is None:
        error = calculaLista(nuevoNumero)
        if error:
            st.error(error)

    if st.button('**Reiniciar**',type='primary'):
            reiniciar()
            
    if nuevoNumero != 0:
        calculaLista(nuevoNumero)
        st.write(f'Lista de números ingresados: {st.session_state['numeros']}')

    else:
        if st.session_state['numeros']:
            suma = sum(st.session_state['numeros'])
            media = suma / len(st.session_state['numeros'])
            st.write(f'Lista de números ingresados: {st.session_state['numeros']}')
            st.write(f'**Suma de los números:** {suma:.2f}')
            st.write(f'**Media de los números:** {media:2f}')
        else:
            st.warning("🚨 **No hay números para calcular**")

if __name__ == "__main__":
    main()