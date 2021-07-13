#include <iostream>
using namespace std;

void max_area(int end, int idx, int& width, int& height, int heights[], int& max) {
	if (idx + width > end) {
		height = 1000001;
		width = 1;
		return;
	}

	int area;
	
	if (heights[idx + width - 1] < height)
	{
		height = heights[idx + width - 1];

	}
	area = width * height;
	if (area > max) {
		max = area;
	}
	max_area(end, idx, ++width, height, heights, max);
}

int main() {
	int n;
	cin >> n;
	int* heights = new int[n];
	for (int i = 0; i < n; i++)
	{
		cin >> heights[i];
	}

	int max = 0, width = 1, height = 100001;
	for (int i = 0; i < n; i++)
	{
		max_area(n, i, width, height, heights, max);
	}
	
	cout << max;

	return 0;
}