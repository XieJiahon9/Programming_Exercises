/*
编写一个程序，创建一个包含26个元素的数组，
并在其中存储26个小写字母。然后打印数组的所有内容。
*/
#include<stdio.h>

#define SIZE 26

int main(void){

    char alphabet_small[SIZE];

    for(int i = 'a'; i <= 'z'; i++)
    {
        alphabet_small[i-'a'] = i;
        printf(" %c", alphabet_small[i-'a']);
    }

    return 0;
}