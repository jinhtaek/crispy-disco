import pygame, random, sys

pygame.init()
cell = 20
width = height = 20 * cell
win = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

snake = [(10, 10)]
direction = (1, 0)
apple = (random.randint(0, 19), random.randint(0, 19))

def draw():
    win.fill((0,0,0))
    for s in snake:
        pygame.draw.rect(win, (0,255,0), pygame.Rect(s[0]*cell, s[1]*cell, cell, cell))
    pygame.draw.rect(win, (255,0,0), pygame.Rect(apple[0]*cell, apple[1]*cell, cell, cell))
    pygame.display.update()

def move():
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    if head in snake or not (0 <= head[0] < 20) or not (0 <= head[1] < 20):
        pygame.quit()
        sys.exit()
    snake.insert(0, head)
    if head == apple:
        return True
    else:
        snake.pop()
        return False

def new_apple():
    while True:
        a = (random.randint(0, 19), random.randint(0, 19))
        if a not in snake:
            return a

while True:
    clock.tick(10)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != (0,1): direction = (0,-1)
    if keys[pygame.K_DOWN] and direction != (0,-1): direction = (0,1)
    if keys[pygame.K_LEFT] and direction != (1,0): direction = (-1,0)
    if keys[pygame.K_RIGHT] and direction != (-1,0): direction = (1,0)

    if move():
        apple = new_apple()
    draw()