import pygame
import random
pygame.init()

class DrawInfomation:
	black = 0,0,0
	white = 255, 255, 255
	green = 0, 255, 0
	red = 255, 0, 0
	background_color = white

	gradients = [(128, 128, 128), (160, 160, 160), (192, 192, 192)]


	font = pygame.font.SysFont('comicsans', 30)
	large_font = pygame.font.SysFont('comicsans', 40)

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

def draw(draw_info):
	draw_info.window.fill(draw_info.background_color)

	controles = draw_info.font.render("Press 'r' to reset, 'space' to sort, 'a' to sort accending, 'd' to sort decending", 1, draw_info.black)
	draw_info.window.blit(controles, (draw_info.width/2 - controles.get_width()/2, 5))

	sorting = draw_info.font.render("Press 'i' for insertion sort, 'b' for bubble sort", 1, draw_info.black)
	draw_info.window.blit(sorting, (draw_info.width/2 - sorting.get_width()/2, 35))

	draw_list(draw_info)
	pygame.display.update()

def draw_list(draw_info, color_pos={}):
	lst = draw_info.lst

	for i, val in enumerate(lst):
		x = draw_info.start_x + i * draw_info.block_width
		y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height

		color = draw_info.gradients[i % len(draw_info.gradients)] #every single gradient we reset. 

		if i in color_pos:
			color = draw_info.gradients[color_pos[i] % len(draw_info.gradients)]

		pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.height)) #how far down to draw the block

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
		for j in range(len(lst) - i - 1):
			num1 = lst[j]
			num2 = lst[j+1]

			if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
				lst[j], lst[j+1] = lst[j+1], lst[j] #swap
				#draw()
				yield True #generate a value
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

	while run:
		clock.tick(60)
		draw(draw_info)
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

			elif event.key == pygame.K_a and sorting == False:
				ascending = True
			elif event.key == pygame.K_d and sorting == False:
				ascending = False

	pygame.quit()

if __name__ == "__main__":
	main()