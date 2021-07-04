#include <iostream>
using namespace std;

int main()
{
	int n, k;
	cin >> n >> k;

	int sum = 0;
	int min_n = (k + 1) / 2;
	int max_n = k / 2;
	int* card = new int[n];
	int* min_array = new int[min_n];
	int* max_array = new int[max_n];

	for (int i = 0; i < n; i++) {
		cin >> card[i];
		sum += card[i];
	}

	int min_index = 0; //최소값 중 최대
	int max_index = 0; //최대값 중 최소

	for (int i = 0; i < min_n; i++) {
		min_array[i] = card[i];
		if (min_array[i] > min_array[min_index])
			min_index = i;
	}

	for (int i = 0; i < max_n; i++) {
		max_array[i] = card[i];
		if (max_array[i] < max_array[max_index])
			max_index = i;
	}

	if (max_n!=min_n && max_array[max_index] < card[max_n]) {
		max_array[max_index] = card[max_n];
		for (int j = 0; j < max_n; j++) {
			if (max_array[j] < max_array[max_index])
				max_index = j;
		}
	}

	for (int i = min_n; i < n; i++) {
		if (min_array[min_index] > card[i]) {
			min_array[min_index] = card[i];
			for (int j = 0; j < min_n; j++) {
				if (min_array[j] > min_array[min_index])
					min_index = j;
			}
		}
		if (max_array[max_index] < card[i]) {
			max_array[max_index] = card[i];
			for (int j = 0; j < max_n; j++) {
				if (max_array[j] < max_array[max_index])
					max_index = j;
			}
		}
	}

	int min_sum = 0;
	int max_sum = 0;

	for (int i = 0; i < min_n; i++) {
		min_sum += min_array[i];
	}

	for (int i = 0; i < max_n; i++) {
		max_sum += max_array[i];
	}

	cout << sum - min_sum - max_sum << endl;
}