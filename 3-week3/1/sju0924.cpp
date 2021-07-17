#include <iostream>

using namespace std;
int arr[10001];

int main() {	

	int n, k,res=0,a;
	cin >> n >> k;

	for (int i = 0; i < n; i++) {
		cin >> a;
		if (arr[a]) {
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