pg_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: linear-gradient(rgba(255, 255, 255, 0.9), rgba(255, 255, 255, 0.5)), 
                      url('https://icontinental.edu.pe/wp-content/uploads/2023/05/logo-instituto-continental.png');
    background-size: auto;
    background-position: center;
    background-repeat: no-repeat;
    # height: 100vh; /* Ajusta la altura como necesites */
    # width: 100vw;  /* Ajusta el ancho como necesites */
    margin: auto; /* Centra el contenedor */
}
[data-testid="stSidebar"] {
    background : transparent;
}
[data-testid="stSidebarContent"] {
    # background : white;
    color: black; 
}
[data-testid="stSidebarHeader"]::before {
    content: "MENU PRINCIPAL";
    font-weight: bold;
    font-size: 22px;
    color: black;
}
[data-testid="stSidebarNavItems"] {
    font-weight: bold;
    font-size: 22px;
    color: black;
}
<style>
"""