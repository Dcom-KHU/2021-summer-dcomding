#include <cstdio>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

#define pii pair<int,int>

int n, st, ed;
vector<pii> timetable;
vector<int> computers;
priority_queue<pii> timeQueue;

int main()
{
    scanf("%d",&n);
    for(int cnt=0; cnt<n; ++cnt){
        scanf("%d%d",&st,&ed);
        timetable.push_back(make_pair(st,ed));
    }
    
    sort(timetable.begin(), timetable.end());
    computers.push_back(0);
    timeQueue.push(make_pair(0,0));
    
    for(auto iter = timetable.begin(); iter != timetable.end(); ++iter){
        pii time = timeQueue.top();

        if(-iter->first>time.first){
            computers.push_back(1);
            timeQueue.push(make_pair(-iter->second,computers.size()-1));
        }
        else{
            timeQueue.pop();
            ++computers[time.second];
            timeQueue.push(make_pair(-iter->second,time.second));
        }
    }
    
    printf("%d\n",computers.size());
    for(auto iter = computers.begin(); iter != computers.end(); ++iter)
        printf("%d ", *iter);
    
    return 0;
}
