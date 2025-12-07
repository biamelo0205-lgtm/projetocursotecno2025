import streamlit as st

st.title("🎈 Projeto-Curso 2025")
st.header("Mulheres na Ciência.",divider=True )
st.subheader("Meninas apaixonadas por tecnologia aprendendo a programar.")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.title("Título da página - Tutotial de textos")
#header
st.header("Cabeçalho do Streamlit")
st.subheader("")
st.text("blablá")
st.write("isso é só uma escrita de texto")

#markdown, uso do texto normal, mas usa #, em que a quantidade deles indica o tamanho do texto escrito
st.markdown("esse é um texto usando markdown")
# * indica itálico, dois indica negrito.
st.markdown("esté pe um tutorial, *preste atenção*")

# markdown + """ com fechamento  indica uma lista.
# link: [Vídeo lago dos cisnes] (endereço do vídeo)

#linha divisória
st.markdown ("""---""")

#emojis
st.markdown("### Emojis")
#usa o código de cada emoji
st.markdown("[Emojis](link para os emojis)")
st.markdown(":thumbsup: :heart: :books:")

st.markdown(" ### HTML")

html_code = """
    <h1 style='color: pink;'> Esse é um cabeçalho rosa </h1>
    <p style = ' color: purple;'> Esse é um parágrafo </p>


"""

st.markdown(html_code, unsafe_allow_html=True)

