import time
import pygame
import combat
from personnage import Personnage
from adversaire import Adversaire
from barre_de_vie import barre

pygame.init()

horloge = pygame.time.Clock()
fenetre = pygame.display.set_mode((1280, 720))

# Chargement du fond
fond = pygame.image.load("acets/image_fon.jpg")
fond = pygame.transform.scale(fond, (1280, 720))

# Création des entités
perso = Personnage(-400, 15, 1/3)
ennemi = Adversaire(400, 15, 1/3)

#création des barre
barre_perso = barre(perso, "perso")
barre_ennemi = barre(ennemi, "ennemi")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Gestion des touches du joueur
    touche = pygame.key.get_pressed()
    if touche[pygame.K_r]:
        eta = "avancer"
    elif touche[pygame.K_a]:
        eta = "reculer"
    elif touche[pygame.K_f]:
        eta = "point_droit"
    elif touche[pygame.K_d]:
        eta = "garde"
    elif touche[pygame.K_q]:
        eta = "point_gauche"
    elif touche[pygame.K_e]:
        eta = "coup_de_pied"
    else:
        eta = "immobile"

    # Gestion des touches de l'adversaire
    if touche[pygame.K_u]:
        eta_ennemi = "avancer"
    elif touche[pygame.K_p]:
        eta_ennemi = "reculer"
    elif touche[pygame.K_m]:
        eta_ennemi = "point_droit"
    elif touche[pygame.K_k]:
        eta_ennemi = "garde"
    elif touche[pygame.K_j]:
        eta_ennemi = "point_gauche"
    elif touche[pygame.K_i]:
        eta_ennemi = "coup_de_pied"
    else:
        eta_ennemi = "immobile"

    #verification de colision
    decalage = (ennemi.x - perso.x, ennemi.y - perso.y)
    point_impact = perso.mask.overlap(ennemi.mask, decalage)
    en_colision = bool(point_impact)

    # Mise à jour du joueur
    perso.annimate(eta)
    perso.moov(en_colision)

    # Mise à jour de l'adversaire
    ennemi.annimate(eta_ennemi)
    ennemi.moov(en_colision)
   
    #apliquer les degats
    combat.appliquer_degats(perso, ennemi)
    combat.appliquer_degats(ennemi, perso)

    # Dessin des éléments
    fenetre.blit(fond, (0, 0))
    fenetre.blit(perso.image, (perso.x, perso.y))
    fenetre.blit(ennemi.image, (ennemi.x, ennemi.y))

    #afficher les barre de vie
    barre_perso.barre_affichage(fenetre)
    barre_ennemi.barre_affichage(fenetre)

    pygame.display.flip()

    horloge.tick(240)