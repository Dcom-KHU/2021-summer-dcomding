#include <iostream>
#include<algorithm>

using namespace std;

int main() {

	int N, K, front,rear, res = 0;
	int arr[100001];
	cin >> N >> K;
	
	for (int i = 0; i < N; i++) {
		cin >> arr[i];
	}
	
	sort(arr, arr + N);

	front = K / 2;
	rear = N -1 - (K / 2);

	if (K % 2 == 1) front++;

	for (int i = front; i <= rear;i++) {
		res += arr[i];
	}

	cout << res;
}