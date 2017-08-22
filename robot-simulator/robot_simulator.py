class NORTH(object):
    def __init__(self):
        pass

class SOUTH(object):
    def __init__(self):
        pass

class EAST(object):
    def __init__(self):
        pass

class WEST(object):
    def __init__(self):
        pass
    
class Robot(object):
    def __init__(self, direction=NORTH, x=0, y=0):
        self.directions = [NORTH, EAST, SOUTH, WEST]
        self.direction = direction()
        self.x = x
        self.y = y
    
    def coordinates(self):
        return (self.x, self.y)
    
    def bearing(self):
        return type(self.direction)
    
    def turn_right(self):
        d_index = self.directions.index(type(self.direction))
        if d_index == 3:
            self.direction = self.directions[0]()
        else:
            self.direction = self.directions[d_index + 1]()
        
    
    def turn_left(self):
        d_index = self.directions.index(type(self.direction))
        if d_index == 0:
            self.direction = self.directions[3]()
        else:
            self.direction = self.directions[d_index - 1]()
    
    def advance(self):
        if type(self.direction) == NORTH:
            self.y += 1
        if type(self.direction) == SOUTH:
            self.y += -1
        if type(self.direction) == EAST:
            self.x += 1
        if type(self.direction) == WEST:
            self.x += -1
    
    def simulate(self, sim_list):
        for sim in list(sim_list):
            if sim == 'L':
                self.turn_left()
            if sim == 'R':
                self.turn_right()
            if sim == 'A':
                self.advance()
