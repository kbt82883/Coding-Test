#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(int n, vector<vector<int>> edge) {
    int ans = 0;
    
    vector<vector<int>> graph(n+1);
    
    for (auto x : edge){
        graph[x[0]].push_back(x[1]);
        graph[x[1]].push_back(x[0]);
    }
    
    queue<int> q;
    q.push(1);
    vector<int> dist(n+1, -1); //-1 : 방문 안함
    dist[1] = 0;
    
    while(!q.empty()){
        int curr = q.front();
        q.pop();
        
        for (int nxt : graph[curr]){
            if (dist[nxt] == -1){
                q.push(nxt);
                dist[nxt] = dist[curr]+1;
            }
        }
    }
    
    int mx = -1;
    for (int x : dist){
        if (mx < x){
            mx = x;
        }
    }
    
    for (int x : dist){
        if (mx == x){
            ans++;
        }
    }
    
    return ans;
}