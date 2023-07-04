"""
Text-Adventure in python ( FR version )
Part 2: Deuxieme salle et plus
"""
import main
import time

class Adventure(main.TextAdventure):
    def __init__(self):
        super().__init__()
    
    # Salle avec l'enigme
    def second_room(self):
        self.speech_narrator = "\n--------------- NARRATEUR ---------------\n" \
            "Au cœur de cette sombre pièce, une énigme se dresse, défiant votre esprit avide de réponses.\n" \
            "Les symboles, soigneusement inscrits sur les murs, attendent patiemment que vous déchiffriez leur secret\n" \
            "révélant ainsi le chemin à suivre pour échapper à cette lugubre épreuve.\n" \
            "Choisissez avec précaution, car votre destin repose sur le resultat donné...\n" \
            "---------------"
        print(self.speech_narrator)
        time.sleep(10)
        self.speech_sign = "\n--------------- ENIGME ---------------\n" \
            "Je suis un dédale sans fin, où les âmes errent en vain,\n" \
            "Dans mes couloirs obscurs, l'espoir s'égare, la peur grandit en vain.\n" \
            "Un défi mystérieux, un voyage périlleux, des choix à faire,\n" \
            "Quête de sortie, perdue dans l'effroi, mon nom est un mystère à défaire.\n" \
            "---------------"
        print(self.speech_sign)
        
        reponse = input("Votre réponse : ").lower()
        answer = ["labyrithe", "labyrinthe"]

        if reponse in answer:
            print("\nVous avez percé le mystère qui engloutissait cet endroit sinistre... Une porte apparaît vous la traversé...")
            self.third_room()
        else:
            self.gameover("\nLes ombres moqueuses semblent se rire de votre tentative infructueuse, chaque erreur peut avoir des conséquences funestes...")
    
    # Salle avec un panneau
    def third_room(self):
        self.speech_narrator = "\n--------------- NARRATEUR ---------------\n" \
            "Arrivé dans cette nouvelle salle, vous découvrez une pancarte devant vous.\n" \
            "Souhaitez-vous lire la pancarte ?\n" \
            "\tChoix 1 -- Lire le pancarte\n" \
            "\tChoix 2 -- Vous reposez\n" \
            "---------------"
        print(self.speech_narrator)
        
        reponse = int(input("Votre choix : "))

        if reponse == 1:
            # Lecture de la pancarte
            self.speech_sign = "\n--------------- PANCARTE ---------------\n" \
                                "Salut Amigo, si tu lis ce panneau c'est que tu as réussi à résoudre l'énigme, me concernant j'ai eu du mal à trouver la réponse hahaha.\n" \
                                "Tu t'en doutes surement, mais nous sommes dans un Labyrinthe, j'ai découvert qu'il y avait de nombreux pièges menant à une mort certaine,\n" \
                                "fait attention lors de tes choix. J'ai aussi découvert certaine entité vagabondant dans le labyrinthe.\n" \
                                "Ils me font penser à des âmes boqué dans un dédale infini... En tout si tu en croise fuis vite !\n" \
                                "J'essayerais de revenir avec de bonne nouvelle la prochaine fois, à très vite Amigo !\n" \
                                "---------------"
            print(self.speech_sign)
            time.sleep(10)
            print("\nVous sortez de la salle avec la pancarte, pour rentrer dans une salle des plus étrange...")
            self.fourth_room()
        elif reponse == 2:
            self.gameover("\nNombreux sont ceux dont le repos fut mortel...Bienvenue parmis eux...")
        else:
            self.gameover("\nChaque erreur à une conséquence...Retourne d'ou tu viens...")
    
    # Puzzle room
    def fourth_room(self):
        time.sleep(1)
        self.speech_narrator = "\n--------------- NARRATEUR ---------------\n" \
            "Alors que vous pénétrez dans la quatrième salle, l'atmosphère s'alourdit et l'obscurité vous enveloppe.\n" \
            "Les murmures énigmatiques remplissent l'air, révélant une épreuve bien différente de ce que vous avez connu jusqu'à présent.\n" \
            "Devant vous se dressent des inscriptions ésotériques, chargées de questions philosophiques captivantes.\n" \
            "Des traces témoignant d'une vie humaine... D'une civilisation avancée qui maitrisait les mystères de l'univers.\n" \
            "Préparez-vous à plonger dans les abysses du savoir et à défier les énigmes philosophiques qui vous attendent dans cette salle empreinte de mystère.\n" \
            "---------------"
        print(self.speech_narrator)
        time.sleep(5)

        puzzle_question = ["\nQu'est-ce qui est tout et rien à la fois ?",
                    "\nJe peux être touché, mais je ne peux pas être saisi. Qui suis-je ?", 
                    "\nPlus je suis grand, moins je suis visible. Que suis-je ?"]
        puzzle_answer = ["le silence", "le vent", "l'obscurité"]
    
        for i, question in enumerate(puzzle_question):
            print(f"\nQuestion {i+1}: {question}")
            reponse = input("Votre réponse : ")
            if reponse.lower() != puzzle_answer[i].lower():
                self.gameover("Mauvaise réponse ! Les ténèbres vous engloutissent, retentez votre chance dans une prochaine vie...")
                return False
            print(f"Vous avez réussi l'énigme {i+1} sur {len(puzzle_question)}...\n")
        print("Vous avez réussi l'énigme d'une ancienne civilisation, peut-être allez vous enfin réussir à vous échapper de ce labyrinthe...")
        time.sleep(2)
        print("Vous accédez à une salle qui semble être totalement différente des précédentes... Serait-ce la fin ?")
        self.final_room()

    def final_room(self):
        time.sleep(2)
        self.speech_narrator = "\n--------------- NARRATEUR ---------------\n" \
            "Félicitations, voyageur intrépide. Tu as bravé les épreuves de ce premier quartier du labyrinthe.\n" \
            "Cependant, sache que tu n'as vu qu'un visage parmi les multiples facettes de ce dédale mystérieux.\n" \
            "Trois autres parties attendent d'être explorées, chacune avec ses propres défis et secrets.\n" \
            "Prépare-toi à plonger plus profondément dans les abîmes du labyrinthe, car ton périple est loin d'être terminé.\n" \
            "---------------"
        print(self.speech_narrator)
        time.sleep(8)
        self.gameover("Merci d'avoir suivi cette première partie d'aventure, bon vous vous êtes douté de mon inéfficacité à l'écriture d'histoire,\n" \
                      "cependant si vous êtes arrivé jusqu'à là, c'est qu'elle vous a quand même interressé n'est-ce pas ??\n" \
                      "Encore merci d'avoir pris du temps pour cette histoire, n'hésitez pas à me contacté pour me faire un retour !\n" \
                      "C'était juste une idée fun qui est apparut dans ma tête.")
