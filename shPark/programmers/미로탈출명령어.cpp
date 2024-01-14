#include <string>
#include <iostream>
#include <queue>
#include <tuple>

using namespace std;

int dx[] = {1, 0, 0, -1};
int dy[] = {0, -1, 1, 0};
char ds[] = {'d', 'l', 'r', 'u'};

int manhattan(int now_x, int now_y, int end_x, int end_y) {
    return abs(now_x  - end_x) + abs(now_y - end_y);
}

string solution(int n, int m, int x, int y, int r, int c, int k) {
    string answer = "";
    
    if (manhattan(x-1, y-1, r-1, c-1) > k || (manhattan(x-1, y-1, r-1, c-1) - k)%2) return "impossible";
    
    queue<tuple<int, int, int, string>> q;
    q.push(make_tuple(x-1, y-1, 0, ""));
    while (!q.empty()) {
        int now_x = get<0>(q.front());
        int now_y = get<1>(q.front());
        int cnt = get<2>(q.front());
        string now_str = get<3>(q.front());
        q.pop();
        
        if (now_x == r-1 && now_y == c-1) {
            if ((k-cnt)%2) return "impossible";
            else if (cnt == k) return now_str;
        }
        for (int i=0; i<4; i++) {
            int nx = now_x + dx[i];
            int ny = now_y + dy[i];
            string ns = now_str + ds[i];
            if (0<=nx && nx<n && 0<=ny && ny<m) {
                if (manhattan(nx, ny, r-1,c-1) + cnt + 1 > k) {
                    continue;
                }
                q.push(make_tuple(nx, ny, cnt+1, ns));
                break;
            }
        }
    }
    
    return answer;
}