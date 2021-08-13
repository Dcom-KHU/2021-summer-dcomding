#include <iostream>

using namespace std;

double blocks[200001];
double center[200001];
int n, m;

using namespace std;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int res = 1;

	cin >> n >> m;
	for (int i = 1; i <= n;i++) {
		cin >> blocks[i];
	}

	int cnt = 2;
	center[n] = blocks[n];
	for (int i = n - 1; i >= 1;i--) {
		

		if (center[i+1] >= blocks[i] + m || center[i+1] <= blocks[i] - m) {
			res = 0;
			break;
		}
		
		center[i] = (blocks[i]  + center[i + 1] * (cnt - 1)) / cnt;
		cnt++;
		
	}

	cout << res << "\n";
}
