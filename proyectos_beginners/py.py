import pygame
# Initialize Pygame
pygame.init()

# Create a window
window = pygame.display.set_mode((640, 480))

# Create a rectangle for the racket
racket = pygame.Rect(100, 200, 100, 20)
# Create a ball object
ball = pygame.Rect(320, 240, 10, 10)
ball.speed = (5,5)
# Create a game loop
while True:
    # Update the position of the ball and the rackets
    ball.x += ball.velocity[0]
    ball.y += ball.velocity[1]
    if ball.x < 0 or ball.x > 640:
        ball.velocity[0] *= -1
    if ball.y < 0 or ball.y > 480:
        ball.velocity[1] *= -1
    if ball.colliderect(racket):
        ball.velocity[1] *= -1
    # Check for collisions with the walls
    if ball.x < 0 or ball.x > 640:
        ball.x = 0
        ball.x = 640
    if ball.y < 0 or ball.y > 480:
        ball.y = 0
        ball.y = 480
    # Draw the ball and the rackets
    pygame.draw.rect(window, (255, 255, 255), racket)
    pygame.draw.rect(window, (255, 0, 0), ball)
  
    # Check if the ball hit the paddles.
    if ball.y < 0 or ball.y > 600:
        # Reverse the ball's y-direction.
        ball_speed[1] *= -1
    # Check if the ball scored a point.
    if ball.x < 0:
        # Left player scored a point.
        left_score += 1
        ball.x = 400
        ball.y = 300
        ball.speed = [5, 5]
    elif ball.x > 800:
        # Right player scored a point.
        right_score += 1
        ball.x = 400
        ball.y = 300
        ball_speed = [5, 5]
    # Draw the paddles and the ball.
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), left_paddle)
    pygame.draw.rect(screen, (255, 255, 255), right_paddle)
    pygame.draw.rect(screen, (255, 0, 0), ball)
    # Update the display.
    pygame.display.flip()