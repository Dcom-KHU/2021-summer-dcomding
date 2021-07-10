#include <iostream>
#include<stack>
#include<string>
using namespace std;

stack<int> st1,st2,st3;
string s;
bool found = false;
bool is_aborted = 0;
int cnt = 0;
void clear() {
	while (!st1.empty()) st1.pop();
	while (!st2.empty()) st2.pop();
	while (!st3.empty()) st3.pop();
	is_aborted = 0;
	cnt = 0;
}


int main()
{
	cin >> s;
	int len = s.length();
	int start = 0, end = len - 1;
	

	while (start<len) {
		//cout << "start : " << start << " end: " << end<<"\n";
		int i = start;
		while (true) {
			//cout << s.at(i) ;
			if (s.at(i) == '(') {
				st1.push(1);
			}
			else if (s.at(i) == '{') {
				st2.push(1);
			}
			else if (s.at(i) == '[') {
				st3.push(1);
			}
			else if (s.at(i) == ')') {
				if (st1.empty()) {
					is_aborted = 1;
					break;
				}
				st1.pop();
			}
			else if (s.at(i) == '}') {
				if (st2.empty()) {
					is_aborted = 1;
					break;
				}
				st2.pop();
			}
			else if (s.at(i) == ']') {
				if (st3.empty()) {
					is_aborted = 1;
					break;
				}
				st3.pop();
			}

			if (st1.empty() && st2.empty() && st3.empty()) {
				cnt++;
			}
			if (i == len - 1) {
				i = -1;
			}
			i++;
			if (i == start) break;
		}
		//cout << "\n";

		if (st1.empty() && st2.empty() && st3.empty() && !is_aborted) {
			found = 1;
			break;
		}
		start++;
		clear();
	}

	if (found) cout << cnt;
	else cout << 0;
}
