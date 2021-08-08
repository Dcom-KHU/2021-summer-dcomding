#include <iostream>
using namespace std;



int main()
{
	int n;
	cin >> n;

	int answer = 1;
	for (int i = 0; n >= 2; i++) {
		answer = answer * 2;
		n = n / 2;
	}

	cout << answer << endl;
}