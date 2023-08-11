""" DESAFIO 021: Faça um programa em Python que abra e reproduza o áudio de um arquivo mp3.
 *TOCANDO UM MP3*
"""

import pygame
pygame.init()
pygame.mixer.music.load('desafio021.mp3')
pygame.mixer.music.play()
pygame.event.wait()


