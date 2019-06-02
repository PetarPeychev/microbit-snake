from microbit import *
import random as r

INTRO = "SNAKE"
SCORE = "SCORE:"
COUNTDOWN = ["3", "2", "1"]
START_POS = (2, 4)
START_DELAY = 1000
MIN_DELAY = 500

def countdown():
    for i in COUNTDOWN:
        display.show(i)
        sleep(1000)
    
def gameloop():
    score = 1
    snake = [START_POS]
    direction = 0
    delay = START_DELAY
    running = True
    food = (1, 1)
    
    while running:
        # Input
        direction = (direction + 4 - button_a.get_presses()) % 4
        direction = (direction + button_b.get_presses()) % 4
        
        # Update
        x, y = snake[0]
        
        if (direction == 0):
            if (y != 0):
                snake.insert(0, (x, y - 1))
            else:
                snake.insert(0, (x, 4))
        elif (direction == 1):
            if (x != 4):
                snake.insert(0, (x + 1, y))
            else:
                snake.insert(0, (0, y))
        elif (direction == 2):
            if (y != 4):
                snake.insert(0, (x, y + 1))
            else:
                snake.insert(0, (x, 0))
        elif (direction == 3):
            if (x != 0):
                snake.insert(0, (x - 1, y))
            else:
                snake.insert(0, (4, y))
            
        # Feeding Check
        if (food == (x, y)):
            score += 1
            food = (r.randrange(5), r.randrange(5))
          
            if (delay >= MIN_DELAY):
                delay = delay - 50
        else:
            snake.pop()
          
        # Collision Check
        for point in snake[1:]:
            if (point == snake[0]):
                running = False
        
        # Display
        display.clear()
        for point in snake:
            display.set_pixel(point[0], point[1], 9)
            
        display.set_pixel(food[0], food[1], 9)
            
        # Tick
        sleep(delay)
    
    return score

display.scroll(INTRO)
    
countdown()

final_score = gameloop()

display.scroll(SCORE)

display.show(str(final_score))
