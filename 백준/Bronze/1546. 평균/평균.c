#include <stdio.h>


int main()
{
	int n, i, max=0;
	float sum=0.00;
	float a[1001];
	scanf("%d", &n);
	if(n>1000)
		return -1;
	for(i=0; i<n; i++)
		scanf("%f", &a[i]);	
	for(i=0; i<n; i++)
	{
		if(a[i] > max)
			max = a[i];
	}
	for(i=0; i<n; i++)
	{
		sum += a[i];
	}
	printf("%.2f", (sum/max*100)/n);

	return 0;
}	