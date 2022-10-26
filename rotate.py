import time
import rotatescreen

screen = rotatescreen.get_primary_display()
start_orientation = screen.current_orientation
print(start_orientation)

for i in range (1, 10):
    current_orientation = abs((start_orientation - i*90)%360)
    screen.rotate_to(current_orientation)
    time.sleep(0.25)

screen.rotate_to(0)