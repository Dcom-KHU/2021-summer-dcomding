#include <iostream>
#include<stack>
#include<string>

using namespace std;

stack<char> front;
stack<char> back;

void printString(stack<char> *f, stack<char>*b) {
	while (!f->empty()) {
		b->push(f->top());
		f->pop();
	}


	while (!b->empty()) {
		cout << b->top();
		b->pop();
	}
	cout << "\n";
}

int main()
{
	ios::sync_with_stdio(false); 
	cin.tie(NULL); 
	cout.tie(NULL);

	int n;
	string input;
	char c;
	
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> input;
		for (int cur = 0; cur < input.size();cur++) {
			switch (input[cur]) {
			case '-':
				if (!front.empty()) {
					front.pop();
				}
				break;
			case '<':
				if (!front.empty()) {
					back.push(front.top());
					front.pop();
				}
				break;
			case '>':
				if (!back.empty()) {
					front.push(back.top());
					back.pop();
				}
				break;
			default:
				front.push(input[cur]);
			}

			//cout << "front : " << front.size() << "letter, back : " << back.size() << " letter \n";
			//printString(front, back);

		}

		printString(&front, &back);

	}

}
