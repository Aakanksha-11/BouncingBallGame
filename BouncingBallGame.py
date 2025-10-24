from graphics import Canvas
import time

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 25
DELAY = 0.01
bounce = 3
obstacle_speed = 3

#things to do:
#>create a ball
#>add obstacles
#>make them move
#>dodge obstacles


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    ball_left = CANVAS_WIDTH // 6
    ball_top = CANVAS_HEIGHT - SIZE
    ball_right = ball_left + SIZE
    ball_bottom = ball_top + SIZE
    ball = canvas.create_oval(ball_left, ball_top, ball_right, ball_bottom, "red")
    
    #create obstacle1
    obstacle1_left = CANVAS_WIDTH - SIZE
    obstacle1_top = CANVAS_HEIGHT - SIZE
    obstacle1_right = CANVAS_WIDTH
    obstacle1_bottom = CANVAS_HEIGHT
    obstacle1 = canvas.create_rectangle(obstacle1_left, obstacle1_top, obstacle1_right, obstacle1_bottom)
    
    #create obstacle2
    obstacle2_left = CANVAS_WIDTH - SIZE - (CANVAS_WIDTH // 2)
    obstacle2_top = CANVAS_HEIGHT - SIZE
    obstacle2_right = CANVAS_WIDTH - (CANVAS_WIDTH // 2)
    obstacle2_bottom = CANVAS_HEIGHT
    obstacle2 = canvas.create_rectangle(obstacle2_left, obstacle2_top, obstacle2_right, obstacle2_bottom)

    current_direction = "down"
    height = CANVAS_HEIGHT - 100
    game_over = False
    score = 0
    
    text = canvas.create_text(40,40,font_size=35, text = 'Bouncing Ball Game')
    ball_moving_up = False           
    while True:
       
        # Handle key press
        key = canvas.get_last_key_press()
        if key == "ArrowUp" and current_direction == "down":
            current_direction = "up"
            print('up arrow pressed!')

        if current_direction == "up":
            if ball_top > height:
                ball_top -= bounce
                ball_bottom -= bounce
            else:
                current_direction = "down"
       
        if current_direction == "down":
            if ball_bottom < CANVAS_HEIGHT:
                ball_top += bounce
                ball_bottom += bounce

        canvas.moveto(ball, ball_left, ball_top)

        # Move obstacle 1
        obstacle1_left -= obstacle_speed
        canvas.moveto(obstacle1, obstacle1_left, obstacle1_top)

        # Move obstacle 2
        obstacle2_left -= obstacle_speed
        canvas.moveto(obstacle2, obstacle2_left, obstacle2_top)

        # Check collision with obstacle 1
        if (
            ball_right > obstacle1_left
            and ball_left < obstacle1_left + SIZE
            and ball_bottom > obstacle1_top
            and ball_top < obstacle1_top + SIZE
        ):
            game_over = True
            break

        # Check collision with obstacle 2
        if (
            ball_right > obstacle2_left
            and ball_left < obstacle2_left + SIZE
            and ball_bottom > obstacle2_top
            and ball_top < obstacle2_top + SIZE
        ):
            game_over = True
            break
        
        #when the obstacles disappears and the ball dodges the obstacle, increment score by 1
        if obstacle1_left + SIZE < 0:
            score += 1
            obstacle1_left = CANVAS_WIDTH
            canvas.moveto(obstacle1, obstacle1_left, obstacle1_top)
            #print(score)

        if obstacle2_left + SIZE < 0:
            score += 1
            obstacle2_left = CANVAS_WIDTH
            canvas.moveto(obstacle2, obstacle2_left, obstacle2_top)
            #print(score)

        time.sleep(DELAY)

    print("Score:", score)
    print("game over")
    text = canvas.create_text(130, 180, font_size=20, text='Game Over!')
    text = canvas.create_text(150, 200, font_size=20, text='Score:'+str(score))


if __name__ == '__main__':
    main()







