#include <iostream>
using namespace std;

int sum = 0;

void hanoi(int n, int from, int to, int temp) {
	if (n == 1) 
		sum += to;
	else {
		hanoi(n - 1, from, temp, to);
		sum += to;
		hanoi(n - 1, temp, to, from);
	}
}

int main()
{
	int n;
	cin >> n;
	hanoi(n, 1, 3, 2);
	cout << sum << endl;
}