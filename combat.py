# Dégâts infligés par chaque type d'attaque
degats = {
    "point_droit": -100,
    "point_gauche": -200,
    "coup_de_pied": -50
}

def appliquer_degats(attaquant, cible):
    if (attaquant.etat_actuel in degats          # l'attaquant est bien en train d'attaquer
        and not attaquant.toucher                # ce coup n'a pas encore touché
        and attaquant.get_hitbox().colliderect(cible.get_hitbox())):  # les hitbox se touchent maintenant

        cible.vie += degats[attaquant.etat_actuel]  # applique les dégâts (déjà négatifs)
        attaquant.toucher = True                    # bloque toute répétition pour ce même coup

        if attaquant.etat_actuel == "coup_de_pied":
            # recul de la cible, dans le sens du coup
            cible.x += 40 if attaquant.x < cible.x else -40