#include <cstdio>
#include <stack>
using namespace std;

char str[1000001];

//left는 커서 왼쪽에 있는 문자열, right는 커서 오른쪽에 있는 문자열임
stack<char> left, right;

int main() {
	scanf("%s", str);
	for(int cnt=0; str[cnt]; ++cnt){
		switch(str[cnt]){
			case '<':
				//왼쪽에 문자가 있으면 오른쪽 스택에 옮김 == 커서를 왼쪽으로 옮김
				if(!left.empty()){
					right.push(left.top());
					left.pop();
				}
				break;
			case '>':
				//오른쪽에 문자가 있으면 왼쪽 스택에 옮김 == 커서를 오른쪽으로 옮김
				if(!right.empty()){
					left.push(right.top());
					right.pop();
				}
				break;
			case '-':
				//왼쪽에 문자열이 있을 때 문자를 하나 지움 == 커서를 기준으로 왼쪽에 있는 문자 하나 지움
				if(!left.empty())
					left.pop();
				break;
			default:
				//왼쪽 스택에 문자를 넣음 == 문자를 입력하고 커서를 왼쪽으로 옮김
				left.push(str[cnt]);
		}
	}
	
	//커서를 왼쪽 끝으로 보냄
	while(!left.empty()){
		right.push(left.top());
		left.pop();
	}
	
	//커서를 오른쪽으로 하나씩 옮기면서 지나온 문자 출력
	while(!right.empty()){
		printf("%c",right.top());
		right.pop();
	}
	return 0;
}