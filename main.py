import pygame, sys
import nave

#Cores
branco = (255, 255, 255)
preto = (0, 0, 0)
cinza = (50, 50, 50)

def main():

    pygame.init()
    largura = 640
    altura = 480
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Navezinha!")
    relogio = pygame.time.Clock()
    frames = 30
    frames_passados = 0

    player = nave.Nave(largura, altura)
    gravidade = 0.25

    plano_fundo = pygame.image.load("imagens/background.jpg")

    cameraX = 0
    cameraY = 0

    while(True):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()

            #Teclado
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_SPACE or event.key == pygame.K_w):
                    player.motorLigado = True
                if(event.key == pygame.K_d):
                    player.direita = True
                if (event.key == pygame.K_a):
                    player.esquerda = True

            if(event.type == pygame.KEYUP):
                if(event.key == pygame.K_SPACE or event.key == pygame.K_w):
                    player.motorLigado = False
                if (event.key == pygame.K_d):
                    player.direita = False
                if (event.key == pygame.K_a):
                    player.esquerda = False

        #Rodar
        relogio.tick(frames)
        pygame.display.update()
        player.cair(gravidade)
        player.colisao(largura, altura)
        if(player.motorLigado == True):
            player.voar()
        if(player.direita == True):
            player.mover_direita()
        if (player.esquerda == True):
            player.mover_esquerda()


        #Desenhas
        cameraX -= player.velocidadeX
        cameraY -= player.velocidadeY
        tela.fill(cinza)
        tela.blit(plano_fundo, (cameraX, cameraY))
        player.pintar(tela)




main()