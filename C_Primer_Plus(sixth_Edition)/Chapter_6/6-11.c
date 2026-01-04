/*
编写一个程序，在数组中读入8个整数，然后倒序打印着8个整数。
*/
#include<stdio.h>

int main(void){

    int i, num[8];
    
    printf("Enter the 8 integer data (seperate by blank): ");
    for(i = 0; i < 8; i++){
        scanf("%d", &num[i]);
    }

    printf("Ok, the reverse data is :");
    for(i--; i >= 0; i--)
    {
        printf(" %d", num[i]);
    }
    printf("Done!\n");

    return 0;
}