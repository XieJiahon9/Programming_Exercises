/*编写一个程序把一个单词读入一个字符数组中，然后倒序打印这个单词。*/
#include<stdio.h>
#include<string.h>

#define SIZE 50

int main(void){

    int i;
    char word[SIZE];

    printf("ENter the word u want.\n");
    scanf("%s", word);

    for(i = strlen(word)-1; i >= 0; i--)
        printf("%c", word[i]);
    printf("\n");

    return 0;
}