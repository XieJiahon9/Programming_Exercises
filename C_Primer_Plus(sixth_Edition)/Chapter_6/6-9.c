/*
修改习题八，自定义一个函数calc()，
该函数有两个参数，用于输入习题八中的两个数字，
返回值为习题八中要求的运算结果。
习题八：
编写一个程序，要求用户两个浮点数，并打印两数之差除以两数乘积的结果。
在用户输入非数字之前，程序应循环处理用户输入每对值。
*/
#include<stdio.h>

float calc(float a, float b);

int main(void){

    float a, b, result;

    for(;printf("Please enter two foloat data(seprate by blan):") == 1 ,scanf("%f%f", &a, &b) != 0;)
    {
        result = calc(a, b);
        printf("The answer is %f\n", result);
    }
    printf("Program end!\n");

    return 0;
}

float calc(float a, float b){

    float sub, mul;

    sub = a - b;
    mul = a * b;

    return sub / mul;
}