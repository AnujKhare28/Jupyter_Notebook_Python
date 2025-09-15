import turtle
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'yellow', 'blue', 'orange', 'brown', 'cyan', 'black', 'purple', 'pink']

def get_number_of_racers():
    while True:
        racers = int(input("Enter number of racers (2 - 10): "))
        if 2 <= racers <= 10:
            return racers
        print("Number of racers must be between 2 and 10 ")

def race(colors):
    turtles = create_turtle(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)
            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                winner = colors[turtles.index(racer)]
                print(f'The winner is {winner} turtle !!')

                turtle.bye() 
                return

def create_turtle(colors):
    turtles = []
    spacing_x = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i+1) * spacing_x, -HEIGHT // 2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing")

    
    canvas = screen.getcanvas()
    root = canvas.winfo_toplevel()
    root.lift()
    root.attributes('-topmost', True)
    root.after_idle(root.attributes, '-topmost', False)

    return screen

racers = get_number_of_racers()
screen = init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]

race(colors)