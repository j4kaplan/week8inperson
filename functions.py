import arcade

def create_shapes(win_width, win_height):
    x_scale = win_width/4
    win_height = win_height/4
    shape_list=[]
    rectangle = arcade.create_rectangle(x_scale,win_height,100,win_height,arcade.color.COPPER_PENNY)
    circle= arcade.create_ellipse(x_scale * 3 ,win_height,50,50,arcade.color.DARK_TANGERINE)
    shape_list.append(rectangle)
    shape_list.append(circle)
    line= arcade.create_line(x_scale,600,x_scale * 3,win_height,arcade.color.ENGLISH_LAVENDER,3)
    shape_list.append(line)
    return shape_list


def create_more_shapes (existing_shapes):
    list_of_points =[(400,650),(350,600),(450,600)]
    triangle= arcade.create_polygon(list_of_points,arcade.color.NAPIER_GREEN)
    existing_shapes.append(triangle)

def main():
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 700
    arcade.open_window(WINDOW_WIDTH,WINDOW_HEIGHT,"Functions Demo")
    shapes_to_draw = create_shapes(WINDOW_WIDTH, WINDOW_HEIGHT)
    create_more_shapes(shapes_to_draw)
    print (f"WINDOW_HEIGHT is {WINDOW_HEIGHT}")
    arcade.start_render()
    for shape in shapes_to_draw:
        shape.draw()


    arcade.finish_render()
    arcade.run()



main()


