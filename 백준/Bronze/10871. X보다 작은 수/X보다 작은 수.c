#include <stdio.h>

int main() {
	int i, j, N, X;
	int a[10000];
	scanf("%d %d", &N, &X);
	for (i = 0; i < N; i++) {
		scanf("%d", &a[i]);
	}
	for (j = 0; j < N; j++) {
		if (a[j] < X)
			printf("%d ", a[j]);
	}
	return 0;
}