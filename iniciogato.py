# Importar streamlit
import streamlit as st

# Configurar la pagina
st.set_page_config(
    page_title="Gatitos",
    page_icon=":no_entry:", # Usar el comando python -m rich.emoji para ver lista de emojis
    layout="centered",
)

# Configuración de Logo
st.logo(
    "logogato1.jpeg",
)
#para iniciar las paginas
#pg = st.navigation(["homepage.py", "gatos99.py" , "mantequilla.py" , "paris.py" , "quienes.py"])
#pg.run()

    # Links de navegación
    st.page_link("home.py", label="Inicio", icon=":material/home:")
    st.page_link("pages/1_productos.py", label="Productos", icon=":material/density_small:")
    st.page_link("pages/2_servicios.py", label="Servicios", icon=":material/assistant_navigation:")
    st.page_link("pages/3_nosotros.py", label="Nosotros", icon=":material/group_search:")
    st.page_link("pages/4_contacto.py", label="Contacto", icon=":material/mobile:")
