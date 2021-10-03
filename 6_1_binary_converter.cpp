#include <stdio.h>

void binary(long long n) {
	if (n > 0) {
		binary(n / 2);
		printf("%lld", n % 2);
	}
}

int main() {
	long long n;
	scanf("%lld", &n);
	binary(n);
}
