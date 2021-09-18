import turtle

# Setting up the screen
window = turtle.Screen()
window.title("Classic Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(2)


# Creating class
class Paddle(turtle.Turtle):
    def __init__(self, a, b, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=a, stretch_len=b)
        self.goto(x, y)
        self.speed(1)

    def move_up(self):
        y = self.ycor()
        y += 20
        self.sety(y)
        if self.ycor() > 250:
            self.sety(250)

    def move_down(self):
        y = self.ycor()
        y -= 20
        self.sety(y)
        if self.ycor() < -250:
            self.sety(-250)


# Create object from class
paddle_a = Paddle(5, 1, -350, 0)
paddle_b = Paddle(5, 1, 350, 0)
ball = Paddle(1, 1, 0, 0)
ball.dx = 1
ball.dy = -1

# Setup keybinding
window.listen()
window.onkeypress(paddle_a.move_up, "w")
window.onkeypress(paddle_a.move_down, "s")
window.onkeypress(paddle_b.move_up, "Up")
window.onkeypress(paddle_b.move_down, "Down")

# Score label
score_a = 0
score_b = 0
pen = turtle.Turtle()
pen.penup()
pen.color("white")
pen.shape("square")
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Player A: 0  Player B: 0", align="center", font=("Terminal", 22, "normal"))

# Main game loop
while True:
    window.update()
    # Ball mover
    ball.setx(ball.xcor() + ball.dx/5)
    ball.sety(ball.ycor() + ball.dy/5)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Terminal", 22, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Terminal", 22, "normal"))

    # Paddles collision
    if 350 > ball.xcor() > 340 and paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50:
        ball.setx(340)
        ball.dx *= -1

    if -340 > ball.xcor() > -350 and paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50:
        ball.setx(-340)
        ball.dx *= -1
