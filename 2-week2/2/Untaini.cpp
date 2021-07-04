#include <cstdio>
#include <cstring>

char str[1010];
int len, result;

bool checkCorrectBracket(int startPos){
	int bracketCnt[3] = {}, pos=startPos;
	do{
		char curLetter = str[pos%len];
		int selBracket = curLetter/40-1;
		switch(curLetter){
			case '(': case '[': case '{': 
				++bracketCnt[selBracket];
				break;
			case ')': case ']': case '}':
				--bracketCnt[selBracket];
				if(bracketCnt[selBracket]<0)
					return false;
				break;
		}
		pos=(pos+1)%len;
	}while(pos!=startPos);
	
	bool res = true;
	for(int cnt=0; cnt<3; ++cnt)
		res &= !bracketCnt[cnt];
	return res;
}

int main() {
	scanf("%s",str);
	len = strlen(str);
	
	for(int cnt=0;cnt<len;++cnt)
		if(checkCorrectBracket(cnt))
			++result;
		
	printf("%d",len%2==1?0:result);
	return 0;
}