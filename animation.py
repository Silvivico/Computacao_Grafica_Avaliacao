# animation.py

class Animador:
    def __init__(self, objeto, direcao='x', velocidade=0.02, limite=2.5):
        self.objeto = objeto
        self.direcao = direcao  # 'x' ou 'y'
        self.velocidade = velocidade
        self.limite = limite

    def animar(self):
        if self.direcao == 'x':
            self.objeto.x += self.velocidade
            if abs(self.objeto.x) >= self.limite:
                self.velocidade *= -1
        elif self.direcao == 'y':
            self.objeto.y += self.velocidade
            if abs(self.objeto.y) >= self.limite:
                self.velocidade *= -1

        # Gira também:
        self.objeto.rot_x += 1
        self.objeto.rot_y += 1
