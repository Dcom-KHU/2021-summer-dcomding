#include <cstdio>
#include <cstring>

char str[1001];
int len, result;

bool checkCorrectBracket(int startPos){
	int bracketCnt[3][2] = {};
	for(int cnt = startPos; (cnt+1)%len!=startPos; ++cnt){
		char curLetter = str[cnt%len];
		int selBracket = curLetter/40-1;
		switch(curLetter){
			case '(': case '[': case '{': 
				++bracketCnt[selBracket][0];
				break;
			case ')': case ']': case '}':
				++bracketCnt[selBracket][1];
				if(bracketCnt[selBracket][0] < bracketCnt[selBracket][1])
					return false;
				break;
		}
	}
	return true;
}

int main() {
	scanf("%s",str);
	len = strlen(str);
	
	for(int cnt=0;cnt<len;++cnt)
		if(checkCorrectBracket(cnt))
			++result;
		
	printf("%d",result);
	return 0;
}