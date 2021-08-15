#include <iostream>
using namespace std;

int main()
{
	int n, m;
	cin >> n >> m;

	int* blocks = new int[n];
	for (int i = 0; i < n; i++)
		cin >> blocks[i];

	double sum = blocks[n - 1];
	for (int i = n - 2; i >= 0; i--) {
		if ((blocks[i] - m > blocks[i + 1]) || (blocks[i] + m < blocks[i + 1])) {
			cout << "0" << endl;
			return 0;
		}
		if ((blocks[i] - m >= sum) || (blocks[i] + m <= sum)) {
			cout << "0" << endl;
			return 0;
		}
		sum = (sum * (n - i - 1) + blocks[i]) / double(n - i);
	}

	cout << "1" << endl;
	return 0;
}