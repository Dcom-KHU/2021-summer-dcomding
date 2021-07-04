#include <cstdio>
#include <cstring>

char str[1001];
int len, result;

bool checkCorrectBracket(int startPos){
	int bracketCnt[3][2] = {}, pos=startPos;
	do{
		char curLetter = str[pos%len];
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
		pos=(pos+1)%len;
	}while(pos!=startPos);
	
	bool result = true;
	for(int cnt=0; cnt<3; ++cnt)
		result &= (bracketCnt[cnt][0] == bracketCnt[cnt][1]);
	return result;
}

int main() {
	scanf("%s",str);
	len = strlen(str);
	
	for(int cnt=0;cnt<len;++cnt)
		if(checkCorrectBracket(cnt))
			++result;
		
	printf("%d",len==1?0:result);
	return 0;
}