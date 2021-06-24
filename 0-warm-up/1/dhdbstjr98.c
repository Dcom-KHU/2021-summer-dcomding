#include <stdio.h>
#include <stdlib.h>

int main() {
	int num, i;
	scanf("%d", &num);

	for(i = 1; i <= 3; i++) {
		printf("%d * %d = %d\n", num, i, i * num);
	}

	return 0;
}