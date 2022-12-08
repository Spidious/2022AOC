
# Stack class
class Stack:
    # Initialize the stack
    def __init__(self):
        self.items = []

    # Boolean function to check if stack is empty
    def is_empty(self):
        return len(self.items) == 0

    # Push a new item onto the stack
    def push(self, item):
        self.items.append(item)

    # Remove and return the top item on the stack
    def pop(self):
        return self.items.pop()

    # Return the top item of the stack without removing it
    def peek(self):
        if not self.is_empty():
            return self.items[len(self.items)-1]
        else:
            return None

    # return the size of the stack
    def size(self):
        return len(self.items)

    def printStack(self):
        print(self.items)

    def removeOccurance(self, item):
        for x in range(0, len(self.items)):
            try:
                self.items.remove(item)
            except: 
                return None


# Main Function
def main():
    # create a file object and dump the csv file into a list, strip the \n characters
    fp = open("input.csv", "r")
    list = fp.readlines()
    for item in list:
        item.strip("\n")
    fp.close()

    # reverse the list, create stack object, and a list
    list.reverse()
    stackList = []
    # initialize the list
    for x in range(0, 9*2):
        stackList.append(Stack())

    # fill the stacks skipping the odd indexes
    for column in range(0, 9*2):
        if(column % 2 == 1):
            continue
        for row in list:
            stackList[column].push(row[column])
    
    # remove the odd indexes and occurances of ' '
    for x in range(9*2-1, -1, -1):
        if(x % 2 == 1):
            del stackList[x]
            continue
        stackList[x].removeOccurance(' ')


    # ################# Start moving crates ################
    fp = open("input.txt", "r")
    # Start the actual moving of crates
    while(True):
        # get each line from input.txt until the break condition is satisfied
        result = fp.readline()
        if(result == ''):
            break
        # remove the words "move" "from" and "to"
        result = result.split()
        result.remove('move')
        result.remove('from')
        result.remove('to')

        # move the crates
        for crate in range(0, int(result[0])):
            stackList[int(result[2])-1].push(stackList[int(result[1])-1].pop())

        # # Print the stack
        # print("Current .CSV")
        # for x in range (0, 9):
        #     stackList[x].printStack()
    fp.close()
    print("result:")
    for stack in stackList:
        print(stack.peek())



if __name__ == "__main__":
    main()
