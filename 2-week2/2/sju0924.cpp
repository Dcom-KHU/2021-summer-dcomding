#include <iostream>
#include<stack>
#include<string>
using namespace std;

stack<int> st;
string s;
bool found = false;
bool is_aborted = 0;
int cnt = 0;
void clear() {

	while (!st.empty()) st.pop();
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
				st.push(1);
			}
			else if (s.at(i) == '{') {
				st.push(2);
			}
			else if (s.at(i) == '[') {
				st.push(3);
			}
			else if (s.at(i) == ')') {
				if (st.empty()||st.top()!=1) {
					is_aborted = 1;
					break;
				}

				st.pop();
			}
			else if (s.at(i) == '}') {
				if (st.empty()||st.top() != 2) {
					is_aborted = 1;
					break;
				}
				st.pop();
			}
			else if (s.at(i) == ']'||st.top() != 3) {
				if (st.empty()) {
					is_aborted = 1;
					break;
				}
				st.pop();
			}

			if (st.empty() ) {
				cnt++;
			}
			if (i == len - 1) {
				i = -1;
			}
			i++;
			if (i == start) break;
		}
		//cout << "\n";

		if (st.empty() && !is_aborted) {
			found = 1;
			break;
		}
		start++;
		clear();
	}

	if (found) cout << cnt;
	else cout << 0;
}
