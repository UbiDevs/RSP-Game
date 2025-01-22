import pygame as pg
from sys import exit

pg.init()

from classes.classGame import Game

if __name__ == '__main__':
    try:
        game = Game()
        game.runGame()
    finally:
        pg.quit()
        exit()