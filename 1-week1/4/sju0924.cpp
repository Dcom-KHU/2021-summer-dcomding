#include <iostream>

using namespace std;

int stone[200001];
int n,k;

int nextStone(int cur) {
	for (int i = 1; i <= k; i++) {
		if (cur + i == n) return -1;
		if (stone[cur + i])return i;
	}
	return 0;
}

int Crossing() {
	int cur = 0, next, res = 0;
	while (true) {
		next = nextStone(cur);
		
		if (next == -1) {
			res++;
			cur = 0;
		}
		else if (next == 0) {
			return res;
		}
		else {
			cur += next;
			stone[cur]--;
		}
	}
}
int main() {

	
	cin >> n>>k;
	for (int i = 0; i < n; i++) {
		cin >> stone[i];
	}

	cout << Crossing();

}