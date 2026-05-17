#include <string>
#include <vector>
#include <queue>

using namespace std;

long long solution(int n, vector<int> works) {
    long long ans = 0;
    
    priority_queue<int> pq;
    
    int total = 0;
    for (int x : works){
        pq.push(x);
        total+=x;
    }
    
    if (total <= n){
        return 0;
    }
    
    while (n-- > 0){
        int tmp = pq.top();
        pq.pop();
        pq.push(tmp-1);
    }
    
    while (!pq.empty()){
        int tmp = pq.top();
        pq.pop();
        
        ans += tmp * tmp;
    }
    
    return ans;
}