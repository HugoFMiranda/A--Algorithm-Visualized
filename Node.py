import pygame
import Colors

class Node:

    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.width = width
        self.total_rows = total_rows
        self.x = row * width
        self.y = col * width
        self.neighbors = []
        self.color = Colors.DARK_GREY

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == Colors.RED

    def is_open(self):
        return self.color == Colors.PINK

    def is_barrier(self):
        return self.color == Colors.LIGHT_GREY

    def is_start(self):
        return self.color == Colors.ORANGE

    def is_end(self):
        return self.color == Colors.TURQUOISE

    def reset(self):
        self.color = Colors.DARK_GREY

    def make_closed(self):
        self.color = Colors.RED

    def make_open(self):
        self.color = Colors.PINK

    def make_barrier(self):
        self.color = Colors.LIGHT_GREY

    def make_start(self):
        self.color = Colors.ORANGE

    def make_end(self):
        self.color = Colors.TURQUOISE

    def make_path(self):
        self.color = Colors.LIGHT_GREEN

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []

        # Baixo y+
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row + 1][self.col])

        # Cima y-
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row - 1][self.col])

        # Direita x+
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col + 1])

        # Esquerda x-
        if self.col < self.total_rows - 1 and not grid[self.row][self.col - 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        return False
