#include <iostream>
using namespace std;

int pow(int n, int r) {
	int res = 1;
	for (int i = 0; i < r; i++) {
		res *= n;
	}
	return res;
}

int getRes(int N) {
	int res = 2, cnt = 0;
	while (N > 1) {
		N /= 2;
		cnt++;
	}

	return pow(2,cnt);
}

int main()
{
	int N ;
	cin >> N;

	cout << getRes(N);

}