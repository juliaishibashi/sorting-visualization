import pygame
import math 
import random
pygame.init()

class DrawInfomation:
	@staticmethod
	def hex_to_rgb(hex_color):
		hex_color = hex_color.lstrip('#')
		return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

	def __init__(self, width, height, lst):
		self.width = width
		self.height = height

		self.window = pygame.display.set_mode((width, height))
		pygame.display.set_caption("Sorting Algorithm Visualization")

		self.black = self.hex_to_rgb("#344155")
		self.green = self.hex_to_rgb("#81BF97")
		self.yellow = self.hex_to_rgb("#F0DD5D")
		self.white = self.hex_to_rgb("#FFFFFF")
		self.red = self.hex_to_rgb("#DF6756")
		self.background_color = self.white

		self.yellows = [self.hex_to_rgb("#C9BB8E"), self.hex_to_rgb("#FAE29C"), self.hex_to_rgb("#E7C27D")]

		self.font = pygame.font.SysFont('Courier New', 20)
		self.large_font = pygame.font.SysFont('Courier New', 30)

		self.side_pad = 100
		self.top_pad = 150

		self.set_list(lst)

	def set_list(self, lst):
		self.lst = lst
		self.min_val = min(lst)
		self.max_val = max(lst)

		self.block_width = round((self.width - self.side_pad) / len(lst))
		self.block_height = math.floor((self.height - self.top_pad) / (self.max_val - self.min_val))
		self.start_x = self.side_pad // 2 

def draw(draw_info, algo_name, ascending):
	draw_info.window.fill(draw_info.background_color)

	title = draw_info.large_font.render(f"{algo_name} - {'Ascending' if ascending else 'Descending'}", 1, draw_info.black)
	draw_info.window.blit(title, (draw_info.width/2 - title.get_width()/2, 5))

	annotation = draw_info.font.render("Press a key to choose the sorting algorithm", 1, draw_info.black)
	draw_info.window.blit(annotation, (draw_info.width/2 - annotation.get_width()/2, 45))

	sorting = draw_info.font.render("I - Insertion Sort | B - Bubble Sort", 1, draw_info.black)
	draw_info.window.blit(sorting, (draw_info.width/2 - sorting.get_width()/2, 70))

	controles = draw_info.font.render("R - Reset | SPACE - Start Sorting | A - Ascending | D - Descending", 1, draw_info.black)
	draw_info.window.blit(controles, (draw_info.width/2 - controles.get_width()/2, 90))

	draw_list(draw_info)
	pygame.display.update()

def draw_list(draw_info, color_pos={}, clear_bg=False):
	lst = draw_info.lst

	if clear_bg:
		clear_rect = (draw_info.side_pad//2, draw_info.top_pad, draw_info.width - draw_info.side_pad, draw_info.height - draw_info.top_pad)
		pygame.draw.rect(draw_info.window, draw_info.background_color, clear_rect)

	for i, val in enumerate(lst):
		x = draw_info.start_x + i * draw_info.block_width
		y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height

		color = draw_info.yellows[i % len(draw_info.yellows)] #every single gradient we reset. 

		if i in color_pos:
			color = color_pos[i]

		pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.height)) #how far down to draw the block

	if clear_bg:
		pygame.display.update()

# n is the number of elements in the list
# min_val is the minimum value of the elements in the list
# max_val is the maximum value of the elements in the list
def generate_starting_list(n, min_val, max_val):
	lst = []

	for _ in range(n):
		val = random.randint(min_val, max_val)
		lst.append(val)

	return lst

def bubble_sort(draw_info, ascending=True):
	lst = draw_info.lst

	for i in range(len(lst) - 1):
		for j in range(len(lst) - 1 - i):
			num1 = lst[j]
			num2 = lst[j+1]

			if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
				lst[j], lst[j+1] = lst[j+1], lst[j] #swap
				draw_list(draw_info, {j:draw_info.green, j+1:draw_info.red}, True)
				yield True #generate a value
	return lst

def insertion_sort(draw_info, ascending=True):
	lst = draw_info.lst

	for i in range(1, len(lst)):
		current = lst[i]

		while True:
			ascending_sort = i > 0 and lst[i - 1] > current and ascending
			descending_sort = i > 0 and lst[i - 1] < current and not ascending

			if not ascending_sort and not descending_sort:
				break

			lst[i] = lst[i - 1]
			i = i - 1
			lst[i] = current
			draw_list(draw_info, {i - 1: draw_info.green, i: draw_info.red}, True)
			yield True
	return lst

def main():
	run = True
	clock = pygame.time.Clock()

	n = 50
	min_val = 0
	max_val = 100

	lst = generate_starting_list(n, min_val, max_val)
	draw_info = DrawInfomation(800, 600, lst)
	sorting = False
	ascending = True

	sorting_algorithm = insertion_sort
	sorting_algorithm_name = "Insertion Sort"
	sorting_algorithm_gen = None

	while run:
		clock.tick(20)

		if sorting:
			try:
					next(sorting_algorithm_gen)
			except StopIteration:
					sorting = False
		else:
				draw(draw_info, sorting_algorithm_name, ascending)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if event.type != pygame.KEYDOWN:
				continue

			if event.key == pygame.K_r:
				#reset the list
				lst = generate_starting_list(n, min_val, max_val)
				draw_info.set_list(lst)
				sorting = False

			elif event.key == pygame.K_SPACE and sorting == False:
				#sort the list
				sorting = True
				sorting_algorithm_gen = sorting_algorithm(draw_info, ascending)

			elif event.key == pygame.K_a and sorting == False:
				ascending = True

			elif event.key == pygame.K_d and sorting == False:
				ascending = False
			
			elif event.key == pygame.K_i and sorting == False:
				sorting_algorithm = insertion_sort
				sorting_algorithm_name = "Insertion Sort"

			elif event.key == pygame.K_b and sorting == False:
				sorting_algorithm = bubble_sort
				sorting_algorithm_name = "Bubble Sort"

	pygame.quit()

if __name__ == "__main__":
	main()