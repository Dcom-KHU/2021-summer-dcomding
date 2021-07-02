#include <iostream>

using namespace std;

unsigned long long int H[16] = { 0, };

int hanoi(int a,int b,int c) {
	if (a == 1)return c;
	if(!H[a]) H[a]= hanoi(a - 1,b,6-b-c) + hanoi(1,b,c) + hanoi(a - 1,6-b-c,c);
	return H[a];
}

int main() {

	int N;
	cin >> N;
	cout << hanoi(N, 1, 3) << "\n";
} 