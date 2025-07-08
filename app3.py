from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI
import mysql.connector as mysql
 
# modèle utilisé
# modèle de base gpt-4.1-nano-2025-04-14
# fichier fine-tuning file-2MPUmfbVhpq2XPCcyL4sk3
modele = "ft:gpt-4.1-nano-2025-04-14:jn-formation::BqyjOIN3"
 
# initialise connection openai
def initialiser():
    load_dotenv()
    client = OpenAI()
    return client
 
# gère envoi des requêtes et réception des réponses avec l'api openai
# gère erreurs liées à l'api
def demander(client, prompt):
    # gestion d'erreur
    try:
        # si succès
        reponse = client.responses.create(
            model = modele,
            input = prompt
        )
        return 1, reponse.output_text
    except Exception as e:
        # si erreur
        return 2, f"Erreur inattendue : {str(e)}"
 
# archivage des conversations avec le chatbot en base de données
def sauvegarder_echange(prompt, reponse, date, statut):
    # connexion à la base de données
    connexion = mysql.connect(
        host='localhost',
        user='root',
        password='example',
        database='cgvbot',
        port=3306
    )
    # initialise curseur et envoi de la requête
    curseur = connexion.cursor()
    requete = """
            INSERT INTO echanges (prompt, reponse, date, statut)
            VALUES (%s, %s, %s, %s)
        """
    valeurs = (prompt, reponse, date, statut)
    curseur.execute(requete, valeurs)
    connexion.commit()
    # ferme les connexions à la base de données
    curseur.close()
    connexion.close()
 
def main():
    # initialise
    client = initialiser()
    prompt = ""
    print("\033[92mChatbot MonEshop - Powered by OpenAI")
    print("Des questions sur nos CGV ? Le bot vous répondra immédiatement !\033[0m")
    # boucle principale
    # str.lower pour prendre en compte les Exit, eXit, EXit, exIt...
    while str.lower(prompt) != "exit":
        # saisie
        prompt = input("Vous >> ")
        # sortie de boucle si saisie vide ou exit
        if prompt == "" or str.lower(prompt) == "exit":
            print("Merci d'avoir utilisé notre chatbot, à bientôt !")
            break
        # appel api openai
        # récupère code d'erreur et réponse
        # code d'erreur 1 = succès
        code_erreur, reponse = demander(client, prompt)
        # gestion couleur de la réponse
        # vert si succès rouge si erreur
        code_couleur = "\033[92m" if code_erreur == 1 else "\033[31m"
        # affichage réponse ou message d'erreur
        print("Bot >> ", code_couleur, reponse, "\033[0m")
        # archivage de l'échange en base de données
        sauvegarder_echange(prompt, reponse, datetime.now(), code_erreur)
 
if __name__ == "__main__":
    main()