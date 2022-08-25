#include <stdio.h>

int gcd(int x, int y)
{
    if(y != 0)
        gcd(y, x%y);
    else
        return x;
}

int main()
{
    int i, j, k, l, p, temp;

    scanf("%d", &l);

    for(i=0; i < l; i++)
    {
        scanf("%d %d", &j, &k);

        if(j<k)
        {
            temp = j;
            j = k;
            k = temp;
        }

        p = gcd(j, k);

        printf("%d\n", p*(j/p)*(k/p));

    }
}
