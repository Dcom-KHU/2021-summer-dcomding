#include <cstdio>
#include <stack>
using namespace std;

char str[1000001];
stack<char> left, right;

int main() {
	scanf("%s", str);
	for(int cnt=0; str[cnt]; ++cnt){
		switch(str[cnt]){
			case '<':
				if(!left.empty()){
					right.push(left.top());
					left.pop();
				}
				break;
			case '>':
				if(!right.empty()){
					left.push(right.top());
					right.pop();
				}
				break;
			case '-':
				if(!left.empty())
					left.pop();
				break;
			default:
				left.push(str[cnt]);
		}
	}
	
	while(!left.empty()){
		right.push(left.top());
		left.pop();
	}
	
	while(!right.empty()){
		printf("%c",right.top());
		right.pop();
	}
	return 0;
}