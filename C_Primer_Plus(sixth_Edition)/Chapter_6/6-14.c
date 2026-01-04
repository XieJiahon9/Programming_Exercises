/*
编写一个程序，创建两个包含8个元素的double类型数组，
使用循环提示用户为第一个数组输入8个值。
第二个数组元素的值设置为第一个数组对应元素的累积之和。
例如，第二个数组的第4个元素的值是第一个数组的前4个元素之和。
第二个数组的第5个元素是第一个数组的前5个元素之和。
最后使用循环显示两个数组的内容，
第一个数组显示成一行，第二个数组显示在第一个数组的下一行，
而且每一个元素都与第一个数组的元素相对应。
*/
#include<stdio.h>

#define SIZE 8

int main(void){

    int i;
    double num1[SIZE], num2[SIZE];

    for(i = 0, printf("Enter 8 data to the FIRST array: "); i < 8; i++){
        scanf("%lf", &num1[i]);
        if(0 == i)  /*比较时用‘==’，单个‘=’号是赋值运算*/
            num2[i] = num1[i];
        else
            num2[i] = num2[i-1] + num1[i];
    }

    printf("All the data of twp array:\n");
    for(i = 0, printf("First Array: "); i < 8; i++){
        printf("%15.6lf", num1[i]);
    }
    printf("\n");

    for(i = 0, printf("Second Array:"); i < 8; i++){
        printf("%15.6lf", num2[i]);
    }
    printf("\n");


    printf("Done!\n");

    return 0;
}