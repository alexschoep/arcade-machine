


def get_blended_colors_list(start, target, steps): # Tuple value for start, tuple value for a target, steps to blend
    colors = []

    # Determine the differences on the RGB channels to blend to the target value
    red_dif = target[0] - start[0]
    red_step = red_dif / steps
    green_dif = target[1] - start[1]
    green_step = green_dif / steps
    blue_dif = target[2] - start[2]
    blue_step = blue_dif / steps

    for i in range(0, (steps + 1)): # Create RGB values for each step with the last being the target value
        rgb_val = ((start[0] + int(red_step * i)),
                   (start[1] + int(green_step * i)),
                   (start[2] + int(blue_step * i)))
        colors.append(rgb_val)
    return colors # return a list of tuples

if __name__ == "__main__":
    pass