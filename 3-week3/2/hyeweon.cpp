#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
	int n;
	cin >> n;

	int* t = new int[n + 1];
	int* p = new int[n + 1];
	for (int i = 0; i < n; i++) {
		cin >> t[i] >> p[i];
	}
	t[n] = p[n] = 0;
	
	int p_sum = 0;
	for (int i = n - 1; i >= 0; i--) {
		if (i + t[i] > n)
			p[i] = p_sum;
		else {
			p[i] = max(p[i + 1], p[i] + p[i + t[i]]);
			p_sum = max(p_sum, p[i]);
		}
	}
	cout << p_sum << endl;

	return 0;
}