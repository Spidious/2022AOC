# Checks if a character or string is Upper or lowercase
# Takes one argument of type Char or String
# returns Boolean Value
def checkupper(char):
    if ord(char) < 96 :
        return True
    return False 

# Checks for duplicates in two halves of a string
# takes two strings, returns integer value of priority for the duplicate
def checkDuplicates(half1, half2):
    for c in half1:
        for s in half2:
            if(c == s):
                if(checkupper(c)):
                    return(ord(c)-38)
                else:
                    return(ord(c)-96)

def main():
    f = open("input.txt", "r")
    list = []
    count = 0

    # 
    while(True):
        str = f.readline()
        if(str == ''):
            break
        
        firstpart, secondpart = str[:len(str)//2], str[len(str)//2:]    # I don't know how this works I pulled it off github
        list.append(checkDuplicates(firstpart, secondpart))
        count+=1
    
    print(f"Solution to Part 1 is : {sum(list)}")

    f.close()



if __name__ == "__main__":
    main()