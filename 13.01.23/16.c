long long f(long long n) {
	if (n == 0) return 0;
	if (n % 2 != 0) return f(n - 1) + 1;
	if (n > 0 && n % 2 == 0) return f(n / 2);
	exit(1);
}

int main() {
	long long c = 0;
	for (long long i = 0; i < 1'000'000'000LL; i++) {
		if (f(i) == 2) {
			c++;
		}
	}
	printf("%lld\n", c);
}