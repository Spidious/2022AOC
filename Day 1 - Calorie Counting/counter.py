
def main():
    # INPUT FILE SHOULD NOT END WITH NEW LINE
    f = open("calorieInput.txt", "r")
    num = 0
    total =  0
    array = []
    count = 0


    while(num!=''):
        # reset total value
        total = 0
        while(True): # continue until break condition is met of num is either new line or ''
            # get the next line from the file
            num = f.readline()

            # break condition   
            if(num == '\n' or num == ''):
                break

            # add the new number to total
            total+=int(num)

        #check if its the new highest number
        array.append(total)
        count+=1

    # sort the array and print outputs
    array.sort(reverse=True)
    print(f"{array[0]} is the highest number of calories held by one elf")
    print(f"{array[0]+array[1]+array[2]} is the highest number of calories held by any three elves combined")

if __name__ == "__main__":
    main()