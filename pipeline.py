from collections import deque
visited = set()
flow = set()
def getNextElements(grid,connections):
    elements = []
    for conn in connections:
        if 0 <= conn[1] < len(grid) and 0 <= conn[0] < len(grid[0]) and grid[conn[1]][conn[0]] != ' ':
            elements.append([grid[conn[1]][conn[0]],(conn[0],conn[1])])
    return elements

def parse_input(file_content):
    lines = file_content.strip().split('\n')
    data = [line.split() for line in lines]
    return [(char, int(x), int(y)) for char, x, y in data]

def sortSinkFromVisited(sinks,grid):
    visitedsink = []
    for sink in sinks:
        if sink in visited:
            visitedsink.append(grid [sink[1]] [sink[0]])
    return  ''.join(sorted(visitedsink))

def build_grid(parsed_data):
    max_x = max(item[1] for item in parsed_data)
    max_y = max(item[2] for item in parsed_data)

    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for char, x, y in parsed_data:
        grid[y][x] = char

    return grid


def allConnect(x, y):
    return {(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)}


def horizontal(x, y):
    return {(x + 1, y), (x - 1, y)}


def vertical(x, y):
    return {(x, y + 1), (x, y - 1)}


def upsideL(x, y):
    return {(x + 1, y), (x, y-1)}

def mirroredUpsideL(x, y):
    return {(x - 1, y), (x, y-1)}

def lConnect(x, y):
    return {(x + 1, y), (x, y+1)}

def mirroredL(x, y):
    return {(x -1, y), (x, y+1)}

def rightsideT(x, y):
    return {(x, y+1), (x, y-1),(x+1,y)}

def leftsideT(x, y):
    return {(x, y+1), (x, y-1),(x-1,y)}

def teesideT(x, y):
    return {(x+1, y), (x, y-1),(x-1,y)}

def upsideT(x,y):
    return {(x + 1, y), (x, y + 1), (x - 1, y)}

def getConnections(cell):
    if cell.isalpha():
        return allConnect
    pipe_connections = {
        '═': horizontal,
        '║': vertical,
        '╔': upsideL,
        '╗': mirroredUpsideL,
        '╚': lConnect,
        '╝': mirroredL,
        '╠': rightsideT,
        '╣': leftsideT,
        '╦': teesideT,
        '╩': upsideT,
        '*':allConnect

    }
    return pipe_connections[cell]

def find_connected_sinks(grid):
    source_pos = None
    sinks = set()

    # Identify the source and sink positions
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == '*':
                source_pos = (x, y)
            elif cell.isalpha() and cell.isupper():
                sinks.add((x, y))
    branchFromCurrentElement(source_pos,grid,sinks)
    return sortSinkFromVisited(sinks,grid)

def branchFromCurrentElement(currElement,grid,sinks):
        connections = getConnections(grid[currElement[1]][currElement[0]])(currElement[0], currElement[1])
        nextElements = getNextElements(grid, connections)
        if len(nextElements) > 0:
            for elem in nextElements:
                nextElemConnections = getConnections(elem[0])(elem[1][0],elem[1][1])
                if currElement in nextElemConnections:
                    if currElement not in visited:
                        visited.add(currElement)
                    localflow = (currElement[0],currElement[1],elem[1][0],elem[1][1])
                    if localflow not in flow:
                        flow.add(localflow)
                        branchFromCurrentElement(elem[1],grid,sinks)
        return None

def determine_connected_sinks(file_content):
    parsed_data = parse_input(file_content)
    grid = build_grid(parsed_data)
    connected_sinks = find_connected_sinks(grid)
    return connected_sinks


file_content = """* 0 2
C 1 0
╠ 1 1
╣ 1 2
═ 2 1
╚ 3 0
╝ 3 1
╔ 3 2
═ 4 0
═ 4 2
B 5 0
A 5 2
"""

print(determine_connected_sinks(file_content))
