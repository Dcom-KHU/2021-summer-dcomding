#include<iostream>
#include<string>

using namespace std;

string word;
int Min(int a, int b) {
	if (a < b)return a;
	else return b;
}

int search(int front, int rear, int value) {
	int res = 2;

	//cout << front << " " << rear << "\n";

	if (front>rear) {
		return value;

	}
	if (word[front] == word[rear]) {
		res = Min(search(front + 1, rear - 1,value), res);
	}
	if (!value) {
		res = Min(search(front + 1, rear, 1), res);
		res = Min(search(front, rear - 1, 1), res);
	}

	return res;
}
int main() {

	cin >> word;

	cout << search(0, word.size() - 1, 0) <<"\n";

}
