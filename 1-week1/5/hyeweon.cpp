#include <iostream>
using namespace std;

int main()
{
	int n;
	int sum = 0;
	cin >> n;
	int *money = new int[n+1];
	for (int i = 0; i < n; i++)
		cin >> money[i];
	money[n] = money[0];

	for (int i = 1; i < n;) {
		if (money[i] > money[i - 1] + money[i + 1]) {
			sum += money[i];
			i += 3;
		}
		else {
			sum += (money[i - 1] + money[i + 1]);
			i += 4;
		}
	}

	cout << sum << endl;
}