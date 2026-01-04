/*
编写一个程序，要求用户两个浮点数，并打印两数之差除以两数乘积的结果。
在用户输入非数字之前，程序应循环处理用户输入每对值。
*/
#include<stdio.h>

int main(void){

    float a, b, sub, mul, result;

    for(;printf("Please enter two foloat data(seprate by blan):") == 1 ,scanf("%f%f", &a, &b) != 0;)
    {
        sub = a - b;
        mul = a * b;
        result = sub / mul;
        printf("The answer is %f\n", result);
    }
    printf("Program end!\n");

    return 0;
}