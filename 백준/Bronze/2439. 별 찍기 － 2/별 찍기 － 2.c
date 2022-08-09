#include <stdio.h>

int main()
    {
    int i,j,k,N;
    scanf("%d", &N);
    for(i=0; i<N; i++){
        for(j=i; j<N-1; j++)
            {
            printf(" ");
        }
        for(k=0; k<i+1;k++)
            {
            printf("*");
        }
        printf("\n");
    }
    return 0;
}