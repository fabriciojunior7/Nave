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
    frames = 60
    frames_passados = 0

    player = nave.Nave(largura, altura)
    gravidade = 0.1

    while(True):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()

            #Teclado
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_SPACE):
                    player.motorLigado = True
                if(event.key == pygame.K_d):
                    player.mover_direita()

            if(event.type == pygame.KEYUP):
                if(event.key == pygame.K_SPACE):
                    player.motorLigado = False

        #Rodar
        relogio.tick(frames)
        pygame.display.update()
        player.cair(gravidade)
        player.colisao(largura, altura)
        if(player.motorLigado == True):
            player.voar()
        #Desenhas
        tela.fill(cinza)
        player.pintar(tela)




main()