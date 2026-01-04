/*
编写一个程序，创建一个包含8个元素的int类型数组，
分别把数组元素设置为2的前八次幂，
使用for循环设置数组元素的值，使用do while循环显示数组元素的值。
*/
#include<stdio.h>

int main(void){

    int num[8], i, j;

    for(i = 2, j = 0; j < 8; i *= 2, j++){
        num[j] = i;
    }

    j--;
    do{
        printf(" %d", num[j]);
        j--;
    }while( j >=0 );
    printf("\n");

    return 0;
}

/*
参考答案：
#include <stdio.h>
int main(void){
    int data[8];
    data[0] = 2;
    * 初始化第一个元素为2的一次幂 *
    for(int i = 1; i < 8;i++){
        data[i] = data[i-1] * 2;
    }
    * 2的n次幂等于2乘以2的n-1次幂。*
    int i = 0;
    do{
        printf("%d ",data[i++]);
    }while(i<8);

    printf("\nDone!\n");
    return 0;
}
*/