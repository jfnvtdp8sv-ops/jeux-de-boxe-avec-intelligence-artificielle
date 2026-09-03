import os
import pygame

class Personnage:
    # Initialisation du personnage
    def __init__(self, x, y, taille):
        # Position initiale
        self.x = x
        self.y = y
        # Limites de déplacement
        self.x_min = -400
        self.x_max = 500
        self.vitesse = 5
        self.vie = 1000
        self.vie_maxe = 1000
        self.toucher = False
        
        # Dictionnaire des images
        self.images = {
            "immobile": [], "avancer": [], "reculer": [],
            "point_droit": [], "point_gauche": [], "coup_de_pied": [], "garde": []
        }
        # Dossiers des actions
        nom_dossier = ["avancer", "reculer", "immobile", "point_droit", "point_gauche", "coup_de_pied", "garde"]
        # Chargement des images
        for i in nom_dossier:
            liste_fichier = os.listdir(f"acets/joueur/{i}")
            liste_fichier.sort(key=lambda nom: int(nom.split(".")[0]))
            for nom_fichier in liste_fichier:
                self.images[i].append(pygame.image.load(f"acets/joueur/{i}/{nom_fichier}").convert_alpha())
        # Variables d'animation
        self.index = 0
        self.compteur = 0
        self.etat_actuel = "immobile"
        self.etat_demande = "immobile"
        self.image = self.images["immobile"][0]
        self.mask = pygame.mask.from_surface(self.image)

    # Animation du personnage
    def annimate(self, eta):
        attaques = ["point_droit", "point_gauche", "coup_de_pied"]
        #création du masque
        self.mask = pygame.mask.from_surface(self.image)
        # Gestion de la priorité des attaques
        if self.etat_actuel in attaques:
            self.etat_demande = self.etat_actuel
        else:
            self.etat_demande = eta
        # Réinitialisation si changement d'état
        if self.etat_demande != self.etat_actuel:
            self.etat_actuel = self.etat_demande
            self.index = 0
            self.compteur = 0
            self.toucher = False
        # Incrémentation du compteur
        self.compteur += 1
        # Mise à jour de l'index
        if self.compteur >= 2:
            self.compteur = 0
            # Bloquer l'index sur la dernière frame pour la garde
            if self.etat_actuel == "garde":
                if self.index < len(self.images["garde"]) - 1:
                    self.index += 1
            # Gérer la fin des attaques
            elif self.etat_actuel in attaques:
                self.index += 1
                if self.index >= len(self.images[self.etat_actuel]):
                    self.etat_actuel = "immobile"
                    self.index = 0
            # Boucle pour les autres états
            else:
                self.index = (self.index + 1) % len(self.images[self.etat_actuel])
        # Mise à jour de l'image
        self.image = self.images[self.etat_actuel][self.index]
        self.mask = pygame.mask.from_surface(self.image)

    
    
    # Déplacement du personnage
    def moov(self, en_colision):
        # Mouvement vers la droite
        if self.etat_actuel == "avancer" and self.x < self.x_max and not en_colision:
            self.x += self.vitesse
        # Mouvement vers la gauche
        elif self.etat_actuel == "reculer" and self.x > self.x_min:
            self.x -= self.vitesse
    
    
    #metode pour créer la hitbox
    def get_hitbox(self):
        bbox = self.image.get_bounding_rect()
        largeur_hitbox = bbox.width * 0.6
        hauteur_hitbox = bbox.height * 0.55
        decalage_x = bbox.x + (bbox.width - largeur_hitbox) / 2
        decalage_y = bbox.y
        rect = pygame.Rect(self.x + decalage_x, self.y + decalage_y, largeur_hitbox, hauteur_hitbox)
        if self.etat_actuel == "point_droit" or self.etat_actuel == "point_gauche":
            rect.width += 70
        return rect