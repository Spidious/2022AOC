#include<stdio.h>
#include<stdlib.h>

int checkEncase(int firLow, int firHigh, int secLow, int secHigh){
    if(firLow <= secLow){
        if(firHigh >= secHigh) return 1;
    }
    if(firLow >= secLow){
        if(firHigh <= secHigh) return 1;
    }
    return 0;
}

int checkEncase2(int firLow, int firHigh, int secLow, int secHigh){
    if((firLow >= secLow) && (firLow <= secHigh) || (secLow >= firLow) && (secLow <= firHigh)) return 1;
    if((firHigh >= secLow) && (firHigh <= secHigh || (secHigh >= firLow) && (secLow <= firHigh))) return 1;
    return 0;
}

int main(void){
    // open file to fp
    FILE * fp = fopen("input.txt", "r");
    // create variables for first low & high and second low & high, and count variables
    int firLow = 0, firHigh = 0, secLow = 0, secHigh = 0, count1 = 0, count2 = 0;
    int val = 0;

    // get each assignment pairing from file and pass it to a function
    while(1){
        if(fscanf(fp, "%d-%d,%d-%d\n", &firLow, &firHigh, &secLow, &secHigh) == -1) break;
        if(checkEncase(firLow, firHigh, secLow, secHigh)) count1++;
        if(checkEncase2(firLow, firHigh, secLow, secHigh)) count2++;

    }

    printf("part 1: %d\n", count1);
    printf("part 2: %d\n", count2);
}