# controls.py

def controlar_global(tecla, objetos):
    tecla = tecla.upper()
    for obj in objetos:
        if tecla == 'W':
            obj.y += 0.1
        elif tecla == 'S':
            obj.y -= 0.1
        elif tecla == 'A':
            obj.x -= 0.1
        elif tecla == 'D':
            obj.x += 0.1
        elif tecla == 'Q':
            obj.rot_x += 5
        elif tecla == 'E':
            obj.rot_x -= 5
        elif tecla == 'R':
            obj.rot_y += 5
        elif tecla == 'F':
            obj.rot_y -= 5
        elif tecla == 'Z':
            obj.zoom += 0.1
        elif tecla == 'X':
            obj.zoom -= 0.1

def controlar_individual(tecla, cubo, triangulo, piramide):
    tecla = tecla.upper()
    
    # Cubo (I, K, J, L)
    if tecla == 'I':
        cubo.y += 0.1
    elif tecla == 'K':
        cubo.y -= 0.1
    elif tecla == 'J':
        cubo.x -= 0.1
    elif tecla == 'L':
        cubo.x += 0.1

    # Triângulo (G, B, V, N)
    elif tecla == 'G':
        triangulo.y += 0.1
    elif tecla == 'B':
        triangulo.y -= 0.1
    elif tecla == 'V':
        triangulo.x -= 0.1
    elif tecla == 'N':
        triangulo.x += 0.1

    # Pirâmide (setas ↑ ↓ ← →)
    elif tecla == b'\xe0':  # Tecla especial (seta)
        pass  # O tratamento exato da tecla depende do sistema

def controlar_piramide_direcional(codigo_tecla, piramide):
    # Em sistemas Windows, as setas são detectadas com códigos especiais:
    #   setas: ↑ = 72, ↓ = 80, ← = 75, → = 77
    if codigo_tecla == 72:       # ↑
        piramide.y += 0.1
    elif codigo_tecla == 80:     # ↓
        piramide.y -= 0.1
    elif codigo_tecla == 75:     # ←
        piramide.x -= 0.1
    elif codigo_tecla == 77:     # →
        piramide.x += 0.1

def rotacao_zoom_global(tecla, objetos):
    tecla = tecla.upper()
    for obj in objetos:
        if tecla == 'Q':
            obj.rot_x += 5
        elif tecla == 'E':
            obj.rot_x -= 5
        elif tecla == 'R':
            obj.rot_y += 5
        elif tecla == 'F':
            obj.rot_y -= 5
        elif tecla == 'Z':
            obj.zoom += 0.1
        elif tecla == 'X':
            obj.zoom -= 0.1
