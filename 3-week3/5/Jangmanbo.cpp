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

	bool loop = true;
	for (int i = 0; i <= n; i++)
	{
		if (!idx.empty() && heights[idx.top()] > heights[i])
		{
			do
			{
				height = heights[idx.top()];
				idx.pop();
				if (idx.empty())
				{
					width = i;
					loop = false;
				}
				else width = i - idx.top() - 1;
				area = max(area, height * width);
			} while (loop);
			loop = true;
		}
		idx.push(i);
	}

	cout << area;

	return 0;
}