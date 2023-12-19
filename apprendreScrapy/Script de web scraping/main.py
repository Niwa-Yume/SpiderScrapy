# Importer les modules nécessaires
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
from geopy.geocoders import Nominatim
import json
import datetime
import dateparser

# URL de la page des événements avec le filtre pour la catégorie "fête"
url = "https://ladecadanse.darksite.ch/evenement-agenda.php?genre=fête&courant=2023-11-27&sem=0&page=1&nblignes=50&tri_agenda=dateAjout"

try:
    # Envoi de la requête GET pour avoir le contenue de la page que je souhaite scrapper
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    events = soup.find_all("div", class_="evenement")

    # Parcours des événements et affichage des informations
    for event in events:
        try:
            #on récupère le titre
            title = event.find("a", class_="url").text.strip()

            # récup le lieu
            event_locatation = event.find("span", class_="right location").get_text(strip=True)

            # Extraire la description 
            event_description = event.find("div", class_="description").get_text(strip=True)

            # Extraire la date 
            date = soup.h3.text

            #on récupère le lieu ou va se passer l'événement
            location = event.find("span", class_="right location").text.strip()
            
            #on récupère la rue du lieu ou va se passer l'événement
            #street = event.find("span", class_="right street").text.strip()

            #AFFICAGE DES INFORMATIONS :
            print("-----------------------")
            print("Titre : ", title)
            print("   ")
            print("Date : ", date)
            print("   ")
            print("Lieu : ", location)
            print("   ")
            #print("Rue : ", street) 
            print("   ")
            print("Description : ", event_description)
            print("   ")
            print("-----------------------")
        except Exception as e:
            print("Une erreur est arriver lors de l'exècution du script :", str(e))
except Exception as e:
    print("Une erreur est arriver lors de l'exècution du script : ", str(e))