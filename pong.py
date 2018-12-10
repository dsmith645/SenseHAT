from sense_hat import SenseHat
sense = SenseHat()
sense.clear()
w = (255,255,255)
bat_y = 4
def draw_bat():
    sense.set_pixel(0, bat_y, w)
    sense.set_pixel(0, bat_y + 1, w)
    sense.set_pixel(0, bat_y - 1, w)
draw_bat()