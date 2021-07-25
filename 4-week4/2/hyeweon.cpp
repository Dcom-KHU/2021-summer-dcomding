#include <iostream>
#include <algorithm>
using namespace std;

struct Times
{
	int start;
	int end;
};

bool schedule(Times x, Times y) {
	if (x.end != y.end)
		return x.end < y.end;
	else
		return x.start < y.start;
}

int main()
{
	int n;
	cin >> n;

	Times* times = new Times[n];
	for (int i = 0; i < n; i++) {
		cin >> times[i].start >> times[i].end;
	}
	sort(times, times + n, schedule);

	int count = 0;
	int end = -1;

	for (int i = 0; i < n; i++) {
		if (times[i].start >= end) {
			count++;
			end = times[i].end;
		}
	}

	cout << count << endl;

	return 0;
}