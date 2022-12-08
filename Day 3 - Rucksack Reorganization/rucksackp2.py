from rucksack import checkupper


def checkDuplicates(str):
    for c in str[0]:
            for s in str[1]:
                if(c == s):
                    for i in str[2]:
                        if i == c:
                            if(checkupper(c)):
                                return(ord(c)-38)
                            else:
                                return(ord(c)-96)

def main():
    f = open("input.txt", "r")
    list = []

    while(True):
        str = [f.readline().strip('\n'), f.readline().strip('\n'), f.readline().strip('\n')]

        if(str[0] == '' or str[1] == '' or str[2] == ''):
            break

        list.append(checkDuplicates(str))

    print(f"The solution to part 2 is {sum(list)}")

if __name__ == "__main__":
    main()