import pygame

class Vaisseau:

    def __init__(self, pos, destinations, couleur, trace=False, sprite=None):
        self.position = pos
        self.destinations = destinations
        self.couleur = couleur
        self.vitesse = 0
        self.derniere_distance = 0
        self.dessine_trajectoire = False
        self.trace = trace
        if sprite:
            try:
                with open(sprite) as sprite_file:
                    raw_sprite = pygame.image.load(sprite_file)
                    self.sprite = \
                        pygame.transform.smoothscale(raw_sprite, (80,80))
            except Exception as error:
                self.sprite = None
        else:
            self.sprite = None

    def avance(self, dt):
        x, y = self.position
        destination = self.destinations[0]
        dx, dy = destination.calcule_pos()
        x = (1 - self.vitesse) * x + self.vitesse * dx
        y = (1 - self.vitesse) * y + self.vitesse * dy
        self.position = x,y
        distance = (x-dx)*(x-dx) + (y-dy)*(y-dy)
        if distance > self.derniere_distance:
            self.vitesse += 0.01
        if abs(x-dx) + abs(y-dy) < 1.0:
            if len(self.destinations) > 1:
                self.destinations = self.destinations[1:]
            self.vitesse = 0
        self.derniere_distance = distance

    def dessine(self, s_persistante, s_temp):
        x, y = self.position
        if self.sprite:
            s_temp.blit(self.sprite, (x-40,y-40))
        else:
            pygame.draw.rect(s_temp, self.couleur, (int(x), int(y), 3, 3))
        if self.dessine_trajectoire:
            position = x, y
            for d in self.destinations:
                dx, dy = d.calcule_pos()
                pygame.draw.line(s_temp, self.couleur, position, (int(dx), int(dy)))
                position = dx, dy
        if self.trace:
            pygame.draw.circle(s_persistante, self.couleur, (int(x), int(y)), 1)
    
