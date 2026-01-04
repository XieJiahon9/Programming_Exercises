/*
编写一个程序，读取一行输入，然后把输入的内容倒序打印出来，
可以把输入存储在char类型的数组中，假设每行字符不超过255。
回忆一下，根据%c转换说明，scanf()函数一次只能从输入中读取一个字符，
而且在用户按下enter键时，scanf()函数才会生成一个换行字符\n。
*/
#include<stdio.h>
#include<string.h>

#define SIZE 256

int main(void){

    char stringg[SIZE];

    printf("Enter the char in a line : ");
    scanf("%s", stringg);

    for(int i = strlen(stringg) - 1, printf("The reverse char of the data: "); i >= 0; i--){
        printf("%c",stringg[i]);
    }

    return 0;
}

/*
参考答案：
#include <stdio.h>
#include <string.h>
int main(void){
    char data[256];
    printf("Enter the char in a line : ");
    int i = 0;
    do{
        scanf("%c",&data[i]);
    }while(data[i]!='\n' && ++i);
     * 循环读取用户输入的字符，并保存之字符数组，直到用户输入回车符
     * 循环未检查输入字符数量，特定情况可能会产生溢出*
    printf("The reverse char of the data: ");
    for(i--;i >=0;i--){
         * 原下标 i 为最后一个字符的下标，初始化时 i-- 目的删除最后一个换行符 *
        printf("%c",data[i]);
    }
    printf("\nDone!\n");
    return 0;
}
*/