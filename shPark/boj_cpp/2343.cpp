#include <iostream>
#define MAX_VAL 100001

using namespace std;

int N, M;
int values[MAX_VAL];

int main () {
    iostream::sync_with_stdio(false);cin.tie(nullptr);cout.tie(nullptr);

    cin >> N >> M;
    int sum_val = 0;
    int max_len = 0;
    for (int i=0; i<N; i++) {
        cin >> values[i];
        sum_val += values[i];
        max_len = max(max_len, values[i]);
    }

    int left = max_len;
    int right = sum_val;
    int res;

    while (left <= right) {
        int mid = (left + right) / 2;
        int cnt = 0;
        int record = 0;

        for (int i=0; i<N; i++) {
            if ((record + values[i]) > mid) {
                cnt++;
                record = 0;
            }
            record += values[i];
        }

        if (record > 0) {
            cnt++;
        }

        if(cnt <= M) {
            right = mid - 1;
        }
        else {
            left = mid + 1;
        }
    }

    cout << left << "\n";

    return 0;
}