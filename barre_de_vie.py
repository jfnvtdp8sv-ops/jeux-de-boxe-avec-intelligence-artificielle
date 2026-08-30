import pygame


#création de la classe de la barre de vie
class barre:
    def __init__(self, antity, type):
        self.antity = antity
        self.type = type
        if self.type == "perso":
            self.x = 20
            self.y = 20
        elif self.type == "ennemi": 
            self.x = 1050
            self.y = 20
            
            
            
            
            
            
            
    #metode de cration et affichage des barre de vie
    def barre_affichage(self, screen):
        largeur_actuelle = 200 * (self.antity.vie / self.antity.vie_maxe)
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, 200, 20))
        pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, largeur_actuelle, 20))
        
        
        
    
    
    