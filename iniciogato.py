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
    st.page_link("iniciogato.py", label="Inicio", icon=":material/home:")
    st.page_link("pages/1_mantequilla.py", label="matequilla", icon=":material/density_small:")
    st.page_link("pages/5_homepage.py", label="home", icon=":material/density_small:")
    st.page_link("pages/2_paris.py", label="mantequilla", icon=":material/assistant_navigation:")
    st.page_link("pages/3_quienes.py", label="quienes", icon=":material/group_search:")
    st.page_link("pages/4_gatos99.py", label="gato", icon=":material/mobile:")





