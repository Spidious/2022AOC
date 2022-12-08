from stacksPt1 import Stack

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

    # ##################### Start Stacking ######################

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
        crates = Stack()
        # move to crates stack
        for crate in range(0, int(result[0])):
            crates.push(stackList[int(result[1])-1].pop())
        crate = 0
        # move to stackLlist
        for crate in range(0, int(result[0])):
            stackList[int(result[2])-1].push(crates.pop())

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