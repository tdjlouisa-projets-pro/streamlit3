import pandas as pd
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu
import streamlit_authenticator as stauth 

# ---------------------------------------------------------
# 1. CONFIGURATION PAGE (Une seule fois au tout début !)
# ---------------------------------------------------------
st.set_page_config(
    page_title="MON ALBUM PHOTO",
    page_icon=":)",
    layout="wide"  # Utilise toute la largeur de l'écran
)

# ---------------------------------------------------------
# 2. CONFIGURATION AUTHENTIFICATION
# ---------------------------------------------------------
lesDonneesDesComptes = {
    'usernames': {
        'utilisateur': {
            'name': 'Utilisateur Test',
            'password': 'utilisateurMDP', # Note: En prod, utilisez des mots de passe hachés
            'email': 'utilisateur@gmail.com',
            'failed_login_attempts': 0, 
            'logged_in': False,
            'role': 'utilisateur'
        },
        'root': {
            'name': 'Administrateur',
            'password': 'rootMDP',
            'email': 'admin@gmail.com',
            'failed_login_attempts': 0,
            'logged_in': False,
            'role': 'administrateur'
        }
    }
}

# Initialisation de l'authenticator
authenticator = stauth.Authenticate(
    lesDonneesDesComptes, # Les données (credentials)
    "mon_album_cookie",   # Nom du cookie
    "abcdef",             # Clé secrète (random string)
    30                    # Expiration en jours
)

# APPEL DE LA FONCTION LOGIN (Indispensable pour afficher le formulaire)
authenticator.login()

# =========================================================
# AJOUT POUR ENTRER SANS MOT DE PASSE (A SUPPRIMER PLUS TARD)
if st.session_state["authentication_status"] is None:
    st.session_state["authentication_status"] = True
    st.session_state["name"] = "Mode Développeur"
    st.session_state["username"] = "dev"
# =========================================================
# ---------------------------------------------------------
# 3. LOGIQUE D'AFFICHAGE PRINCIPALE
# ---------------------------------------------------------

# CAS 1 : L'UTILISATEUR EST CONNECTÉ (Succès)
if st.session_state["authentication_status"]: 
    
    # --- SIDE BAR (Menu) ---
    with st.sidebar:
        st.write(f"Connecté en tant que : **{st.session_state['name']}**")
        # Le bouton de déconnexion géré par la librairie
        authenticator.logout('Déconnexion', 'sidebar') 
        
        st.markdown("---")
        selection = option_menu(menu_title=None, options=["Accueil", "Mon album Photos"])

    # --- CONTENU DES PAGES ---
    
    # PAGE ACCUEIL
    if selection == "Accueil":
        col1, col2, col3 = st.columns([3,6,1])
        st.markdown("---")
        with col2:
            st.write("Bienvenue sur la page d'accueil !")
            
        col1, col2, col3 = st.columns([3,6,1])
        with col2:
            st.image("https://media.licdn.com/dms/image/v2/D4E22AQFReJ6ay_kHLg/feedshare-shrink_2048_1536/feedshare-shrink_2048_1536/0/1727866027985?e=2147483647&v=beta&t=n5oehr3Y5XSh-MjWkvZcYjsFowKx1lE8I7ErS0eO1is")
        
        # animation mignions
        url_background = "https://i.pinimg.com/originals/80/f4/b4/80f4b4c09340c2e7c46ca4254a14d9ff.gif"

    # PAGE ALBUM PHOTOS
    elif selection == "Mon album Photos":
        col1, col2, col3 = st.columns([3,6,1])
        with col2:
            st.write("Bienvenue sur mon album photo")
            
        st.markdown("""
        <h1 style="color: white; font-size: 50px; text-align: center;">
            Bienvenue sur mon album photo
        </h1>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)

        # Contenu 1ere colonne : 
        with col1:
            st.image("https://www.monchatestroi.fr/wp-content/uploads/2023/05/Chat-rancunier-info-ou-intox.jpg")

        # Contenu 2e colonne :
        with col2:
            st.image("https://goodflair.com/app/uploads/2024/09/beautiful-bengal-cat.jpg")

        # Contenu 3e colonne : 
        with col3:
            st.image("https://conseils.wanimo.com/veterinaire/wp-content/uploads/2011/05/FIV-du-chat.jpg")

    # PIED DE PAGE (Affiché uniquement si connecté)
    def afficher_footer():
        st.markdown("""
            <div class="footer">
                <br><br><hr>
                © 2025 LT WCS | Design par <b>Streamlit CSS</b> | v.2.0
            </div>
        """, unsafe_allow_html=True)
    
    afficher_footer()

