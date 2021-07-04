#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
	int n;
	cin >> n;
	int *money = new int[n];
	for (int i = 0; i < n; i++)
		cin >> money[i];

	int *case1 = new int[n];
	case1[0] = case1[1] = money[0];
	int *case2 = new int[n];
	case2[0] = 0;
	case2[1] = money[1];

	for (int i = 2; i < n - 1; i++) {
		if (case1[i - 1] > case1[i - 2] + money[i]) {
			case1[i] = case1[i - 1];
		}
		else {
			case1[i] = case1[i - 2] + money[i];
		}
	}

	for (int i = 2; i < n; i++) {
		if (case2[i - 1] > case2[i - 2] + money[i]) {
			case2[i] = case2[i - 1];
		}
		else {
			case2[i] = case2[i - 2] + money[i];
		}
	}

	if (case1[n-2] > case2[n-1])
		cout << case1[n - 2] << endl;
	else
		cout << case2[n - 1] << endl;
}