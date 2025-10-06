 #Importar streamlit
import streamlit as st

# ---------------------  Contenido del sitio   --------------------------#
# Sección Inicial
st.title("quienes somos")
st.badge("grupo", color="yellow", icon=":material/chevron_right:")

# Sutítulo
st.header("", divider=True)
#imagen
st.image("gato5.jpg", caption="mi inspiración")
#escritura
st.write("""¡Una idea fantástica! Aquí tienes una historia corta y tierna sobre un extraterrestre y su inusual amor por los gatos terrestres.

El Coleccionista de Ronroneos
Mi nombre, en mi planeta natal de Xylos-7, se traduce más o menos como "El Observador Silencioso de Nebulosas". Pero aquí, en la Tierra, simplemente me llamo Zylar. Vine para estudiar, para analizar la forma de vida dominante y preparar el primer contacto... hasta que conocí a un gato.

Mi nave, camuflada como un cobertizo de jardín suburbano, era el centro de mis operaciones. Mis herramientas analizaban la complejidad de la política global, el arte moderno y la densidad del aire. Pero mi mayor fascinación, de lejos, se convirtió en los felinos domésticos.

En Xylos-7, nuestra forma de vida es cristalina y lógica; todo es simetría y eficiencia. El concepto de una criatura que duerme dieciséis horas al día, ignora las leyes de la gravedad en las cortinas y exige afecto solo en sus términos era, para mí, una deliciosa anomalía estadística.

Mi primer sujeto de estudio, y el que me arruinó la misión (para bien), fue un gato atigrado callejero al que la vecina llamaba "Rayo".

Una tarde, Rayo se coló en mi módulo de observación. Yo estaba midiendo las micro-vibraciones de un cepillo de dientes eléctrico cuando Rayo saltó a la mesa, empujó el dispositivo y se acostó sobre el panel de control.""")