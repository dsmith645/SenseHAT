from sense_hat import SenseHat
from time import sleep
from random import randint
sense = SenseHat()
sense.clear()
white = (255,255,255)
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
purple = (255,255,0)
cyan = (0,255,255)
bat_y = 4
ball_position = [3,3]
ball_velocity = [1,1]
def draw_bat():
    sense.set_pixel(0, bat_y, white)
    sense.set_pixel(0, bat_y + 1, white)
    sense.set_pixel(0, bat_y - 1, white)

def move_up(event):
    global bat_y
    if event.action == 'pressed' and bat_y > 1:
        bat_y -= 1

def move_down(event):
    global bat_y
    if event.action == 'pressed' and bat_y < 6:
        bat_y += 1

def draw_ball():
    sense.set_pixel(ball_position[0], ball_position[1], blue)
    ball_position[0] += ball_velocity[0]
    if ball_position[0] == 7 or ball_position[0] == 0:
        ball_velocity[0] = -ball_velocity[0]
    ball_position[1] += ball_velocity[1]
    if ball_position[1] == 7 or ball_position[1] ==0:
        ball_velocity[1] = -ball_velocity[1]
    if ball_position[0] == 1 and (bat_y - 1) <= ball_position[1] <= (bat_y + 1):
        ball_velocity[0] = -ball_velocity[0]

while True:
    sense.clear(0, 0, 0)
    draw_bat()
    draw_ball()
    sleep(0.25)
    sense.stick.direction_up= move_up
    sense.stick.direction_down = move_down
    if ball_position[0] == 0:
        sleep(1)
        sense.set_pixel(ball_position[0], ball_position[1], blue)
        sense.clear(red)
        sleep(0.25)
        sense.clear()
        sleep(0.25)
        sense.clear(red)
        sleep(0.25)
        sense.clear()
        sleep(0.25)
        sense.clear(red)
        sleep(0.25)
        sense.clear()
        sleep(0.25)
        sense.show_message('You Lose!', scroll_speed = 0.05)
        sense.clear()
        break;