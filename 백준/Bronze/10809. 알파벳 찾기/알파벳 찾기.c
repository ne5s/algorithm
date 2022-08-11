#include <stdio.h>
#include <string.h>

int main()
{
    int i, b[26], a[100];
    char S[100];

    scanf("%s", &S);

    for(i=0; i<26; i++)
    {
        b[i] = -1;
    }

    for(i=0; i<strlen(S); i++)
    {
        a[i] = S[i];
        if(b[a[i]-97] == -1)
                b[a[i]-97] = i;
    }

    for(i=0; i<26; i++)

    {
        printf("%d ", b[i]);
    }

    return 0;
}
