class Game_Setiings:
    def __init__(self, size=3, quantity_matryoshka=6):
        self.size = size
        self.quantity_matryoshka = quantity_matryoshka
        
class Player(Game_Setiings):
    def __init__(self, color, game_account=0):
        self.color = color
        self.matryoshki = [i for i in range(1,Game_Setiings.quantity_matryoshka)]
        self.game_account = game_account
        
class Game_Border(Game_Setiings):
    def __init__(self, coordinates=[None, None], size_matryoshka=None):
        self.matrix = [[None]*Game_Setiings.size]*Game_Setiings.size
        self.size_matryoshka = size_matryoshka
        self.coordinates = coordinates
    def Place_matryoshka(self):
        if not(self.coordinates[0] <= Game_Setiings.size and self.coordinates[0] <= Game_Setiings.size):
            print('Нельзя поставить на эту клетку')
        elif not(self.matrix[self.coordinates[0]][self.coordinates[2]] == None or self.matrix[self.coordinates[0]][self.coordinates[2]] < self.size_matryoshka):
            print('Нельзя поставить на эту клетку')
        else:
            
    
        
    