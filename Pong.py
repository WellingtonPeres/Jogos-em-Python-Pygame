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
		self.directionX = 1#15
		self.directionY = 1#5

	def move(self):
		self.positionX += self.directionX
		self.positionY += self.directionY

	def paddle_collision(self):
		# Invert Direction
		self.directionX = - self.directionX

	def wall_colision(self):
		# Invert Direction
		self.directionY = - self.directionY


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

	def clamp(self):
		if self.positionY <= 0:
			self.positionY = 0

		if self.positionY + self.height >= HEIGHT:
			self.positionY = HEIGHT - self.height


class CollisionManager:
	def between_ball_and_paddle1(self, ball, paddle1):
		if ball.positionY + ball.radius > paddle1.positionY and ball.positionY - ball.radius < paddle1.positionY + paddle1.height:
			if ball.positionX - ball.radius <= paddle1.positionX + paddle1.width:
				return True

		return False

	def between_ball_and_paddle2(self, ball, paddle2):
		if ball.positionY + ball.radius > paddle2.positionY and ball.positionY - ball.radius < paddle2.positionY + paddle2.height:
			if ball.positionX + ball.radius >= paddle2.positionX:
				return True

		return False

	def between_ball_and_walls(self, ball):
		# Top
		if ball.positionY - ball.radius <= 0:
			return True

		# Bottom
		if ball.positionY + ball.radius >= HEIGHT:
			return True

		return False

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
collision = CollisionManager()

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
		# Ball movement
		ball.move()
		ball.show()

		# Paddle1
		paddle1.move()
		paddle1.clamp()
		paddle1.show()

		# Paddle2
		paddle2.move()
		paddle2.clamp()
		paddle2.show()

		# Check for collisions
	if collision.between_ball_and_paddle1(ball, paddle1):
		ball.paddle_collision()

	if collision.between_ball_and_paddle2(ball, paddle2):
		ball.paddle_collision()

	if collision.between_ball_and_walls(ball):
		ball.wall_colision()

	pygame.display.update()
