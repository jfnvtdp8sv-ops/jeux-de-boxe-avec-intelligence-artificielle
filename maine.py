import time
import pygame
from personnage import Personnage
from adversaire import Adversaire

pygame.init()

horloge = pygame.time.Clock()
fenetre = pygame.display.set_mode((1280, 720))

# Chargement du fond
fond = pygame.image.load("acets/image_fon.jpg")
fond = pygame.transform.scale(fond, (1280, 720))

# Création des entités
perso = Personnage(-400, 15, 1/3)
ennemie = Adversaire(400, 15, 1/3)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Dessin des éléments
    fenetre.blit(fond, (0, 0))
    fenetre.blit(perso.image, (perso.x, perso.y))
    fenetre.blit(ennemie.image, (ennemie.x, ennemie.y))

    pygame.display.flip()

    # Gestion des touches du joueur
    touche = pygame.key.get_pressed()
    if touche[pygame.K_RIGHT]:
        eta = "avancer"
    elif touche[pygame.K_LEFT]:
        eta = "reculer"
    elif touche[pygame.K_f]:
        eta = "point_droit"
    elif touche[pygame.K_d]:
        eta = "garde"
    elif touche[pygame.K_q]:
        eta = "point_gauche"
    elif touche[pygame.K_UP]:
        eta = "coup_de_pied"
    else:
        eta = "immobile"

    # Mise à jour du joueur
    perso.annimate(eta)
    perso.moov()

    # Mise à jour de l'adversaire (immobile par défaut)
    ennemie.annimate("immobile")
    ennemie.moov()

    horloge.tick(60)