#include<stdio.h>
#include<stdlib.h>

int calculateScore(char opponent, char player){
    // check for a draw
    if((int)player-23 == (int)opponent) return ((int)player-87)+3;
    
    // check for win
    if(((opponent == 'A')&&(player == 'Y')) || ((opponent == 'B')&&(player == 'Z')) || ((opponent == 'C')&&(player == 'X'))){
        return ((int)player-87)+6;
    }

    // check for loss
    if(((opponent == 'A')&&(player == 'Z')) || ((opponent == 'C')&&(player == 'Y')) || ((opponent == 'B')&&(player == 'X'))){
        return ((int)player-87)+0;
    }

    // so I know something is obviously wrong if what I get is negative
    return(-2147483647);
}

int calculateScore2(char opponent, char result){
    // Case for draw
    if(result == 'Y') return ((int)opponent-64)+3;
    
    // Case for win
    if(result == 'Z'){
        if(opponent == 'A') result = 'Y';
        if(opponent == 'B') result = 'Z';
        if(opponent == 'C') result = 'X';
        return ((int)result-87)+6;
    }

    // Case for loss
    if(result == 'X'){
        if(opponent == 'A') result = 'Z';
        if(opponent == 'B') result = 'X';
        if(opponent == 'C') result = 'Y';
        return ((int)result-87)+0;
    }

    // so I know something is obviously wrong if what I get is negative
    return(-2147483647);
}


int main(void){
    // Create and initialize variables and file pointer
    FILE *f = fopen("input.txt", "r");
    char opp, pla;
    int totalScore = 0;
    int totalScore2 = 0;

    // read file and calculate score of each round
    while(fscanf(f, "%c %c\n", &opp, &pla)!=-1){
        totalScore+=calculateScore(opp, pla);
        totalScore2+=calculateScore2(opp, pla);
    }

    // close file and print output
    fclose(f);
    printf("Total Score           : %d\n", totalScore);
    printf("Total Score for part 2: %d\n", totalScore2);

    return(0);
}