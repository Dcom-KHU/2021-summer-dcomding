#include <iostream>
#include <set>

using namespace std;

int slope[502][502];
int cases[502][502];
int dir[4][2] = { {1,0},{0,1},{-1,0},{0,-1} };
int M, N;

bool is_available(int x, int y, int i) {
	bool res = false;

	if (x + dir[i][0] > 0 && x + dir[i][0] <= M && y + dir[i][1] > 0 && y + dir[i][1] <= N) {		
		res = true;
	}

	return res;
}
int getload(int x, int y) {
	int res = 0;
	bool found = false;
	//cout << "x: " << x << ", y: " << y << "\n";
	if (cases[x][y] != -1) {
		//cout << cases[x][y] << "\n";
		return cases[x][y];
	}

	if (x == M && y == N) {
		return 1;
	}

	for (int i = 0; i < 4; i++) {
		if (is_available(x, y, i)) {
			if (slope[x][y] > slope[x + dir[i][0]][y + dir[i][1]]) {
				res += getload (x + dir[i][0], y + dir[i][1]);
			}
			
		}
	}

	//cout << res << "\n";
	cases[x][y] = res;
	return res;
}
int main() {
	cin >> M >> N;
	for (int i = 1; i <= M;i++) {
		for (int j = 1; j <= N; j++) {
			cin >> slope[i][j];
			cases[i][j] = -1;
		}
	}

	cout << getload(1, 1);
}