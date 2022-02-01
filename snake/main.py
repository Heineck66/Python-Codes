from snake import Snake
from food import Food
from scoreboard import Score
import game

game = game.Game()
snake = Snake()
food = Food()
score = Score()

game.add_listner(snake.up, "Up")
game.add_listner(snake.down, "Down")
game.add_listner(snake.right, "Right")
game.add_listner(snake.left, "Left")


while game.is_on:
    game.update()
    snake.move()

    if snake.head.distance(food) < 15:
        snake.extend()
        snake.change_color(food.get_current_color())
        food.refresh()
        score.increase_score()
        score.update_score()

    if (
        snake.head.xcor() > 290
        or snake.head.xcor() < -290
        or snake.head.ycor() > 290
        or snake.head.ycor() < -290
    ):
        score.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()


game.exit()
