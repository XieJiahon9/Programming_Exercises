/*
Chuckie Lucky赢得了100万美元（税后），
他把奖金存入了年利率8%的账户。在每年的最后一天Chuckie取出10万美元。
编写一个程序，计算并输出多少年后Chuckie会取完账户的钱？
*/
#include<stdio.h>

int main(void){

    int year;
    float award_money;

    for(year = 1, award_money = 100; award_money > 0; year++){
        award_money *= 1+0.08;
        award_money -= 10;
    }
    printf("Need %d years!\n", year-1);

    return 0;
}