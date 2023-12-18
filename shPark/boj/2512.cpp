#include <iostream>
#include <algorithm>
#define MAX_VAL 10001

using namespace std;

// global variables
int N, M;
int contries[MAX_VAL];

int cal_budget (int mid) {
    int tmp = 0;
    for (int i=0; i<N; i++) {
        tmp += contries[i]>mid ? mid : contries[i];
    }
    return tmp;
}

// parametric search
int para_search (int start, int end) {
    int tmp;
    int mid = (start + end) / 2;

    // escape condition
    if (start > end) return mid;

    tmp = cal_budget(mid);

    // test
    // cout << mid << " " << tmp << "\n";

    return tmp == M ? mid : tmp > M ? para_search(start, mid-1) : para_search(mid+1, end);
}


int main () {
    ios_base::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr);

    // local variable
    int res;

    // input
    cin >> N;
    for (int i=0;i<N;i++) {
        cin >> contries[i];
    }
    cin >> M;

    int max_value = *max_element(contries, contries + N);

    res = para_search(0, max_value);

    // output
    cout << res << "\n";

    return 0;
}