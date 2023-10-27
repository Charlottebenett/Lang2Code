import streamlit as st
import openai
import sys
from io import StringIO
# Configuration de la clé d'API OpenAI
openai.api_key = "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"

# Fonction pour générer du code Python
def test_openai_api(prompt_human: str):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Sans explication hors code, sans commentaire, traduire le texte suivant en code Python : {prompt_human}"}
        ],
        temperature=0.4,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response['choices'][0]['message']['content']

# Interface Streamlit
st.title("Assistant de génération de code Python ma petite :chicken: ")

# Zone de texte pour l'entrée de l'utilisateur
user_input = st.text_area("Entrez une description pour créer du code Python :")

if st.button("Exécuter"):
    if user_input:
        generated_code = test_openai_api(user_input)  # Utilisez la fonction test_openai_api pour générer le code
        st.code(generated_code, language="python")

st.title("Colle le code généré ma petite puce :sheep: ")

#Zone de texte pour saisir le code Python
code = st.text_area("Saisissez votre code Python ici:")

#Bouton pour exécuter le code
if st.button("Exécuter le code"):
    if code:
        try:
            # Créer une zone pour afficher le code saisi
            st.subheader("Code saisi 😊")
            st.code(code, language="python")

            # Rediriger la sortie standard vers un tampon
            old_stdout = sys.stdout
            new_stdout = StringIO()
            sys.stdout = new_stdout

            # Exécuter le code Python saisi
            exec(code, {})

            # Récupérer la sortie standard capturée
            output = new_stdout.getvalue()

            # Restaurer la sortie standard d'origine
            sys.stdout = old_stdout

            # Créer une zone pour afficher le résultat
            st.subheader("Résultat de l'exécution 😊")
            st.text(output)

        except Exception as e:
            st.error(f"Erreur : {e}")
        finally:
            st.info("Merci d'avoir utilisé cette application !")    

# Barre latérale
st.sidebar.header("Petite Note pour le plaisir d'une petite note")
st.sidebar.info("Les projets fantaisistes d'Elon Musk sont comme des étoiles filantes dans le ciel de l'innovation, illuminant l'avenir de l'humanité. :smiling_imp:\nIls sont le fruit d'une imagination audacieuse, d'une détermination sans bornes et d'une vision inébranlable. Parmi ces projets, on trouve des idées telles que la colonisation de Mars, le développement de voitures électriques révolutionnaires, la construction de tunnels de transport souterrains, l'exploration du cerveau humain :brain:, et même la création de réseaux de communication mondiaux via des constellations de satellites :alien:\nCes projets incarnent l'esprit de l'aventure et de l'exploration, repoussant constamment les limites de ce qui est possible.")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://i.postimg.cc/4xgNnkfX/Untitled-design.png");
background-size: cover;
background-position: center center;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

                
