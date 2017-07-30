class Maze(object):
    def __init__(self, maze):
        self.maze = maze
        self.start_position = [-1, -1]

    def get_start_position(self):
        if self.start_position != [-1, 1]:
            return self.start_position

        start_position = [0, 0]
        row_idx = -1
        for row in self.maze:
            row_idx += 1
            col_idx = -1
            for item in row:
                col_idx += 1
                if item == 2:
                    self.start_position = [col_idx, row_idx]
                    return [col_idx, row_idx]
        return start_position

    def get_position_value(self,x , y):
        if x < 0 or y < 0 or x > len(self.maze) or y > len(self.maze[0]):
            return 1
        return self.maze[y][x]

    def is_wall(self, x, y):
        return self.get_position_value(x, y) == 1

    def get_max_x(self):
        return len(self.maze[0]) - 1

    def get_max_y(self):
        return len(self.maze) - 1

    def score_route(self, route):
        score = 0
        visited = [[False] * self.get_max_y() for _ in range(self.get_max_x())]
        for route_step in route:
            if self.maze[route_step[1]][route_step[0]] == 3 and visited[route_step[1]][route_step[0]] == False:
                score += 1
                visited[route_step[1]][route_step[0]] = True
        return score




