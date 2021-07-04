#include <iostream>
using namespace std;

int N;
int Min = 1000000000;
int Max = -1000000000;
int num[11];

void cal(int result, int sum, int sub, int mul, int div, int index) {
	if (index == N) {
		if (result < Min)
			Min = result;
		if (result > Max)
			Max = result;
	}
	if (sum > 0) {
		cal(result + num[index], sum - 1, sub, mul, div, index + 1);
	}
	if (sub > 0) {
		cal(result - num[index], sum, sub - 1, mul, div, index + 1);
	}
	if (mul > 0) {
		cal(result * num[index], sum, sub, mul - 1, div, index + 1);
	}
	if (div > 0) {
		cal(result / num[index], sum, sub, mul, div - 1, index + 1);
	}
}

int main()
{
	int sum, sub, mul, div;
	cin >> N;
	for (int i = 0; i < N; i++)
		cin >> num[i];
	cin >> sum >> sub >> mul >> div;

	cal(num[0], sum, sub, mul, div, 1);
	
	cout << Max << endl;
	cout << Min << endl;
}