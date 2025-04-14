# objects.py

from OpenGL.GL import *
from OpenGL.GLU import *
import math

class ObjetoBase:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = -5
        self.rot_x = 0
        self.rot_y = 0
        self.zoom = 1.0

    def aplicar_transformacoes(self):
        glTranslatef(self.x, self.y, self.z)
        glRotatef(self.rot_x, 1, 0, 0)
        glRotatef(self.rot_y, 0, 1, 0)
        glScalef(self.zoom, self.zoom, self.zoom)

# ===================================
# CUBO
# ===================================
class Cubo(ObjetoBase):
    def desenhar(self):
        glPushMatrix()
        self.aplicar_transformacoes()

        glBegin(GL_QUADS)
        # Face frontal
        glColor3f(1, 0, 0)
        glVertex3f(-1, -1,  1)
        glVertex3f( 1, -1,  1)
        glVertex3f( 1,  1,  1)
        glVertex3f(-1,  1,  1)

        # Face traseira
        glColor3f(0, 1, 0)
        glVertex3f(-1, -1, -1)
        glVertex3f(-1,  1, -1)
        glVertex3f( 1,  1, -1)
        glVertex3f( 1, -1, -1)

        # Face superior
        glColor3f(0, 0, 1)
        glVertex3f(-1,  1, -1)
        glVertex3f(-1,  1,  1)
        glVertex3f( 1,  1,  1)
        glVertex3f( 1,  1, -1)

        # Face inferior
        glColor3f(1, 1, 0)
        glVertex3f(-1, -1, -1)
        glVertex3f( 1, -1, -1)
        glVertex3f( 1, -1,  1)
        glVertex3f(-1, -1,  1)

        # Face direita
        glColor3f(1, 0, 1)
        glVertex3f( 1, -1, -1)
        glVertex3f( 1,  1, -1)
        glVertex3f( 1,  1,  1)
        glVertex3f( 1, -1,  1)

        # Face esquerda
        glColor3f(0, 1, 1)
        glVertex3f(-1, -1, -1)
        glVertex3f(-1, -1,  1)
        glVertex3f(-1,  1,  1)
        glVertex3f(-1,  1, -1)
        glEnd()
        glPopMatrix()

# ===================================
# TRIÂNGULO
# ===================================
class Triangulo(ObjetoBase):
    def desenhar(self):
        glPushMatrix()
        self.aplicar_transformacoes()
        glBegin(GL_TRIANGLES)
        glColor3f(1.0, 0.5, 0.0)
        glVertex2f(-1.0, -1.0)
        glVertex2f(1.0, -1.0)
        glVertex2f(0.0, 1.0)
        glEnd()
        glPopMatrix()

# ===================================
# PIRÂMIDE
# ===================================
class Piramide(ObjetoBase):
    def desenhar(self):
        glPushMatrix()
        self.aplicar_transformacoes()

        glBegin(GL_TRIANGLES)
        # Face frontal
        glColor3f(1, 0, 0)
        glVertex3f( 0.0,  1.0, 0.0)
        glVertex3f(-1.0, -1.0, 1.0)
        glVertex3f( 1.0, -1.0, 1.0)

        # Face direita
        glColor3f(0, 1, 0)
        glVertex3f( 0.0,  1.0, 0.0)
        glVertex3f( 1.0, -1.0, 1.0)
        glVertex3f( 1.0, -1.0, -1.0)

        # Face traseira
        glColor3f(0, 0, 1)
        glVertex3f( 0.0,  1.0, 0.0)
        glVertex3f( 1.0, -1.0, -1.0)
        glVertex3f(-1.0, -1.0, -1.0)

        # Face esquerda
        glColor3f(1, 1, 0)
        glVertex3f( 0.0,  1.0, 0.0)
        glVertex3f(-1.0, -1.0, -1.0)
        glVertex3f(-1.0, -1.0, 1.0)
        glEnd()

        # Base (quadrado)
        glBegin(GL_QUADS)
        glColor3f(0, 1, 1)
        glVertex3f(-1.0, -1.0,  1.0)
        glVertex3f( 1.0, -1.0,  1.0)
        glVertex3f( 1.0, -1.0, -1.0)
        glVertex3f(-1.0, -1.0, -1.0)
        glEnd()

        glPopMatrix()
