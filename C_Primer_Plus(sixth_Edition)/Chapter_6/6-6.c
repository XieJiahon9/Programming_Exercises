/*
编写一个程序打印一个表格，每一行打印一个整数、该数的平方、该数的立方。
要求用户输入表格的上下限，使用一个for循环。
*/
#include<stdio.h>

int main(void){

    int start, end, i;

    printf("Please enter the start number:");
    scanf("%d", &start);
    printf("Please enter the end number:");
    scanf("%d", &end);

    printf("%8s:%10s:%10s:\n", "Ori", "Square", "Cubic");
    for(i = start; i <= end; i++)
        printf("%8d,%9d,%11d\n", i, i*i, i*i*i);

}