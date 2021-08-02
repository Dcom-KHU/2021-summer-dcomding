#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    while (1)
    {
        unsigned long long n;
        int answer = 0;
        int i=1;
        cin >> n;
        // for(; i<=n; i*=2)
        // {
        //     if(i > n) break;
        // }
        int log_val = log2l(n);
        cout << (unsigned long long)pow(2, log_val) << "\n";
    }
    
    
    

    
}