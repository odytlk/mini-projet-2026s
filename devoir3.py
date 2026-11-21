# Sujet 1 — Gestion d'une cafétéria universitaire
#
# Développer une application pour gérer les produits, les recettes,
# les ingrédients, les clients et les commandes.
#
# Fonctionnalités attendues :
#
# • Gérer les recettes et les stocks d'ingrédients.
# • Créer des commandes contenant plusieurs produits et les modifier
#   avant validation.
# • Appliquer des règles tarifaires différentes aux étudiants et au
#   personnel grâce à l'héritage.
# • Suivre les commandes : en préparation, prêtes, livrées ou annulées.
# • Présenter les ventes, les produits les plus demandés et les alertes
#   de stock.
#
# Contrainte centrale : vérifier les besoins cumulés de tous les
# produits avant de valider une commande. Si un ingrédient manque,
# aucun stock ne doit être débité. Définir les conditions d'annulation
# et leur effet sur les stocks et les recettes.

import json

# lien avec le fichier json
FICHIER_JSON = "donnees.json"

with open(FICHIER_JSON, "r", encoding="utf-8") as f:
    donnees = json.load(f)

def sauvegarder():
    donnees["stocks"] = {s.ingredient: s.quantite for s in List_stocks}
    donnees["commandes"] = List_commandes
    donnees["historiques"] = hitoriques
    with open(FICHIER_JSON, "w", encoding="utf-8") as f:
        json.dump(donnees, f, indent=2, ensure_ascii=False)


reponse = "0"
comande_reponse = "0"
validation ="0"
status = ""
ordre = []
List_commandes = donnees["commandes"]
hitoriques = donnees["historiques"]
# section de gestion des ingredient
class stock:
    def __init__(self,ingredient, quantite):
        self.ingredient = ingredient
        self.quantite = quantite



    def __str__(self):
        return f"{self.ingredient} : {self.quantite} "

s1 = stock("farine", donnees["stocks"]["farine"])
s2 = stock("fromage", donnees["stocks"]["fromage"])
s3 = stock("sauce tomate", donnees["stocks"]["sauce tomate"])
s4 = stock ("pain", donnees["stocks"]["pain"])
s5 = stock("jambon", donnees["stocks"]["jambon"])
s6= stock ("orange", donnees["stocks"]["orange"])
s7= stock("sucre", donnees["stocks"]["sucre"])
s8 = stock("oeuf", donnees["stocks"]["oeuf"])
List_stocks = [s1,s2,s3,s4,s5,s6,s7,s8]

# section de gestion des produit

class menu:
    def __init__(self,produit, prix,quantite):
        self.produit = produit
        self.prix = prix
        self.quantite = quantite
        self.possible = True
        self.stock = List_stocks
        if self.produit == "pizza":
            self.recette= {"farine":200,"fromage":100,"sauce tomate":50}
        elif self.produit == "sandwich":
            self.recette= {"pain":1,"fromage":50,"jambon":2}
        elif self.produit == "jus":
            self.recette= {"orange":3,"sucre":10}
        elif self.produit == "omelette":
            self.recette={"oeuf":3,"fromage":30}


    def preparer(self, nb=1):
        # Étape 1 : vérifier tous les ingrédients
        for nom, requis in self.recette.items():
            trouve = False
            for s in self.stock:
                if s.ingredient == nom:
                    trouve = True
                    self.possible = True
                    if s.quantite < requis * nb:
                        print(f"Impossible de préparer : {nom} insuffisant")
                        self.possible= False
                        return
            if not trouve:
                print(f"Impossible de préparer : {nom} absent du stock")
                self.possible= False
                return


        # Étape 2 : débiter (seulement si tout est bon)
        for nom, requis in self.recette.items():
            for s in self.stock:
                if s.ingredient == nom:
                    s.quantite -= requis * nb

        self.quantite += nb
        print(f"{nb} {self.produit} ajouter au panier")
        return

    def rendre(self, nb):
        for nom, requis in self.recette.items():
            for s in self.stock:
                if s.ingredient == nom:
                    s.quantite += requis * nb
        self.quantite -= nb

    def __str__(self) :
        return f"{self.produit} : {self.prix} HTG"



p1 = menu("pizza", 500,0)
p2 = menu("sandwich", 250, 0)
p3 = menu("jus", 150, 0)
p4 = menu("omelette", 200, 0)

# section gestion client

class client :
    def __init__(self,nom):
        self.nom = nom
        self.panier= []
        self.prix =[]
        self.quantite = []
        self.historique = []

    def achat(self,produit, quantite):
        self.panier.append({produit: quantite})
        print (self.panier)

class etudiant(client) :
    def __init__(self,nom):
        super().__init__(nom)
        self.reduction = 0.4


c1 = etudiant("etudiant")
c2 = client("proffeseur")




# section de gestion des achat

def commande() :
    while True :
        print(f"MENU de commande"
                  f"\n bien venu cher {status.nom}, veuiller passer une commande"
                  f"\nProduit disponible  :"
                  f"\n 1-{p1}"
                  f"\n 2-{p2}"
                  f"\n 3-{p3}"
                  f"\n 4-{p4}"
                  f"\n 5- retour "
                  )
        if status.panier != []:
            print(f"\n{status.panier}")
            print("vous pouvez encor ajouter d autre produit , sinon")
            print("\n---taper 'ok' pour passer a la caisse---" )

    # section de gestion des commandes de produits

        comande_reponse=(input("reponse :"))
        while True :
            if comande_reponse == "1":
                objet = p1
            elif comande_reponse == "2":
                objet=p2
            elif comande_reponse == "3":
                objet= p3
            elif comande_reponse == "4":
                objet=p4
            elif comande_reponse == "5":
                 return

            elif comande_reponse == "ok":
                total= 0
                print("panier de commande")
                choix = []
                for i in range(len(status.panier)):
                    somme = status.prix[i] * status.quantite[i]
                    print(f"\n{1 + i}-{status.panier[i]}  Prix : {status.prix[i]}*{status.quantite[i]} = {somme} HTG")
                    total+=somme
                    choix.append(str(1+i))
                if status == c1:
                    print(status.reduction*total)
                    print (f"total : {total} HTG"
                           f"\n- STATUS ETUDIANT -reduction de  -{status.reduction*total} HTG "
                           f"\n Nouveau total {total-(status.reduction*total)} HTG")
                else:
                     print(f"total {total} HTG")
                print("\npour supprimer une comande inscriver son numero, sinon")
                print("---taper ok pour valider la comande--")
                validation = input("reponse : ")


                if validation in choix:
                    i = int(validation) - 1
                    ordre[i].rendre(status.quantite[i])
                    status.panier.pop(i)
                    status.prix.pop(i)
                    status.quantite.pop(i)
                    ordre.pop(i)

                    break
                elif validation == "ok":
                    print("marci d'avoir passer commande !")

                    nouvelle_commande = {
                        "client": status.nom,
                        "produits": status.panier.copy(),
                        "statut": "En preparation"
                    }
                    status.panier=[]
                    status.quantite= []
                    status.prix= []

                    List_commandes.append(nouvelle_commande)
                    sauvegarder()

                    return
                else:
                    print("mauvaise entrer, veuiller recommancer")
                    break

            else:
                print("mauvaise entrer, veuiller recommancer")
                break


            if comande_reponse != "0":
                print(f"panier d'achat"
                      f"\n {objet}")
                nb = int(input(f"combien de {objet.produit} ?:"))
                objet.preparer(nb)
                if objet.possible == True:
                    status.achat(objet.produit, nb)
                    status.prix.append(objet.prix)
                    status.quantite.append(nb)
                    ordre.append(objet)

                break





# suivi des commandes
def suivi_commande():

    print("===== SUIVI DES COMMANDE =====")

    if List_commandes == []:
        print("Aucune commande")
        return

    for i in range(len(List_commandes)):
        print(f"\nCommande numero : {i+1}")
        print(f"Client : {List_commandes[i]['client']}")
        print(f"Produits : {List_commandes[i]['produits']}")
        print(f"Statut : {List_commandes[i]['statut']}")

    choix = int(input("\nNumero de commande : "))

    if choix > 0 and choix <= len(List_commandes):

        print("\n1- En preparation")
        print("2- Prete")
        print("3- Livree")
        print("4- Annulee")

        reponse = input("Nouveau statut : ")

        if reponse == "1":
            List_commandes[choix-1]['statut'] = "En preparation"

        elif reponse == "2":
            List_commandes[choix-1]['statut'] = "Prete"

        elif reponse == "3":
            List_commandes[choix-1]['statut'] = "Livree"
            hitoriques.append(List_commandes[choix-1])

        elif reponse == "4":
            List_commandes[choix-1]['statut'] = "Annulee"
            hitoriques.append(List_commandes[choix - 1])

        else:
            print("Mauvaise reponse")
            return

        print("Statut modifie avec succes")
        sauvegarder()

    else:
        print("Commande introuvable")




# section de gestion de l admin

def administrator() :
    print(f"MENU de gestion de la cafeteriat"
          f"\n 1- Gestion des stocks"
          f"\n 2- Historique des ventes"
          f"\n 3- Suivi des commandes")

    admin_reponse=(input("reponse :"))
    if admin_reponse == "1" :
        print(f"stocks de la cafeteriat")
        t=1
        alert = ""
        for i in List_stocks:
            if i.quantite<= 0:
                alert = "(stock vide)"
            elif i.quantite<=70:
                alert= "(stock faible) "
            else:
                alert= "(en stock) "
            print(f"{t}-{i}, {alert}")
            t+=1
        print ("--- Pour ajouter des ingredient en stock taper ok ")
        admin_reponse=(input("reponse :"))
        if admin_reponse == "ok" :
            print("inscriver le numero du stock que vous vouler ajouter")
            admin_reponse=(input("reponse :"))
            match admin_reponse:
                case"1":
                    s1.quantite+= int(input("inscrire la quantite :"))
                case"2":
                    s2.quantite+= int(input("inscrire la quantite :"))
                case"3":
                    s3.quantite+= int(input("inscrire la quantite :"))
                case"4":
                    s4.quantite+= int(input("inscrire la quantite :"))
                case "5":
                    s5.quantite += int(input("inscrire la quantite :"))
                case "6":
                    s6.quantite += int(input("inscrire la quantite :"))
                case "7":
                    s7.quantite += int(input("inscrire la quantite :"))
                case "8":
                    s8.quantite += int(input("inscrire la quantite :"))
            sauvegarder()



    elif admin_reponse == "2" :
        print(f"historiques des vente")
        for i in range (len(hitoriques)):
            print(f"Client : {hitoriques[i]['client']}")
            print(f"Produits : {hitoriques[i]['produits']}")
            print(f"Statut : {hitoriques[i]['statut']}\n")



    elif admin_reponse == "3" :
        suivi_commande()


# section de gestion du menu principal

while True :
    print(f"MENU"
          f"\nconnecter vous en tans que :"
          f"\n 1- etudiant "
          f"\n 2- proffeseur "
          f"\n 3- Admin ")
    reponse =(input("reponse :"))
    if reponse == "1" :
        status = c1
        commande()
    elif reponse == "2" :
        status = c2
        commande()
    elif reponse == "3" :
        status = "admin"
        administrator()
    else:
        print("reponse incorecte , veuiller reessayer")
        reponse = "0"
