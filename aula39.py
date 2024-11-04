import pygame

i
import sys

# Inicialização do Pygame
pygame.init()


pygame.

p
# Definições de constantes
WIDTH, HEIGHT = 
WIDTH, HE

WIDTH
600, 600
SQUARE_SIZE = WIDTH // 
SQUARE_SIZE = WIDTH //

SQUARE_SIZE = WIDTH

SQUARE_SIZE = W

SQUARE_

SQU
8
WHITE = (
WHITE = (

WHITE 

WHI
255, 255, 255)
BLACK = (
BLACK = (
0, 0, 0)

# Configuração da tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.se

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.di

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame

screen = pygame.displ

screen = pygame.di

screen = pygame
"Jogo de Xadrez")

# Função para desenhar o tabuleiro

d
def draw_board():
    
    fo

 
for row in range(8):
        
      
for col in range(8):
            
        

    
if (row + col) % 2 == 0:
                pygame.draw.rect(screen, WHITE, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            
                pygame.draw.rect(screen, WHITE, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            el

                pygame.draw.rect(screen, WHITE, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
       

                pygame.draw.rect(screen, WHITE, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUAR

                pygame.draw.rect(screen, WHITE, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE,

                pygame.draw.rect(screen, WHITE, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUAR

                pygame.draw.rect(screen, WHITE, (col * SQUARE_SIZE, row * SQUARE_SIZ

                pygame.draw.rect(screen, WHITE, (col * SQUARE_SIZE, row * SQUA

                pygame.draw.rect(screen, WHITE, (col * SQUARE_SIZE

                pygame.draw.rect(screen, WHITE, (col * SQUAR

                pygame.draw.rect(screen, WHITE, (

                pygame.draw.rect(screen, WHI

                pygame.draw.rect(

                pygame.draw.

                p

            

 
else:
                pygame.draw.rect(screen, BLACK, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


                pygame.draw.rect(screen, BLACK, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

                pygame.draw.rect(screen, BLACK, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_S

                pygame.draw.rect(screen, BLACK, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, S

                pygame.draw.rect(screen, BLACK, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_S

                pygame.draw.rect(screen, BLACK, (col * SQUARE_SIZE, row * SQUARE_SIZ

                pygame.draw.rect(screen, BLACK, (col * SQUARE_SIZE, row * SQUAR

                pygame.draw.rect(screen, BLACK, (col * SQUARE_SIZE, r

                pygame.draw.rect(screen, BLACK, (col * SQUARE_S

                pygame.draw.rect(screen, BLACK, (col 

                pygame.draw.rect(screen, BLACK, (

                pygame.draw.rect(screen, BLA

                pygame.draw.rect(screen,

                pygame.draw.rect(sc

                pygame.draw.r

                pygame.

          

   
# Função principal do jogo

de
def main():
    
  
while True:
        
  
for event in pygame.event.get():
            
   
if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_board()
        pygame.display.flip()


                pygame.quit()
                sys.exit()

        draw_board()
        pygame.display.fli

                pygame.quit()
                sys.exit()

        draw_board()
        pygame.displ

                pygame.quit()
                sys.exit()

        draw_board()
        pygam

                pygame.quit()
                sys.exit()

        draw_board()
       

                pygame.quit()
                sys.exit()

        draw_bo

                pygame.quit()
                sys.exit()

        d

                pygame.quit()
                sys.exit

                pygame.quit()
                s

                pygame.quit()
 

               

       
if __name__ == "__main__":
    main()

    main()
`

    main
