/*
使用嵌套循环，按照下面的格式打印字母。
A
BC
DEF
GHIJ
KLMNO
PQRSTU
*/
#include<stdio.h>

int main(){

    int i,j;
    char letter;

    for(i = 1, letter = 'A'; i <= 6; i++)
    {
        for(j = 1; j <= i; j++,letter++)
            printf("%c", letter);
        printf("\n");
            
    }

    return 0;
}