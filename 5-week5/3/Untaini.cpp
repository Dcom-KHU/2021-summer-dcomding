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
queue<pii> reserveTimes;
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
        int minComputer = computers.size();
        pii time;
        while(!timeQueue.empty() && -iter->first <= (time = timeQueue.top()).first){
            reserveTimes.push(time);
            minComputer = min(minComputer, -time.second);
            timeQueue.pop();
        }
        
        if(!reserveTimes.size()){
            computers.push_back(1);
            timeQueue.push(make_pair(-iter->second,-computers.size()+1));
        }
        else{        
            ++computers[minComputer];
            while(!reserveTimes.empty()){
                time = reserveTimes.front(); reserveTimes.pop();
                if(minComputer == -time.second)
                    timeQueue.push(make_pair(-iter->second,time.second));
                else 
                    timeQueue.push(time);
            }
        }
    }
    
    printf("%d\n",computers.size());
    for(auto iter = computers.begin(); iter != computers.end(); ++iter)
        printf("%d ", *iter);
    
    return 0;
}
