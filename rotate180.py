import rotatescreen

screen = rotatescreen.get_primary_display()
start_orientation = screen.current_orientation
screen.rotate_to((abs(start_orientation + 180))%360)  # rotate 180 degrees only