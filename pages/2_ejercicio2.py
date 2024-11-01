import streamlit as st
import time

st.title('👈 MENU PRINCIPAL')
st.header('Ejercicio 02')
'''
Crear un Array que almacene los valores múltiplos de X entre 0 y 100. Retornar la cantidad de datos que se almacenaron. Retornar la sumatoria de los datos del array.
'''


def multiplos(numX):
    if numX == 0:
        return 'El numero tiene que ser diferente de " 0 "'
    if 'valores' not in st.session_state: 
        st.session_state['valores'] = [] 
    return None

def main(): 
    st.header('Múltiplos de "x"')
    numX = st.number_input("Ingresa un número:",value = None,format='%.f')
    
    if st.button("Calcular", type='primary',use_container_width=True):
        error = multiplos(numX)
        if error:
            st.error(error)
        else:
            st.session_state['valores'].clear()
            for i in range(0, 101):
                if i % numX == 0:
                    st.session_state['valores'].append(i)

            primerMensaje = st.success('Datos agregados correctamente')
            time.sleep(2)
            primerMensaje.empty()
            
            sumatoria = sum(st.session_state['valores'])
            cantidad = len(st.session_state['valores'])
            
            st.write(f'**LISTA DE DATOS:** {st.session_state["valores"]}')
            st.write(f'**TOTAL DE DATOS:** {cantidad}')
            st.write(f'**SUMATORIA DE DATOS:** {sumatoria}')

    if st.button("Limpiar", type='secondary',use_container_width=True):
        st.session_state['valores'].clear()
        segundoMensaje = st.info("La lista ha sido limpiada")
        time.sleep(1)
        segundoMensaje.empty()

if __name__ == "__main__":
    main()