#include <cstdio>

#define max(x,y) (x>y?x:y)

int n, v, fenwickTree[100010], distanceFromRoot[100010], result;

void update(int num, int val){
    while(num<=n)
        fenwickTree[num] += val, num += (num & -num);
}

int sumOneToNum(int num){
    int res = 0;
    while(num)
        res += fenwickTree[num], num -= (num & -num);
    return res;
}

int binarySearch(int val){
    int left = 1, right = n, mid;
    while(left <= right){
        mid = (left+right)/2;
        
        if(sumOneToNum(mid) <= val) left = mid+1;
        else right = mid-1;
    }
    return left;
}

int main() {
    scanf("%d", &n); n+=2;
    update(1,1);
    update(n,1);
    for(int cnt=2; cnt<n; ++cnt){
        scanf("%d", &v); ++v;
        int vSum = sumOneToNum(v), left = binarySearch(vSum-1), right = binarySearch(vSum);
        result += (distanceFromRoot[v] = max(distanceFromRoot[left], distanceFromRoot[right])+1);
        update(v, 1);
        printf("%d\n", --result);
    }
    return 0;
}
