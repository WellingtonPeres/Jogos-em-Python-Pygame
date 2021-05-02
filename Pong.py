import pygame, sys


class Ball:
	def __init__(self, screen, color, positionX, positionY, radius):
		self.screen = screen
		self.color = color
		self.positionX = positionX
		self.positionY = positionY
		self.radius = radius
		self.directionX = 0
		self.directionY = 0
		self.show()

	def show(self):
		pygame.draw.circle(self.screen, self.color, (self.positionX, self.positionY), self.radius)

	def start_moving(self):
		self.directionX = 15
		self.directionY = 5

	def move(self):
		self.positionX += self.directionX
		self.positionY += self.directionY


class Paddle:
	def __init__(self, screen, color, positionX, positionY, width, height):
		self.screen = screen
		self.color = color
		self.positionX = positionX
		self.positionY = positionY
		self.width = width
		self.height = height
		self.state = "stopped"
		self.show()

	def show(self):
		pygame.draw.rect(self.screen, self.color, (self.positionX, self.positionY, self.width, self.height))

	def move(self):
		if self.state == "up":
			self.positionY -= 10
		elif self.state == "down":
			self.positionY += 10


pygame.init()

WIDTH = 900
HEIGHT = 500
# rgb - red, green, blue
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PONG")


def paint_back():
	screen.fill(BLACK)
	pygame.draw.line(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT), 5)


paint_back()

# OBJECTS
ball = Ball(screen, WHITE, WIDTH//2, HEIGHT//2, 15)
paddle1 = Paddle(screen, WHITE, 15, HEIGHT//2 - 60, 20, 120)
paddle2 = Paddle(screen, WHITE, WIDTH - 20 - 15, HEIGHT//2 - 60, 20, 120)

# VARIABLES
playing = False

# Mainloop
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_p:
				ball.start_moving()
				playing = True

			if event.key == pygame.K_w:
				paddle1.state = "up"
			if event.key == pygame.K_s:
				paddle1.state = "down"

			if event.key == pygame.K_UP:
				paddle2.state = "up"
			if event.key == pygame.K_DOWN:
				paddle2.state = "down"

		if event.type == pygame.KEYUP:
			paddle1.state = "stopped"
			paddle2.state = "stopped"

	if playing:
		paint_back()
		# ball movement
		ball.move()
		ball.show()

		paddle1.move()
		paddle1.show()

		paddle2.move()
		paddle2.show()

	pygame.display.update()
