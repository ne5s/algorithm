#include<stdio.h>

main()
{
	int n, a, b;

	scanf("%d", &n);
	a = n/5; n%=5;

	while(a>=0)
	{
		if(!(n%3))
		{
			b = n/3;
			n %= 3;
			break;
		}
		a--; n+=5;
	}
	printf("%d", n==0?a+b:-1); 
}