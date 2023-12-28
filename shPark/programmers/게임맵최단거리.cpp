#include<vector>
#include<queue>

using namespace std;

int solution(vector<vector<int> > maps)
{
    int answer = -1;
    int x, y, nx, ny;
    int n = maps.size();
    int m = maps[0].size();
    int visited[n][m];
    int dx[] = {1, 0, -1, 0};
    int dy[] = {0, 1, 0, -1};
    
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            visited[i][j] = 0;
        }
    }
    
    // bfs
    queue<pair<int, int>> que;
    visited[0][0] = 1;
    que.push(make_pair(0, 0));
    while(!que.empty()) {
        x = que.front().first;
        y = que.front().second;
        que.pop();
        
        if (x==n-1 && y==m-1) {
            answer = visited[x][y];
            break;
        }
        
        for (int i=0; i<4; i++) {
            nx = x + dx[i];
            ny = y + dy[i];
            if (0<=nx && nx<n && 0<=ny && ny<m && maps[nx][ny]==1 && visited[nx][ny]==0) {
                que.push(make_pair(nx, ny));
                visited[nx][ny] = visited[x][y] + 1;
            }
        }
    }
    
    return answer;
}