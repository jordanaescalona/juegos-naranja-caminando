import pgzrun
import random

# Configuración básica
WIDTH = 1200
HEIGHT = 500

# Cargar los sprites para animación de movimiento hacia la derecha y la izquierda
right_sprites = ['right1', 'right2', 'right3', 'right4', 'right5', 'right6', 'right7', 'right8']
left_sprites = ['left1', 'left2', 'left3', 'left4', 'left5', 'left6', 'left7', 'left8']

# Crear el actor del personaje
character = Actor('right1', (400, 200))  # Comienza con el primer sprite hacia la derecha

# Variables para la animación
sprite_index = 0
direction = 'right'  # Dirección inicial del personaje
anim_speed = 5  # Velocidad de animación (cuantos frames tarda en cambiar de sprite)

def update():
    global sprite_index, direction
    
    # Movimiento a la derecha
    if keyboard.right:
        character.x += 5
        direction = 'right'
        sprite_index = (sprite_index + 1) % (len(right_sprites) * anim_speed)
        character.image = right_sprites[sprite_index // anim_speed]  # Cambiar sprite según el índice
        
    # Movimiento a la izquierda
    elif keyboard.left:
        character.x -= 5
        direction = 'left'
        sprite_index = (sprite_index + 1) % (len(left_sprites) * anim_speed)
        character.image = left_sprites[sprite_index // anim_speed]  # Cambiar sprite según el índice
    
    # Si no hay movimiento, mantener el sprite inicial
    else:
        if direction == 'right':
            character.image = 'right1'
        elif direction == 'left':
            character.image = 'left1'

def draw():
    screen.clear()  # Limpiar la pantalla
    character.draw()  # Dibujar el personaje

pgzrun.go()