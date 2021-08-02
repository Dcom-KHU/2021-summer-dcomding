#include <iostream>
#include <set>

using namespace std;

int main() {
	int a, b;
	cin >> a >> b;

	set<int> A, B;

	int input;
	for (int i = 0; i < a; i++) {
		cin >> input;
		A.insert(input);
	}


	for (int i = 0; i < b; i++) {
		cin >> input;
		B.insert(input);
	}

	int res = 0;

	for (auto iter = A.begin(); iter != A.end(); iter++) {
		if (B.find(*iter) != B.end()) {
			res++;
		}
	}
	   
	cout << a+b-2*res;

}