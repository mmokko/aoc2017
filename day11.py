from day11_input import INPUT


class Coordinates(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def travel(self, direction):
        if direction == 'n':
            self.y += 1
        elif direction == 'ne':
            self.y += 1
            self.x += 1
        elif direction == 'se':
            self.y -= 1
            self.x += 1
        elif direction == 's':
            self.y -= 1
        elif direction == 'sw':
            self.y -= 1
            self.x -= 1
        elif direction == 'nw':
            self.y += 1
            self.x -= 1

    def at_origo(self):
        if self.x == 0 and self.y == 0:
            return True
        return False

    def direction_home(self):
        direction = ''
        # first find y-axel direction
        if self.y > 0:
            direction += 's'
        else:
            direction += 'n'
        # find x-axel direction
        if self.x > 0:
            direction += 'w'
        elif self.x < 0:
            direction += 'e'
        return direction


class HexFinder(object):
    def __init__(self, route):
        self._route = route.split(',')
        self._coords = Coordinates()
        self.furthest_away = 0

    def travel(self):
        for direction in self._route:
            self._coords.travel(direction)
            route = self._find_route_back()
            if self.furthest_away < len(route):
                self.furthest_away = len(route)

    def _find_route_back(self):
        route = list()
        coords = Coordinates(self._coords.x, self._coords.y)
        while not coords.at_origo():
            dir_home = coords.direction_home()
            coords.travel(dir_home)
            route.append(dir_home)
        return route

    def steps_to_origo(self):
        route = self._find_route_back()
        return len(route)


def main():
    hex_finder = HexFinder(INPUT)
    hex_finder.travel()
    print(hex_finder.steps_to_origo())
    print(hex_finder.furthest_away)


if __name__=='__main__':
    main()
