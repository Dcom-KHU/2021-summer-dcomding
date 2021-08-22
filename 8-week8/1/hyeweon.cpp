#include <iostream>
#include <string>
using namespace std;

int main()
{
	string word;
	cin >> word;
	int n = word.size();
	int answer = 0;
	bool first = true;

	for (int front = 0, back = n - 1; front < back; front++, back--) {
		if (word[front] == word[back])
			continue;
		else if (word[front + 1] == word[back]) {
			if (first == true) {
				first = false;
				front++;
				answer = 1;
			}
			else {
				answer = 2;
				break;
			}
		}
		else if (word[front] == word[back - 1]) {
			if (first == true) {
				first = false;
				back--;
				answer = 1;
			}
			else {
				answer = 2;
				break;
			}
		}
		else {
			answer = 2;
			break;
		}
	}

	cout << answer << endl;

	return 0;
}