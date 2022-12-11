import time

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

class ropeNode:
    def __init__(self, x = 0, y = 0):
        self.coords = [x, y]
        self.child = None

    def __repr__(self):
        return str(self.coords)

    def setCoords(self, x, y):
        self.coords = list([int(x), int(y)])

    def setChild(self, child):
        self.child = child

    def isTail(self):
        return(self.child == None)

    def checkChildren(self, checkCoords):
        if((checkCoords[0] == self.coords[0]) and (checkCoords[1] == self.coords[1])):
            return True
        if(not self.isTail()):
            return self.child.checkChildren(checkCoords)
        else:
            return False

    def moveChild(self, parCoords):
        if((parCoords==None) or ((abs(parCoords[0]-self.coords[0]) <= 1) and (abs(parCoords[1]-self.coords[1]) <= 1))):       # If has no child or parent node is less than 1 in x or y away, do nothing
            return None
        
        noDiag = False
        if(abs(parCoords[0]-self.coords[0]) > 1):      # check for enough change in X axis
            if(parCoords[0] < self.coords[0]): # Did the parent move left?
                self.setCoords((self.coords[0])-1, self.coords[1])
            if(parCoords[0] > self.coords[0]): # Did the parent move right?
                self.setCoords(self.coords[0]+1, self.coords[1])
            if(abs(parCoords[1]-self.coords[1]) > 0):   # Allow for diagonal movement when moving on X axis
                if(parCoords[1] < self.coords[1]):  # Need to move up?
                    self.setCoords(self.coords[0], self.coords[1]-1)
                if(parCoords[1] > self.coords[1]):  # Need to move down?
                    self.setCoords(self.coords[0], self.coords[1]+1)
            if(not self.isTail()):
                return self.child.moveChild(self.coords)        # Recursively go to next child

        if(abs(parCoords[1]-self.coords[1]) > 1):       # check for enough change in y axis
            if(parCoords[1] < self.coords[1]): # Did the parent move up?
                self.setCoords(self.coords[0], self.coords[1]-1)
            if(parCoords[1] > self.coords[1]): # Did the parent move down?
                self.setCoords(self.coords[0], self.coords[1]+1)
            if(abs(parCoords[0]-self.coords[0]) > 0):   # Allow for diagonal movement when moving on Y axis
                if(parCoords[0] < self.coords[0]):  # Need to move left?
                    self.setCoords(self.coords[0]-1, self.coords[1])
                if(parCoords[0] > self.coords[0]):  # Need to move right?
                    self.setCoords(self.coords[0]+1, self.coords[1])
            if(not self.isTail()):
                return self.child.moveChild(self.coords)        # Recursively go to next child


def redrawMap(map, head, tail):
    newMap = []
    for row in range(0, len(map)):
        mapRow = []
        for column in range(0, len(map[row])):
            if(([column, row] == tail.coords) or (map[row][column] == '#')):
                mapRow.append('#')
                continue
            if(head.checkChildren([column, row])):
                mapRow.append('@')
            else:
                mapRow.append('.')
        newMap.append(mapRow)
    return(newMap)



if __name__ == "__main__":
    NUM_NODES = 320 # exclusive of head | Can NOT be less than 1, must be integer
    GRID_SIZE = 12  # Only neccesary to change if drawing grid

    map = [[ '.' for x in range(0,GRID_SIZE)] for y in range(0,GRID_SIZE)]

    #Set tail length
    head = ropeNode()
    head.setCoords(GRID_SIZE/2, GRID_SIZE/2)
    curNode = head
    for i in range(0, NUM_NODES):
        curNode.setChild(ropeNode())
        curNode = curNode.child
        curNode.setCoords(GRID_SIZE/2, GRID_SIZE/2)
    del curNode

    # save tail node
    tail = head
    while(not tail.isTail()):
        tail = tail.child


    # get file data
    fp = open("input.txt", "r")
    input = fp.readlines()
    holdInput = input
    fileSize = len(input)
    fp.close()

    tailCoords = []

    
    printProgressBar(0, fileSize, prefix = 'Progress:', suffix = 'Complete', length = 50)
    while(len(input) != 0):
        command = input[0].strip('\n').split()
        
        if(command[0] == 'U'):  # If command says UP
            for i in range(0, int(command[1])):
                head.setCoords(head.coords[0], head.coords[1]-1)
                # head.setCoords(head.coords[0], head.coords[1]-1) # If I don't do this it doesn't save it for whatever reason
                head.child.moveChild(head.coords)
                tailCoords.append(tail.coords)
                # map = redrawMap(map, head, tail)
                

        if(command[0] == 'D'):  # If command says DOWN
            for i in range(0, int(command[1])):
                head.setCoords(head.coords[0], head.coords[1]+1)
                # head.setCoords(head.coords[0], head.coords[1]+1) # If I don't do this it doesn't save it for whatever reason
                head.child.moveChild(head.coords)
                tailCoords.append(tail.coords)
                # map = redrawMap(map, head, tail)

        if(command[0] == 'L'):  # If command says LEFT
            for i in range(0, int(command[1])):
                head.setCoords(head.coords[0]-1, head.coords[1])
                # head.setCoords(head.coords[0]-1, head.coords[1]) # If I don't do this it doesn't save it for whatever reason
                head.child.moveChild(head.coords)
                tailCoords.append(tail.coords)
                # map = redrawMap(map, head, tail)

        if(command[0] == 'R'):  # If command says RIGHT
            for i in range(0, int(command[1])):
                head.setCoords(head.coords[0]+1, head.coords[1])
                # head.setCoords(head.coords[0]+1, head.coords[1]) # If I don't do this it doesn't save it for whatever reason
                head.child.moveChild(head.coords)
                tailCoords.append(tail.coords)
                # map = redrawMap(map, head, tail)
        

        input = input[1:]
        printProgressBar(fileSize-len(input), fileSize, prefix = 'Progress:', suffix = 'Complete', length = 50)

    # remove duplicate coordinates
    import itertools
    tailCoords.sort()
    tailCoords = list(tailCoords for tailCoords,_ in itertools.groupby(tailCoords))


    print('output : ',len(tailCoords))
    # print("\n",count)



