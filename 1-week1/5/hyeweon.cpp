#include <iostream>
using namespace std;

int main()
{
	int n;
	int sum1 = 0;
	int sum2 = 0;
	cin >> n;
	int *money = new int[n+2];
	for (int i = 0; i < n; i++)
		cin >> money[i];
	money[n] = money[0];
	money[n+1] = money[1];

	for (int i = 1; i < n;) {
		if (money[i] > money[i - 1] + money[i + 1]) {
			sum1 += money[i];
			i += 3;
		}
		else {
			sum1 += (money[i - 1] + money[i + 1]);
			i += 4;
		}
	}

	for (int i = 2; i < n;) {
		if (money[i] > money[i - 1] + money[i + 1]) {
			sum2 += money[i];
			i += 3;
		}
		else {
			sum2 += (money[i - 1] + money[i + 1]);
			i += 4;
		}
	}
	if (sum1 > sum2)
		cout << sum1 << endl;
	else
		cout << sum2 << endl;
}