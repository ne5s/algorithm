#include <stdio.h>

main()
{
	int c, i, n, j, sum=0;
	int a[1001], avg, cnt=0;
	scanf("%d", &c);
	for(i=0; i<c; i++)
	{
		scanf("%d", &n);
		for(j=0; j<n; j++)
		{
			scanf("%d", &a[j]);
			sum += a[j];
		}
		avg = sum/n;
		for(j=0; j<n; j++)
		{
			if(a[j] > avg)
				cnt++;
		}
		printf("%.3f%%\n", (float)cnt/(float)n*100);
		sum =0; cnt=0;
	}
}