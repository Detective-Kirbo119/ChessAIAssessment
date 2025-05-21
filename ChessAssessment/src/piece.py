import os
class Piece:
    def __init__(self, name, color, value, texture=None, texture_rect=None):
        self.name = name
        self.color = color
        value_sign  = 1 if color == "white" else -1
        self.value = value * value_sign
        self.moves = []
        self.moved = False
        self.set_texture()
        self.texture_rect = texture_rect

    def set_texture(self, size = 80):
        self.texture = os.path.join(
            #"assets", f"{self.name}_{self.color}.png"
            f'assets/images/imgs-{size}px/{self.name}_{self.color}.png')
        self.texture_rect = None    
        ##if self.color == "white":
        ##   self.texture = pygame.image.load(f"assets/{self.name}_w.png")
        ##else:
        ##   self.texture = pygame.image.load(f"assets/{self.name}_b.png")

        ##self.texture = pygame.transform.scale(self.texture, (SQUARE_SIZE, SQUARE_SIZE))
        ##self.texture_rect = self.texture.get_rect()

        def add_moves(self, move):
            self.moves.append(move)
            if move not in self.moves:
                self.moves.append(move)

class Pawn(Piece):
    def __init__(self, color):
        
        self.dir = -1 if color == "white" else 1    
        super().__init__("pawn", color, 1.0)
        ##  self.moved = False

class Knight(Piece):    
    def __init__(self, color):
        super().__init__("knight", color, 3.0)
        ##self.moved = False

class Bishop(Piece):
    def __init__(self, color):
        super().__init__("bishop", color, 3.001)
        ##self.moved = False

class Rook(Piece):
    def __init__(self, color):
        super().__init__("rook", color, 5.0)
        ##self.moved = False

class Queen(Piece):
    def __init__(self, color):
        super().__init__("queen", color, 9.0)
        ##self.moved = False

class King(Piece):
    def __init__(self, color):
        super().__init__("king", color, 10000.0)
        ##self.moved = False