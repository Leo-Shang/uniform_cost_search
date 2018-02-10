from queue import PriorityQueue


def path_find(n, start_loc, goal_loc, values):
    visited_square = []
    fringe = PriorityQueue()
    fringe.put((0, [start_loc]))
    while not fringe.empty():
        cumulative_cost, path = fringe.get()
        current_position = path[-1]
        if current_position == goal_loc:  # reached goal state
            return path
        elif current_position not in visited_square:
            visited_square.append(current_position)  # put this square into explored list
            target_row = current_position[0]
            target_col = current_position[1]
            neighbours = []  # find the neighbours of the current square as a list
            if target_row != 1:
                neighbours.append((target_row - 1, target_col))
            if target_col != 1:
                neighbours.append((target_row, target_col - 1))
            if target_row != n:
                neighbours.append((target_row + 1, target_col))
            if target_col != n:
                neighbours.append((target_row, target_col + 1))
            for iterator in neighbours:
                if iterator not in visited_square:
                    row = iterator[0]
                    col = iterator[1]
                    new_list = path + [(row, col)]
                    fringe.put((cumulative_cost + 1 + values[row - 1][col - 1], new_list))
    return path

shortest_path = path_find(5, (1, 1), (5, 4), [[4,3,3,4,2],[2,4,4,2,2],[3,4,5,3,2],[2,3,4,5,2],[4,3,3,2,4]])
print(shortest_path)