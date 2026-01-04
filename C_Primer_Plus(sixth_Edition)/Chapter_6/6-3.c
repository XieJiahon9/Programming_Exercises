/*
使用嵌套循环，按下面的格式打印字母。
F
FE
FED
FEDC
FEDCB
FEDCBA
*/
#include<stdio.h>

int main(void){

    int i, j;

    for(i = 'F'; i >= 'A'; --i){
        for(j = 'F'; j >= i; --j)
            printf("%c", j);
        printf("\n");
    }

    return 0;
}