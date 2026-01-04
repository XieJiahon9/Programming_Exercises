/*
考虑下面两个无限序列：
1.0 + 1.0/2.0 + 1.0/3.0 + 1.0/4.0 + ...
1.0 - 1.0/2.0 + 1.0/3.0 - 1.0/4.0 + ...
编写一个程序计算这两个无限序列的总和，直到到达某次数。
让用户交互地输入指定的次数，当用户输入0或负值时结束输入。
查看运行100项、1000项、10000项后的总和，是否发现每个序列都收敛于某值？
*/
#include<stdio.h>
int main(void){

    double denominator, sum1, sum2, times;

    printf("Enter the limit length: ");
    scanf("%lf", &times);
    while(times > 0){

        for(denominator = 1, sum1 = sum2 = 0; denominator <= times ; denominator++)
        {
            sum1 += 1/denominator;
            if((int)denominator%2==0)
                sum2 -= 1/denominator;
            else
                sum2 += 1/denominator;
        }

        printf("The sum for 1.0 +...+ 1.0/%.1lf is %lf\n", times, sum1);
        printf("The sum for 1.0 -...+ 1.0/%.1lf is %lf\n", times, sum2);

        printf("Enter the limit length: ");
        scanf("%lf", &times);
    }
    printf("Done!\n");

    return 0;
}