from collections import defaultdict
def switch(room, room_width, room_height, x1, y1, x2, y2, start_x, start_y):
    room[(start_x, start_y)] = 0
    if (room_width > start_x + x1 >= 0):
        if (room_height > start_y + y1 >= 0):
        # grid[(start_x,start_y)] = 0
            switch(room, room_width, room_height, x1, y1, x2, y2, start_x + x1, start_y + y1)
    if (room_width > start_x + x2 >= 0):
        if(room_height > start_y + y2 >= 0):
        # grid[(start_x,start_y)] = 0
            switch(room, room_width, room_height, x1, y1, x2, y2, start_x + x2, start_y + y2)

    # new_status = 0 if status else 1
    # grid[(x,y)] = new_status
    # if x-1 >= 0:
    #     grid[(x-1,y)] = new_status
    #     if y-1 >= 0:
    #         grid[(x-1,y-1)] = new_status
    # return True if grid[(x,y)] == status else False


def num_illuminated(grid_width, grid_height, conn_x1, conn_y1, conn_x2, conn_y2, start_x, start_y):
    grid = defaultdict(int)
    for w in range(grid_width):
        for h in range(grid_height):
            grid[(w,h)] = 1

    switch(grid, grid_width, grid_height, conn_x1, conn_y1, conn_x2, conn_y2, start_x, start_y)
    # print ("Switched Flag = " + str(s_flag))
    return sum(grid.values())


print(num_illuminated(25,25,-1,0,-1,-1,4,2))