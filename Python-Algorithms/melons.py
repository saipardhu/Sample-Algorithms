def melon_count(boxes, melons):
    max_placed = 0
    start_pos = 0
    for index in range(len(melons)):
        melon_index = index
        melons_placed = 0
        box_index = 0
        while box_index < len(boxes) and melon_index < len(melons):
            if boxes[box_index] >= melons[melon_index]:
                melons_placed += 1
                melon_index += 1
            box_index += 1

        if max_placed <= melons_placed:
            max_placed = melons_placed
            start_pos = index
    return max_placed, start_pos