#include <cstdio>
#include <cstdlib>
using namespace std;

int main(void)
{
	char str[255];
	int base;
	scanf("%s %d", &str, &base);
	printf("%d\n", strtol(str, NULL, base));
	return 0;
}