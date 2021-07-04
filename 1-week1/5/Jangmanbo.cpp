#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    int n, steal, not_steal, result = 0, max = 0;
    vector<int> v;

    cin >> n;
    int* money = new int[n];
    
    steal = n / 2;
    not_steal = n - steal;

    for (int i = 0; i < not_steal; i++)
    {
        v.push_back(0);
    }
    for (int i = 0; i < steal; i++)
    {
        v.push_back(1);
    }
    
    for (int i = 0; i < n; i++)
    {
        cin >> money[i];
    }

    bool prev = true;//false∏È ¿Ã¿¸ ≈œø° »…√∆¿Ω, true∏È X
    do
    {
        for (int i = 0; i < n; i++)
        {
            if (v[i] && prev) {
                prev = false;
                result += money[i];
            }
            else if (v[i] && !prev) break;
            else prev = true;
        }
        if (result > max) max = result;
        result = 0;
        prev = true;
    } while (next_permutation(v.begin(), v.end()));
    cout << max;
    return 0;
}