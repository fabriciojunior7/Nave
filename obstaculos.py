import pygame

class Parede(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.imagem = pygame.image.load("imagens/parede.png")
        self.corpo = self.imagem.get_rect()
        self.posIniX = x
        self.posIniY = y
        self.corpo.centerx = 0
        self.corpo.centery = 0
        self.largura = 15
        self.altura = 15

    def pintar(self, tela, x, y):
        self.corpo.centerx = x + self.posIniX
        self.corpo.centery = y + self.posIniY
        tela.blit(self.imagem, self.corpo)