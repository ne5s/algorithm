#include <stdio.h>
main()
{
	int n, i;
	char a[101];
	int sum=0;
	scanf("%d", &n);
	scanf("%s", a);
	for(i=0; i<n; i++)
	{
		sum += a[i]-48;
	}
	printf("%d", sum);
}