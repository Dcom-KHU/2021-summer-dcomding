#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int operation(int num[], vector<int> v) {
    int result = num[0], size = v.size();
    for (int i = 0; i < size; i++)
    {
        switch (v[i])
        {
        case 0:
            result += num[i + 1];
            break;
        case 1:
            result -= num[i + 1];
            break;
        case 2:
            result *= num[i + 1];
            break;
        case 3:
            result /= num[i + 1];
            break;
        default:
            break;
        }
    }
    return result;
}

int main() {
    int N, result, min = 1000000000, max = -1000000000;
    vector<int> v;
    cin >> N;
    int* num = new int[N];
    int op[4];
    for (int i = 0; i < N; i++)
    {
        cin >> num[i];
    }
    for (int i = 0; i < 4; i++)
    {
        cin >> op[i];
        for (int j = 0; j < op[i]; j++)
        {
            v.push_back(i);
        }
    }
    do {
        result = operation(num, v);
        if (result < min) min = result;
        if (result > max) max = result;
    } while (next_permutation(v.begin(), v.end()));
    cout << max << "\n" << min;
    return 0;
}