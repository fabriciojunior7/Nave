import pygame

#Cores
branco = (255, 255, 255)
preto = (0, 0, 0)

class Nave(pygame.sprite.Sprite):
    def __init__(self, largura, altura):
        pygame.sprite.Sprite.__init__(self)

        self.imagem = pygame.image.load("imagens/nave.png")
        self.corpo = self.imagem.get_rect()
        self.corpo.centerx = largura/2
        self.corpo.centery = altura/2
        self.velocidadeY = 0
        self.velocidadeX = 0
        self.forcaX = 0.3
        self.forcaY = 0.3
        self.motorLigado = False

    def pintar(self, tela):
        tela.blit(self.imagem, self.corpo)

    def voar(self):
        self.velocidadeY -= self.forcaY

    def cair(self, gravidade):
        self.velocidadeY += gravidade
        self.corpo.move_ip(0, self.velocidadeY)
        if(self.velocidadeX > 0):
            self.velocidadeX -= 1
        elif(self.velocidadeX < 0):
            self.velocidadeX += 1

    def mover_direita(self):
        self.velocidadeX = 2
        self.corpo.move_ip(self.velocidadeX, 0)

    def colisao(self, largura, altura):
        #Eixo X
        if(self.corpo.centerx > largura):
            self.velocidadeX = -1
        elif(self.corpo.centerx < 0):
            self.velocidadeX = 1
        #Eixo Y
        if(self.corpo.centery > altura):
            self.velocidadeY = -1
        elif(self.corpo.centery < 0):
            self.velocidadeY = 1

    def rodar(self, tela):
        self.imagem = pygame.transform.rotate(self.imagem, -89)


