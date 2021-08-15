#include <iostream>
using namespace std;

int main()
{
	int n, m;
	cin >> n >> m;

	double* blocks = new double[n];
	for (int i = 0; i < n; i++)
		cin >> blocks[i];

	double sum = blocks[n - 1];
	int answer = 1;
	for (int i = n - 2; i >= 0; i--) {
		if ((blocks[i] - m > blocks[i + 1]) || (blocks[i] + m < blocks[i + 1])) {
			answer = 0;
			break;
		}
		if ((blocks[i] - m >= sum) || (blocks[i] + m <= sum)) {
			answer = 0;
			break;
		}
		sum = (sum * (n - i - 1) + blocks[i]) / (n - i);
	}

	cout << answer << endl;
	return 0;
}