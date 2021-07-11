#include <iostream>
using namespace std;

void toBinary(int num, int arr[]) {
	for (int i = 1; i < 5; i++)
	{
		arr[i] = num % 2;
		num /= 2;
	}
}

int main() {
	int bits[16];
	int binary[5];
	int check[5];
	int sum = 0;
	for (int i = 1; i < 16; i++)
	{
		cin >> bits[i];
	}
	for (int i = 1; i < 5; i++)
	{
		for (int j = 1; j < 16; j++)
		{
			toBinary(j, binary);
			sum += binary[i] * bits[j];
		}
		check[i] = sum % 2;
		sum = 0;
	}

	for (int i = 1; i < 5; i++)
	{
		sum += check[i] * pow(2, i - 1);
	}
	if (sum)
	{
		bits[sum] = abs(bits[sum] - 1);
	}

	sum = 0;
	int data = 0;

	for (int i = 3; i < 16; i++)
	{
		if (i != 4 && i != 8) {
			sum += bits[i] * pow(2, data);
			data++;
		}
	}
	cout << sum;
}
