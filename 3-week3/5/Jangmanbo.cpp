#include <iostream>
#include <stack>
#include <algorithm>
using namespace std;

int main() {
	stack<int> idx;
	int n, height, width, area = 0;
	cin >> n;
	int* heights = new int[n];
	for (int i = 0; i < n; i++)
	{
		cin >> heights[i];
	}

	for (int i = 0; i <= n; i++)
	{
		while (!idx.empty() && heights[idx.top()] > heights[i])
		{
			height = heights[idx.top()];
			idx.pop();
			if (idx.empty()) width = i;
			else width = i - idx.top() - 1;
			area = max(area, height * width);
		}
		idx.push(i);
	}

	cout << area;

	return 0;
}