
def main():
    # open and read file, then close
    fp = open("input.txt", "r")
    str = fp.readline()
    fp.close()

    # start count at 4, loop until string has less than 4 characters or a break statement is satisfied
    count = 4
    while(len(str)>=4):
        # save the first 4 characters to new string
        try:
            newString = str[:4]
        except:
            break
        
        # add newString to a set since they cannot contain duplicates, check if they are of the same length
        # if not add 1 to count and remove first element from original string
        strSet = set(newString)
        if(len(strSet) == len(newString)):
            break
        else:
            count+=1
            str = str[1:]
    
    # print the answer
    print(f"answer is {count}")


if __name__ == "__main__":
    main()