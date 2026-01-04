/*
客户Daphne以10%的单利息投资了100美元
（也就是说，每年投资获利相当于原始投资的 10%）。
客户Deirdre以5%复合利息投资了100美元，
（也就是说，利息是当前余额的5%，包含之前的利息），
编写一个程序计算并输出需要多少年Deirdre的投资额才会超过Daphne，并显示那时两人的投资额。
*/
#include<stdio.h>

int main(void){

    int year;
    double Daphne, Deirdre, irate_Da, irate_De;

    for(year = 1, Daphne = Deirdre = 100, irate_Da = 0.1, irate_De = 0.05; Daphne >= Deirdre; year++){
        Daphne += 100*irate_Da;
        Deirdre *= (1 + irate_De);
    }

    printf("Need %d years, Daphen'money: %lf, Deirdre'money: %lf\n", year-1, Daphne, Deirdre);
    return 0;
}