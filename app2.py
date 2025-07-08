from openai import OpenAI
from dotenv import load_dotenv
import mysql.connector as mysql
from datetime import datetime
load_dotenv()
client = OpenAI()
question = ""


#fonction main pour commencer msg de bienvenu
def main():
    print("Bienvenue sur le chatbot ! Tapez 'exit' pour quitter.")
    while saisi() != 0:
        print("")
        


#fonction saisi
def saisi():
    question = input("Vous avez une question sur les CGV : ")
    # Commande exit
    if question == "exit":
        print("Merci d'avoir utilisé notre chatbot, à bientôt !")
        return 0
    try:
        response = client.responses.create(
            model="ft:gpt-4.1-nano-2025-04-14:jn-formation::BqyjOIN3",
            input= question
        )
        print(response.output_text)
        output = response.output_text
        statut = 1

    except Exception:
        print("Une erreur s'est produite, veuillez reessayer")
        output = "erreur"
        statut = 2
    
    sauvegarder_echange(prompt=question,reponse=output,date=datetime.now(),statut=statut)
    return statut
        

#Archivage
def sauvegarder_echange(prompt, reponse, date, statut):
        # Connexion à la base de données
        connexion = mysql.connect(
            host='localhost',
            user='root',       # à adapter
            password='example',  # à adapter
            database='cgvbot',
            port=3306          # à adapter si nécessaire
        )

        curseur = connexion.cursor()
        requete = """
                INSERT INTO echanges (prompt, reponse, date, statut)
                VALUES (%s, %s, %s, %s)
            """
        valeurs = (prompt, reponse, date, statut)
        curseur.execute(requete, valeurs)
        connexion.commit()
    
        curseur.close()
        connexion.close()

main()

    




