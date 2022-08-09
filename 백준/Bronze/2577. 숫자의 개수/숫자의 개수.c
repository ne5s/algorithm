#include <stdio.h>

int main()
{
    int A, B, C, result, cal[10]={0,}, i;
    scanf("%d", &A);
    scanf("%d", &B);
    scanf("%d", &C);

    result = A * B * C;

    while(result)
    {
        cal[result % 10]++;
        result /= 10;
    }

    for(i=0; i<10; i++)
        printf("%d\n", cal[i]);


    return 0;
}
