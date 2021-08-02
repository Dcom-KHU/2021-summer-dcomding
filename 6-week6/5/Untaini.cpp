#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int n, x;
long long k;
bool endPro[200010];
vector<pair<int, int>> proCntList;
int main()
{
    scanf("%d%lld", &n, &k);
    for(int cnt=0; cnt<n; ++cnt){
        scanf("%d",&x);
        proCntList.push_back(make_pair(x,cnt));
    }
    
    sort(proCntList.begin(), proCntList.end());
    
    int prevProCnt=0, selPro=-1;
    for(int cnt=0; cnt<n; ++cnt){
        int pro = proCntList[cnt].second, proCnt = proCntList[cnt].first;
        long long diff = (long long)(n-cnt)*(proCnt-prevProCnt);
            
        if(diff > k){
            selPro=0, k%=n-cnt;
            while(endPro[selPro] || k) k-=(!endPro[selPro++]);
            break;
        }
        else k -= diff, endPro[pro] = 1, prevProCnt = proCnt;
    }
    
    printf("%d", selPro);
    return 0;
}
