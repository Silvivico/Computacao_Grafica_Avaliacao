import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from menu import exibir_menu
from objects import Cubo, Triangulo, Piramide
from controls import controlar_global, controlar_individual, controlar_piramide_direcional
from animation import Animador

# Configurações iniciais do Pygame + OpenGL
def init():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

# Loop de renderização principal
def main():
    init()
    opcao = exibir_menu()

    # Cria objetos
    cubo = Cubo()
    triangulo = Triangulo()
    piramide = Piramide()

    # Posicionamento lado a lado (para as opções combinadas)
    triangulo.x = -3
    cubo.x = 0
    piramide.x = 3

    # Lista de objetos ativos
    objetos = []

    # Animações
    animadores = []

    # Carrega os objetos com base na opção
    if opcao == 1:
        objetos = [cubo]
    elif opcao == 2:
        objetos = [triangulo]
    elif opcao == 3:
        objetos = [cubo, triangulo]
    elif opcao == 4:
        objetos = [piramide]
    elif opcao == 5:
        objetos = [cubo, triangulo, piramide]
    elif opcao == 6:
        objetos = [cubo, triangulo, piramide]
    elif opcao == 7:
        objetos = [cubo, triangulo, piramide]
        animadores = [
            Animador(cubo, 'x', 0.02),
            Animador(triangulo, 'y', 0.015),
            Animador(piramide, 'x', 0.01)
        ]

    clock = pygame.time.Clock()
    rodando = True

    while rodando:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Evento do teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

            elif event.type == pygame.KEYDOWN:
                tecla = pygame.key.name(event.key)

                if opcao in [1, 2, 3, 4, 5]:  # Controles globais
                    controlar_global(tecla, objetos)

                elif opcao == 6:  # Controles individuais
                    controlar_individual(tecla, cubo, triangulo, piramide)

                elif opcao == 6 and event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                    # Para setas (Pygame já traz o nome)
                    direcional = {
                        K_UP: 72,
                        K_DOWN: 80,
                        K_LEFT: 75,
                        K_RIGHT: 77
                    }
                    controlar_piramide_direcional(direcional[event.key], piramide)

        # Atualiza animações se necessário
        if opcao == 7:
            for animador in animadores:
                animador.animar()

        # Desenha os objetos
        for obj in objetos:
            obj.desenhar()

        pygame.display.flip()
        clock.tick(60)  # 60 FPS

    pygame.quit()

if __name__ == "__main__":
    main()
