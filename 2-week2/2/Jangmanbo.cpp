#include <iostream>
#include <string>
#include <stack>
using namespace std;

int main() {
	string s, change;
	stack<char> stack;
	bool check = true;

	cin >> s;
	change = s;

	int num = 0, size = s.size();
	
	do
	{
		for (int i = 0; i < size; i++)
		{
			if (change[i] == '(' || change[i] == '{' || change[i] == '[') {
				stack.push(change[i]);
			}
			else {
				switch (change[i])
				{
				case ')':
					if (stack.empty() || stack.top() != '(') { check = false; }
					else { stack.pop(); }
					break;
				case '}':
					if (stack.empty() || stack.top() != '{') { check = false; }
					else { stack.pop(); }
					break;
				case ']':
					if (stack.empty() || stack.top() != '[') { check = false; }
					else { stack.pop(); }
					break;
				default:
					break;
				}
				if (!check) { break; }
			}
			
		}
		if (check && stack.empty()) { num++; }
		
		while (!stack.empty())
		{
			stack.pop();//스택 비우기
		}
		check = true;
		change = change.substr(1, size) + change[0];
	} while (s != change);
	
	cout << num;
	return 0;
}
