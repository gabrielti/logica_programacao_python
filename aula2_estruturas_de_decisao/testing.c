#include<stdio.h>

int main(void)
{
    int number;

    printf("type a number:");
    scanf("%i",&number);

    if(number%2 == 0)
    {
        printf("number1\n");
    }

    if(number%4 == 0)
    {
        printf("number2\n");
    }

    else
    {
        printf("wrong number \n");
    }
}