import pygame


#Cores
branco = (255, 255, 255)
preto = (0, 0, 0)

class Nave(pygame.sprite.Sprite):
    def __init__(self, largura, altura):
        pygame.sprite.Sprite.__init__(self)

        self.imagem = pygame.image.load("imagens/nave.png")
        self.largura = 20
        self.altura = 20
        self.corpo = self.imagem.get_rect()
        self.corpo.centerx = largura/2
        self.corpo.centery = altura/2
        self.velocidadeX = 0
        self.velocidadeY = 0
        self.velocidadeYMAX = 3
        self.forcaX = 0.5
        self.forcaY = 0.5
        self.arrasto = 0.05
        self.motorLigado = False
        self.direita = False
        self.esquerda = False

    def pintar(self, tela):
        tela.blit(self.imagem, self.corpo)

    def voar(self):
        self.velocidadeY -= self.forcaY

    def atualizar_bordas(self, gravidade):
        self.velocidadeY += gravidade
        if (self.velocidadeX > -self.arrasto and self.velocidadeX < self.arrasto):
            self.velocidadeX = 0
        elif (self.velocidadeX > 0):
            self.velocidadeX -= self.arrasto
        elif (self.velocidadeX < 0):
            self.velocidadeX += self.arrasto

        self.corpo.move_ip(self.velocidadeX, 0)
        self.corpo.move_ip(0, self.velocidadeY)

    def atualizar_centro(self, gravidade):
        self.velocidadeY += gravidade
        if (self.velocidadeX > -self.arrasto and self.velocidadeX < self.arrasto):
            self.velocidadeX = 0
        elif(self.velocidadeX > 0):
            self.velocidadeX -= self.arrasto
        elif(self.velocidadeX < 0):
            self.velocidadeX += self.arrasto

        #self.corpo.move_ip(self.velocidadeX, 0)
        #self.corpo.move_ip(0, self.velocidadeY)


    def mover_direita(self):
        self.velocidadeX += self.forcaX

    def mover_esquerda(self):
        self.velocidadeX -= self.forcaX

    def colisao_parede(self, parede):
        if(self.corpo.colliderect(parede.corpo)):
            print("COLIDINDO!")


    def colisao(self, largura, altura):
        #Eixo X
        if(self.corpo.centerx > largura - (self.largura/2)):
            self.corpo.centerx = largura - (self.largura/2)
            self.velocidadeX = -(self.velocidadeX - (self.velocidadeX*0.7))
        elif(self.corpo.centerx < (self.largura/2)):
            self.corpo.centerx = self.largura / 2
            self.velocidadeX = -(self.velocidadeX - (self.velocidadeX*0.7))
        #Eixo Y
        if(self.corpo.centery > altura - (self.altura/2)):
            self.corpo.centery = altura - (self.altura/2)
            self.velocidadeY = -(self.velocidadeY - (self.velocidadeY*0.7))
        elif(self.corpo.centery < (self.altura/2)):
            self.corpo.centery = self.altura / 2
            self.velocidadeY = -(self.velocidadeY - (self.velocidadeY*0.7))


