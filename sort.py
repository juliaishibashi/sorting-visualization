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

	side_pad = 100
	top_pad = 100

	def __init__(self, width, height, lst):
		self.width = width
		self.height = height

		self.window = pygame.display.set_mode((width, height))

		pygame.display.set_caption("Sorting Algorithm and Visualisation")
 
		self.set_list(lst)

	def set_list(self, lst):
		self.lst = lst
		self.min_val = min(lst)
		self.max_val = max(lst)

		self.block_width = round((self.width - self.side_pad) / len(lst))
		self.block_height = round((self.height - self.top_pad) / (self.max_val - self.min_val))
		self.start_x = self.side_pad // 2 

def generate_starting_list(n, min_val, max_val):
	lst = []

	for _ in range(n):
		val = random.randint(min_val, max_val)
		lst.append(val)

	return lst

def main():
	run = True
	clock = pygame.time.Clock()

	n = 50
	min_val = 0
	max_val = 100

	lst = generate_starting_list(n, min_val, max_val)
	draw_info = DrawInfomation(800, 600, lst)

	while run:
		clock.tick(60)

		pygame.display.update()

		for event in pygame.event.get():
			if event == pygame.QUIT:
				run = False
	pygame.quite()

if __name__ == "__main__":
	main()
