"""
Text-Adventure in python ( FR version )
Intro - Game Over - Premiere et les salles bis
"""
import time
import part2

# Classe principal
class TextAdventure:
    def __init__(self):
        self.speech_narrator = str
        self.speech_sign = str

    # Methode de Game Over
    def gameover(self, raison):
        print("Game Over :", raison)
        
    # Methode pour le début de partie ( introduction )
    def beginning(self):
        self.speech_narrator = "--------------- NARRATEUR ---------------\n" \
                           "Vous vous réveillez à l'intérieur d'une salle, devant vous un panneau et une porte, choisissez-vous lire le panneau ?\n" \
                           "\tChoix 1 -- Lire le pancarte\n" \
                           "\tChoix 2 -- Franchir la porte\n" \
                           "---------------"
        print(self.speech_narrator)
        # Reponse du joueur
        reponse = int(input("Votre choix : "))
        
        if reponse == 1:
            # Lecture de la pancarte
            self.speech_sign = "\n--------------- PANCARTE ---------------\n" \
                               "Salut Amigo, tu te demandes peut-être où tu te trouves actuellement... Sache que moi-meme je n'en ai aucune idée hahaha !!\n" \
                               "J'espère ne pas t'avoir vexé ! Me concernant, je suis juste une personne transporté ici, je laisse des pancartes pour les « échoués » comme toi.\n" \
                               "Si je ne meurs pas d'entité inconnue, tu auras des nouvelles de moi et de mes découvertes via les pancartes donc lis les !\n" \
                               "Amigo, à très vite !\n" \
                               "---------------"
            print(self.speech_sign)
            time.sleep(15)
            print("Après la lecture de la pancarte, vous décidez de franchir la porte...")
            self.first_room()
        
        elif reponse == 2:
            # Choix franchir la porte
            self.speech_narrator = "\n--------------- NARRATEUR ---------------\n" \
                            "Vous ignorez la pancarte et décidez d'ouvrir la porte devant vous pour ainsi passer à la salle suivante...\n" \
                            "---------------"
            print(self.speech_narrator)
            self.first_room()
        else:
            self.gameover("Respecte les règles sinon j'viens m'occuper de ton cas, c'est 1 ou 2 PAS AUTRE CHOSE")
    
    # Premiere salle
    def first_room(self):
        # Attente de 3s pour ne pas envoyer trop de texte d'un coup
        time.sleep(3)
        self.speech_narrator = "\n--------------- NARRATEUR ---------------\n" \
                    "Alors que vous entrez dans la salle, une atmosphère pesante vous enveloppe, laissant une sensation de frissonnement sur votre peau.\n" \
                    "Vous vous retrouvez face à deux portes mystérieuses, chacune renfermant peut-être des secrets inexplorés.\n" \
                    "Une se trouve juste en face de vous, tandis que l'autre se dresse à votre gauche, dissimulant peut-être des réponses à vos questions.\n" \
                    "Choisissez avec précaution, car votre destin repose sur le seuil de l'une de ces portes lugubres.\n" \
                    "\tChoix 1 -- Porte de Gauche\n" \
                    "\tChoix 2 -- Porte en face de vous\n" \
                    "---------------"
        print(self.speech_narrator)
        
        # Reponse du joueur
        reponse = int(input("Votre choix : "))

        # Porte de Gauche ( bis_room -- secrete )
        if reponse == 1:
            print("Vous entrez dans la porte de gauche...\n")
            self.bis_room()
        elif reponse == 2:
            # deuxieme salle provenant de l'autre fichier python pour pas mettre trop de ligne ici
            print("Vous entrez dans une nouvelle salle...\n")
            test = part2.Adventure()
            time.sleep(2)
            test.second_room()
        else:
            self.gameover("Les ténèbres du non-respect des règles vous engloutisse, 1 ou 2. Pourquoi autre chose...")
    
    def bis_room(self):
        time.sleep(2)
        self.speech_narrator = "--------------- NARRATEUR ---------------\n" \
                    "Lorsque vous franchissez le seuil de la salle, une aura inquiétante s'abat sur vous, glaçant votre sang et éveillant vos instincts de survie\n" \
                    "\tLes murs décrépis se dressent devant vous, recouverts de messages énigmatiques tracés dans une encre noire et dégoulinante.\n" \
                    "\tLeurs mots s'entremêlent dans un langage sinistre, semblant murmurer des présages funestes, vous distinguez une chaîne de mot compréhensible\n" \
                    "..Labyri..nt..he... Pie..ge.....\n" \
                    "---------------"
        print(self.speech_narrator)
        time.sleep(11)
        self.gameover("\nL'apparition d'un être sinistre et mystérieux scelle votre destin, interdisant toute révélation des sombres secrets qui hantent cet endroit maudit.")


if __name__ == "__main__":
    obj = TextAdventure()
    obj.beginning()
