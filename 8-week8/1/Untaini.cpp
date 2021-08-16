#include <cstdio>
#include <cstring>
#define abs(a) (a>0?a:-a)

char str[100001];
int len, half, res;

int main() {
	scanf("%s",str);
	len = strlen(str)-1, half = len>>1;
	
	for(int cnt=0;cnt<=half&&res!=2;++cnt){
		if(str[cnt+(res>0)] != str[len-cnt-(res<0)])
			if(res) res=2;
			else{
				res = (str[cnt+1]==str[len-cnt]);
				if(!res) res -= (str[cnt]==str[len-cnt-1]);
				if(!res) res=2;
			}
	}
	
	printf("%d",abs(res));
	
	return 0;
}