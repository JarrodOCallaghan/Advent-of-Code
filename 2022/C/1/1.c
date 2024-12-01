#include <stdio.h>
#include <stdlib.h>
#define MAX_LINE_LENGTH 100

// Take in text file
// For each line:
// Add numbers until new line is found
// If Newline, make a new number set
int main(){
    FILE    *textfile;
    char    line[MAX_LINE_LENGTH];
    char    ch;
    int     counter = 0;
    int     highest = 0;
    // int     high[3];
    printf("FIND Elf calories\n\n");
    textfile = fopen("dataset.txt", "r");
    if(textfile == NULL)
        return 1;
 
    while (fgets(line, MAX_LINE_LENGTH, textfile)){

        if (*line == '\n'){
            printf("%i", counter);
            if (counter > highest){
                highest = counter;
            }

            // switch (counter):
            //     case counter > high[0]:
            //         high[2] = high[1];
            //         high[1] = high[0];
            //         high[0] = counter;
            //         break;
            //     case high[0] > counter > high[2]:





            counter = 0;
            printf("\n\n");
        } else {
            int current = atoi(line);
            counter += current;
        }
    }
    printf("%i", highest);
    fclose(textfile);
    return 0;
}