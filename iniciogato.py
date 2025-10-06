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
pg = st.navigation(["homepage.py", "gatos99.py" , "mantequilla.py" , "paris.py" , "quienes.py"])
pg.run()
