
def blender_list(start, target):
    colors = []
    STEPS = 8

    red_dif = target[0] - start[0]
    red_step = red_dif / STEPS
    green_dif = target[1] - start[1]
    green_step = green_dif / STEPS
    blue_dif = target[2] - start[2]
    blue_step = blue_dif / STEPS

    for i in range(0, (STEPS + 1)):
        rgb_val = ((start[0] + int(red_step * i)),
                   (start[1] + int(green_step * i)),
                   (start[2] + int(blue_step * i)))
        colors.append(rgb_val)
    return colors

if __name__ == "__main__":
    pass