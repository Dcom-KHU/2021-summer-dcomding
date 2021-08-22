#include <iostream>
using namespace std;

int paper[10][10];
int colorpaper[5] = { 0,0,0,0,0 };
int answer = 26;

bool is_square(int x, int y, int n)
{
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (paper[x + i][y + j] == 0)
				return false;
		}
	}
	return true;
}

void glue(int x, int y, int count) {
	while (paper[x][y] == 0) {
		y++;
		if (y == 10) {
			x++;
			if (x == 10){
				if (count < answer)
					answer = count;
				return;
			}
			y = 0;
		}
	}
	if (answer <= count)
		return;

	for (int i = 5; i > 0; i--) {
		if (x + i <= 10 && y + i <= 10 && colorpaper[i] < 5 && is_square(x, y, i) == true) {
			for (int j = 0; j < i; j++) {
				for (int k = 0; k < i; k++) {
					paper[x + j][y + k] = 0;
				}
			}
			colorpaper[i]++;
			glue(x, y, count + 1);
			for (int j = 0; j < i; j++) {
				for (int k = 0; k < i; k++) {
					paper[x + j][y + k] = 1;
				}
			}
			colorpaper[i]--;
		}
	}
}

int main() {
	for (int i = 0; i < 10; i++) {
		for (int j = 0; j < 10; j++)
			cin >> paper[i][j];
	}

	glue(0, 0, 0);

	if (answer > 25)
		answer = -1;

	cout << answer << endl;

	return 0;
}