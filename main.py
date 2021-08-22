"""
Text-Adventure in python ( FR version )
"""
import time
from random import randrange


# Fonction pour les game over pris par le joueur
def game_over(raison):

    print("\n", raison)
    print(" GAME OVER :)")


def seventh_room():
    print("Vous etes arrivé à la septième salle, cependant quelqu'un qui ne semble plus humain se dresse devant vous.\n",
          "Souhaitez-vous rencontré cet etre ?\n",
          "1) Oui\n",
          "2) Non\n")
    reponse = int(input("> "))

    if reponse == 1:
        print("Cet etre vous ordonne de lui donnez son nom...\n")
        reply = input("> ").lower()
        name = ["Dédale", "dédale"]

        if reply in name:
            print("Vous avez vu juste, cet etre est Dédale, celui qui posez les panneaux pour vous.\n",
                  "Il ne semble plus humain, mais vous distinguez un sourire et quelque paroles :\n",
                  "Amigo... Merci...\n")
            time.sleep(5)
            game_over("Cependant, vous mourrez de sa main, l'explication, il prefere vous liberez de ce labyrinthe par lui meme, car il n'existe aucun échappatoire\n")
        elif reply not in name:
            game_over("Vous n'avez pas trouvé le nom de cet etre, il n'hésite pas à vous coupez la tete\n Cependant avant de completement mourir vous distinguez quelques mots : Faux...Amigo...")
    elif reponse == 2:
        game_over("L'etre n'hésite pas à vous décapitez, la raison est qu'il désire vous liberez de cet enfer mal scénarisé...\n")
    else:
        game_over("Tu ne sais pas lire les consignes ?")


def sixth_room():
    print("Vous etes arrivé à la sixième salle, qui diffère totalement des salles précédentes.\n",
          "Une vaste plaine, avec des ruines d'une ancienne cité...\n",
          "Un panneau se trouve devant vous.\n",
          "Souhaitez-vous lire le panneau ?\n",
          "1) Oui\n",
          "2) Non\n")
    reponse = int(input("> "))

    if reponse == 1:
        print("          Hey Amigo !\n",
              "Félicitations d'être arrivé jusque ici, cela devait etre compliqué de trouvé la bonne combinaison.\n",
              "Tu te questionnes peut-être  sur cette salle, et bien sache que c'était mon royaume...\n",
              "Tu dois sûrement  ne rien comprendre haha, c'est normal, lorsque je suis arrivé pour la premiere fois,\n",
              "il n'y avait qu'un village de paysans, puis au fil du temps, on a évolué, jusqu'à devenir une nation.\n",
              "Alors comment ça a pu finir comme ça, en ruine... Des problèmes politiques, que je n'ai pas su m'occuper...\n",
              "Je n'ai pas su bien gérer mon royaume et mon peuple...\n",
              "Amigo cela va être  mon dernier panneau, je ne sais pas si quelqu'un verra les panneaux, mais toutefois\n",
              "s'il y a bien quelqu'un qui les lit, je te souhaite de survivre à tout ça, j'aimerais qu'on se rappel de moi,\n",
              "Amigo peut être aurions-nous la chance de nous rencontré un jour, d'ailleur je m'appel Dédale, souviens t'en haha.\n",
              "Amigo Bonne Chance et ne tombe pas dans les préjudices du labyrinthe\n",
              "PS: J'ai appris que nous n'étions pas les premiers à être arrivé dans le labyrinthe, et qu'ils finissent tous disparu ou mort.\n")
        time.sleep(25)
        print("Au bout des ruines se trouve la porte vers la nouvelle salle...\n")
        time.sleep(2)
        seventh_room()
    elif reponse == 2:
        print("Un etre qui ne semble pas humain se dresse devant vous, et vous ordonne de lui donnez son nom...\n")
        reply = input("> ").lower()
        name = ["Dédale", "dédale"]

        if reply in name:
            print("Vous avez vu juste, cet etre est Dédale, celui qui posez les panneaux pour vous.n",
                  "Il ne semble plus humain, mais vous distinguez un sourire et quelque paroles avant qu'il disparaisse :\n",
                  "Amigo... Merci...\n")
            time.sleep(5)
            game_over("Vous mourrez d'une cause mystérieuse, peut-etre, est-ce le destin de ceux qui évite les pancartes...")

        elif reply not in name:
            game_over("Vous n'avez pas trouvé le nom de cet etre, il n'hésite pas à vous coupez la tete\n Cependant avant de completement mourir vous distinguez quelques mots : Faux...Amigo...")
    else:
        game_over("Tu ne sais pas lire les consignes ?")


def choose_room():
    print("3 portes se trouve devant vous, quel porte choisissez-vous ?\n",
          "1) Porte de Gauche\n",
          "2) Porte du Millieu\n",
          "3) Porte de Droite\n")
    ran_numb = randrange(1, 4)
    print(ran_numb)
    reponse = int(input("> "))

    def choose_room2():
        print("5 portes se trouve devant vous, quel porte choisissez-vous ?\n",
              "1) Porte extrémité gauche\n",
              "2) Porte de gauche\n"
              " 3) Porte du milieu\n",
              "4) Porte de droite\n",
              "5) Porte extrémité droite\n")
        ran_numb2 = randrange(1, 6)  # Choisi un nombre entre 1 à 5 (Portes choisi au hasard donc)
        print(ran_numb2)
        answer = int(input("> "))

        def choose_room3():
            print("5 portes se trouve devant vous, quel porte choisissez-vous ?\n",
                  "1) Porte extrémité gauche\n",
                  "2) Porte de gauche\n"
                  " 3) Porte du millieu\n",
                  "4) Porte de droite\n",)
            ran_numb3 = randrange(1, 5)
            print(ran_numb3)
            which_room = int(input("> "))

        # Boucle POUR LA FONCTION choose_room3() c'est du random
            if which_room == ran_numb3:
                print("Vous sentez une présence, vous épiez, mais vous n'y prêtez pas vraiment d'attention...\n")
                time.sleep(1)
                sixth_room()
            elif which_room != ran_numb3:
                choose_room()
            else:
                game_over("Tu ne sais pas lire les consignes ?")

    # BOUCLE POUR LA FONCTION choose_room2() c'est du random
        if answer == ran_numb2:
            choose_room3()
        elif answer != ran_numb2:
            choose_room()
        else:
            game_over("Tu ne sais pas lire les consignes ?")

#  BOUCLE POUR LA FONCTION choose_room() c'est du random
    if reponse == ran_numb:
        choose_room2()
    elif reponse != ran_numb:
        choose_room()
    else:
        game_over("Tu ne sais pas lire les consignes ?")


def fourth_room():
    print("Vous etes arrivé dans la quatrième salle, 5 portes se présente devant vous\n",
          "Cependant, il y a une pancarte en face des portes\n",
          "Voulez-vous la lire ?\n",
          "1) Lire le panneau\n",
          "2) Ne pas lire le panneau\n")
    reponse = int(input("> "))

    if reponse == 1:
        print("Hey Amigo, ta réussi l'énigme, bien joué !\n",
              "Bon tu vois surement les 5 portes devant toi, eh bien cela fait un bon moment que je suis dessus.\n",
              "Le mystère est qu'ont doit trouvé la bonne combinaison, juste derriere ces portes ce trouve encore d'autres portes.\n",
              "J'espere que tu es née sous une bonne étoile, sinon tu peux y rester bloquer toute ta vie hahaha\n",
              "Je te souhaite bonne chance Amigo !\n",
              "PS : tu recommence l'étape à chaque fois que tu te foire de porte, j'ai remarqué que les portes\n",
              "             sont choisi au hasard à chaque choix, j'espère que tu me comprend hahaha\n")
        time.sleep(20)
        choose_room()

    elif reponse == 2:
        choose_room()

    else:
        game_over("Tu ne sais pas lire les consignes ?")


def enigme():
    print("Qu'est-ce que la vie ?\n",
          "C'est avant tout une histoire qui est raconté,'Ma vie est une énigme dont ton nom est le mot...'\n",
          "'La vie est une phrase interrompue...'", "Qui suis-je ?\n")

    reponse = input("> ").lower()
    ecrivain = ["victor hugo", "Victor Hugo", "victor Hugo", "Victor hugo"]

    if reponse in ecrivain:
        print("Bonne réponse, continuez votre chemin vers la nouvelle salle.")
        fourth_room()
    else:
        game_over("Mauvaise réponse, le labyrinthe a fait son choix.\n Meurs...")


def third_room():
    print("Vous êtes dans la troisième salle, et un panneau se situe devant vous.",
          "Voulez-vous le lire ?\n",
          "1) Lire le panneau\n",
          "2) Ne pas le lire\n")
    reponse = int(input("> "))

    if reponse == 1:
        print("     Salut Amigo !",
              "Si tu lis ça, c'est que tu es en vie haha, tu as du faire face aux gobelins de la salle précédente\n",
              "j'ai fuis, aucune chance d'affronté des monstres sans armes n'est-ce pas ?\n",
              "Amigo, les ennuies commence, cet salle est spécial, enfaite pour passer à l'autre salle, il faut résoudre une énigme\n",
              "perso je n'ai jamais été très bon, mais j'abandonne pas haha\n",
              "Le seul indice que j'ai à te donné est qu'il était un grand écrivain !\n",
              "On se retrouve à la prochaine pancarte, si je suis en vie ! haha\n")
        time.sleep(20)
        enigme()

    elif reponse == 2:
        enigme()
    else:
        game_over("Tu ne sais pas lire les consignes ???")


def second_room():
    print("Vous êtes dans la seconde salle avec à l'intérieur un coffre gardé par 3 gobelins\n",
          "La porte pour la troisième salle se trouve à quelques pas du groupe de gobelins\n",
          "Voulez-vous :\n",
          "1) Combattre ces gobelins\n",
          "2) Fuir vers la porte\n")
    reponse = int(input("> "))

    if reponse == 1:
        game_over("Les gobelins sont 3 et armé, vous finissez encerclé, et abattue par les gobelins.\n")

    elif reponse == 2:
        print("Passage à la troisième salle, en laissant les gobelins et le coffre derrière...\n")
        third_room()
    else:
        game_over("Tu ne sais pas lire les consignes ??")


def first_room():
    print("Vous arrivez dans la première salle du labyrinthe, 2 portes se trouvent devant vous...\n",
          "Une inscription est écrite au-dessus de chaque porte : \n",
          "1) Porte de Droite : Continuer\n",
          "2) Porte de Gauche : Liberté\n"
          "             Quelle porte choisissez-vous, 1 ou 2 ?\n")
    reponse = int(input("> "))

    if reponse == 1:
        print("Vous entrez dans la seconde salle,cependant, juste avant la fermeture complete de la porte",
              "vous entendez un bruit strident...\n")
        time.sleep(5)
        second_room()

    elif reponse == 2:
        print("Vous ouvrez la porte avec espoir de sortir de ce labyrinthe.",
              "Cependant, vous n'y trouvez pas la liberté espérer...",
              "Seul un panneau au milieu de la salle, avec écrit :\n",
              "             Bienvenue...")
        time.sleep(5)
        game_over("Mort inconnu, aucune trace...")

    else:
        game_over("Tu ne sais pas lire les consignes ??")


def early_game():
    # Introduction
    print("Vous vous réveillez à l'intérieur d'une salle, devant un panneau, choisissez vous de lire le panneau ( 1 ou 2 )?\n",
          "1) Lire le panneau\n",
          "2) Ne pas le lire\n")
    reponse = int(input("> "))

    if reponse == 1:
        # Lecture de la pancarte + passage dans l'autre salle
        print("         Salut Amigo\n\n", "Tu te demandes peut-être où tu te trouves actuellement, eh bien moi-même, je ne sais pas haha !\n",
              "Ne sois pas vexé, tout ce que je sais, c'est que nous sommes dans un labyrinthe.\n",
              "Je n'ai moi-meme pas beaucoup d'information actuellement.\n",
              "J'essayerais de te parler de mon aventure à travers les pancartes que je laisserais sur mon passage.\n\n",
              "Amigo, à toi de survivre, pour me raconter ton aventure !\n\n",
              "PS : il y a sûrement des monstres dans ce labyrinthe, Bonne chance !\n\n")

        # Passage dans l'autre salle après 20 secondes ( pour laisser le temps de lire )
        time.sleep(19)
        first_room()

    elif reponse == 2:
        # Passage direct à l'autre salle
        print("Vous passez à la salle suivante grace à la porte situé devant vous.")
        first_room()

    else:
        # Game Over car le joueur n'a pas suivi les instructions
        game_over("Tu ne sais pas lire les consignes ?")


early_game()
