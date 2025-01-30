import pygame as pg
from sys import exit

from sys import stdout

from loguru import logger

logger.add(stdout,
           format="{time:DD.MM.YYYY HH:mm:ss} | {level} | {file}:{line} | {message}",
           level="DEBUG")

pg.init()

from classes.classGame import Game

@logger.catch
def main():
    game = Game()
    game.runGame()

if __name__ == '__main__':
    try:
        main()
    finally:
        pg.quit()
        exit()