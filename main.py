import sys
import pygame
import random
from pygame.locals import *


class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y


window_width = 600
window_height = 500

window = pygame.display.set_mode((window_width, window_height))
fps = 30
img_files = {
    "pipe": "images/pipe.png",
    "background": "images/background.jpg",
    "player": "images/player.png",
}
game_imgs = {}
fps_clck = pygame.time.Clock()
player_pos = Pos(window_width / 5, window_height / 2)


def initGame():
    pygame.init()

    pygame.display.set_caption("Joseph's Amazing Game")

    for name, file in img_files.items():
        game_imgs[name] = pygame.image.load(file)


def createPipe():
    mid = window_height / 3
    height = game_imgs["pipe"].get_height()

    offset = random.randrange(0, int(window_height / 5))
    pipe_x = window_width + 10
    lower_pipe_y = mid + offset
    upper_pipe_y = height - offset
    pipe = [{"x": pipe_x, "y": -upper_pipe_y}, {"x": pipe_x, "y": lower_pipe_y}]
    return pipe


def isGameOver(up_pipes, down_pipes):
    # Check if player has left bounds
    if player_pos.y > window_height or player_pos.y < 0:
        return True

    # Pipe characteristics
    height = game_imgs["pipe"].get_height()
    width = game_imgs["pipe"].get_width()

    # Check for upper pipe collision
    for pipe in up_pipes:
        y_collision = player_pos.y < height + pipe["y"]
        x_collision = abs(player_pos.x - pipe["x"]) < width
        if y_collision and x_collision:
            return True

    # Check for lower pipe collision
    for pipe in down_pipes:
        y_collision = player_pos.y + height > pipe["y"]
        x_collision = abs(player_pos.x - pipe["x"]) < width
        if y_collision and x_collision:
            return True

    # Nothing matched, return false
    return False

def isQuitGameInput(event):
    return event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE)

def isRunGameInput(event):
    return event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP)

def quitGame():
    pygame.quit()
    sys.exit()


def runFlappy():
    score = 0
    first_pipe = createPipe()
    second_pipe = createPipe()
    inital_pipe_x = window_width + 200

    up_pipes = [first_pipe[0], second_pipe[0]]
    down_pipes = [first_pipe[1], second_pipe[1]]

    for pipe in up_pipes + down_pipes:
        pipe['x'] = inital_pipe_x
    
    # print(up_pipes)
    # print(down_pipes)

    # How fast the pipe moves along the x-axis    
    pipe_vel_x = -4
    # How fast the bird moves along the x and y axises
    bird_vel_y = -9
    bird_max_vel_y = 10 # While falling
    bird_min_vel_y = -8 # While flaping
    bird_flap_vel = bird_min_vel_y
    bird_accl_y = 1 # Gravity

    bird_flapped = False
    while True:
        for event in pygame.event.get():
            if isQuitGameInput(event):
                quitGame()
            elif isRunGameInput(event):
                if player_pos.y > 0:
                    bird_vel_y = bird_flap_vel
                    bird_flapped = True

        print("hi")

        if isGameOver(up_pipes, down_pipes):
            return
            
  

def processStartInputs():
    for event in pygame.event.get():
        if isQuitGameInput(event):
            quitGame
        elif isRunGameInput(event):
            runFlappy()


def startGame():
    while True:
        window.blit(game_imgs["background"], (0, 0))
        window.blit(game_imgs["player"], (player_pos.x, player_pos.y))
        pygame.display.update()
        fps_clck.tick(fps)
        # window.blit(game_imgs["base"], (0, 100))
        while True:
            processStartInputs()


# "main" function (prevents code from being run when importing)
if __name__ == "__main__":
    initGame()
    startGame()
