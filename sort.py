import pygame
import random
pygame.init()

class DrawInfomation:
	black = 0,0,0
	white = 255, 255, 255
	green = 0, 255, 0
	red = 255, 0, 0
	gray = 128, 128, 128
	background_color = white

	def __init__(self, width, height, lst):
		self.width = width
		self.height = height

		self.window = pygame.display.set_mode(pygame.)
