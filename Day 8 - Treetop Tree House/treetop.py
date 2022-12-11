class Forest:
    # format the input to self.trees
    def __init__(self, input):
        self.trees = input
        for row in range(0, len(input)):
            input[row] = [*input[row]]
            input[row].remove('\n')
            for x in range(0, len(input[row])):
                input[row][x] = int(input[row][x])+1

    # returns the object representation in string format 
    def __repr__(self):
        return str(self.trees)

    def markTop(self):
        # loop through length of rows
        for x in range(0, len(self.trees[0])):
            treeColumn = [] #reset Tree Column
            treeColumn.clear()
            # Loop through each row, add it to TreeColumn
            for y in range(0, len(self.trees)):
                treeColumn.append(self.trees[y][x])
            
            # mark the visible trees from the top if not already marked
            treeColumn = markVisible(treeColumn)
            y = 0
            for y in range(0, len(self.trees)):
                self.trees[y][x] = treeColumn[y]    # set treeColumn back into the main tree

    def markRight(self):
        for row in range(0, len(self.trees)):
            self.trees[row].reverse()
            self.trees[row] = markVisible(self.trees[row])
            self.trees[row].reverse()

    def markBottom(self):
        # loop through length of rows
        for x in range(0, len(self.trees[0])):
            treeColumn = [] #reset Tree Column
            treeColumn.clear()
            # Loop through each row, add it to TreeColumn
            for y in range(0, len(self.trees)):
                treeColumn.append(self.trees[y][x])
            
            # mark the visible trees from the top if not already marked
            treeColumn.reverse()
            treeColumn = markVisible(treeColumn)
            treeColumn.reverse()
            y = 0
            for y in range(0, len(self.trees)):
                self.trees[y][x] = treeColumn[y]    # set treeColumn back into the main tree

    def markLeft(self):
        for row in range(0, len(self.trees)):
            self.trees[row] = markVisible(self.trees[row])

    def countMarked(self):
        count = 0
        for row in self.trees:
            for item in row:
                if(item < 0):
                    count+=1
        return count

    def checkUp(self, y, x):
        # check if top of map
        if(y==0):
            return 0
        # Get every tree in the range of sight
        viewRange = []
        for row in range(0, y):
            viewRange.append(abs(self.trees[row][x]))

        # mark the visible trees
        viewRange.reverse()        
        viewRange = markVisible2(viewRange, abs(self.trees[y][x]))

        # Count the marked trees
        count = 0
        for tree in viewRange:
            if(tree<0):
                count+=1
        return count

    def checkDown(self, y, x):
        # check if top of map
        if(y==len(self.trees)-1):
            return 0
        # Get every tree in the range of sight
        viewRange = []
        for row in range(y+1, len(self.trees)):
            viewRange.append(abs(self.trees[row][x]))

        # mark the visible trees
        viewRange = markVisible2(viewRange, abs(self.trees[y][x]))

        # Count the marked trees
        count = 0
        for tree in viewRange:
            if(tree<0):
                count+=1
        return count

    def checkLeft(self, y, x):
        if(x == 0):
            return 0
        
        viewRange = self.trees[y][:x]
        for item in range(0, len(viewRange)):
            viewRange[item] = abs(viewRange[item])

        viewRange.reverse()
        viewRange = markVisible2(viewRange, abs(self.trees[y][x]))

        # Count the marked trees
        count = 0
        for tree in viewRange:
            if(tree<0):
                count+=1
        return count      

    def checkRight(self, y, x):
        if(x == len(self.trees[y])-1):
            return 0
        
        viewRange = self.trees[y][x+1:]
        for item in range(0, len(viewRange)):
            viewRange[item] = abs(viewRange[item])

        viewRange = markVisible2(viewRange, abs(self.trees[y][x]))

        # Count the marked trees
        count = 0
        for tree in viewRange:
            if(tree<0):
                count+=1
        return count 

    # Create a map of the scenic score for that position
    def createScenicMap(self):
        map = []
        for row in range(0, len(self.trees)):
            mapRow = []
            mapRow.clear()
            for item in range(0, len(self.trees[row])):
                up = self.checkUp(row, item)
                down = self.checkDown(row, item)
                left = self.checkLeft(row, item)
                right = self.checkRight(row, item)
                mapRow.append(up*left*right*down)
                # print(f"{up} {down} {left} {right}")
            map.append(mapRow)
            # print()
        return map

# mark the visible trees (change them to negative)
def markVisible(list):
    result = []
    highest = 0

    for tree in list:
        if(abs(tree) > highest):
            if(tree >= 0):
                result.append(tree*-1)
            else:
                result.append(tree)
            highest = abs(tree)
        else:
            result.append(tree)

    return result

def markVisible2(list, current):
    marks = []
    highest = abs(list[0])
    for item in range(0, len(list)):

        if(current == list[item]):
            marks.append(abs(list[item])*-1)
            return marks

        if(current < list[item]):
            marks.append(abs(list[item])*-1)
            return marks

        if(highest <= abs(list[item])):
            highest = abs(list[item])
            marks.append(abs(list[item])*-1)

    return marks





def main():
    # Get input as a list of rows
    fp = open("input.txt", 'r')
    forest = Forest(fp.readlines())
    fp.close()

    forest.markTop()
    forest.markBottom()
    forest.markLeft()
    forest.markRight()
    print(forest.countMarked())

    map = forest.createScenicMap()
    # print(map)

    print(max(max(map)))
    # print(map)

if __name__ == "__main__":
    main()
