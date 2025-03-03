#FAÇA UM PROGRAMA EM PYTHON QUE ABRA E REPRODUZA O ÁUDIO DE UM ARQUIVO MP3
import pygame
pygame.init()
pygame.mixer.music.load('C:/Users/thais/Desktop/Python_Curso/desafios/desafio021m/Robocop Gay.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input()