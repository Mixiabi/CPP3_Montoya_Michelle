import os
import streamlit as st

st.title('Ejercicio 01')
'''
Crea un programa que pida al usuario una contraseña, de forma repetitiva mientras que no introduzca “asdasd”. Cuando finalmente escriba la contraseña correcta, se le dirá “Bienvenido” y terminará elprograma.
'''
def get_password(usuario,contra):
    
    if not usuario or not contra:
            return "El usuario y contraseña no deben estar vacios"
    while True: 
            
        if contra == "asdasd":
            break
        
        else:
            return "Contraseña incorrecta. vuelva a intentarlo"

    
def main():
    st.header('Inicio de Sesion')
    
    usuario = st.text_input("**Usuario**")
    
    contra = st.text_input("**Contraseña**", type='password')

    if st.button('Iniciar Sesion',type='primary'):
        error = get_password(usuario, contra)
        if error:
            st.error(error)
        else:
            st.success("Bienvenid@") 

if __name__ == "__main__":
    main()
    