#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

#define pii pair<int, int>

int n, s, e, curEnd, result;
vector<pii> times;
int main()
{
    scanf("%d",&n);
    for(int cnt=0; cnt<n; ++cnt){
        scanf("%d%d",&s,&e);
        times.push_back(make_pair(e, s));
    }
    
    sort(times.begin(), times.end());
    
    for(int cnt=0; cnt<n; ++cnt){
        s = times[cnt].second, e = times[cnt].first;
        if(curEnd <= s)
            ++result, curEnd = e;
    }
    
    printf("%d", result);
    return 0;
}
