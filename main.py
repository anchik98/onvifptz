import ptz_control

if __name__ == '__main__':

    #Do all setup initializations
    ptz = ptz_control.ptzcam()

#*****************************************************************************
# IP camera motion tests
#*****************************************************************************
    print 'Starting tests...'

    #Set preset
    ptz.move_pan(1.0, 1)  #move to a new home position
    ptz.set_preset('home')

    # move right -- (velocity, duration of move)
    ptz.move_pan(1.0, 2)

    # move left
    ptz.move_pan(-1.0, 2)

    # move down
    ptz.move_tilt(-1.0, 2)

    # Move up
    ptz.move_tilt(1.0, 2)

    # zoom in
    ptz.zoom(1.0, 2)

    # zoom out
    ptz.zoom(-0.3, 1)

    #Get presets
    ptz.get_preset()
    #Go back to preset
    ptz.goto_preset('home')

    exit()