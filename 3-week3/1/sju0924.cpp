#include <iostream>

using namespace std;
int arr[200001];

void init() {
	for (int i = 0; i <= 200000;i++) {
		arr[i] = 0;
	}
}

int main() {	

	init();
	int n, k,res=0,a;
	cin >> n >> k;

	for (int i = 0; i < n; i++) {
		cin >> a;
		if (arr[a] == 1) {
			continue;
		}
		else {
			arr[a] = 1;
			if (res < k) {
				res++;
			}
			
			
		}
	}

	cout << res;

}