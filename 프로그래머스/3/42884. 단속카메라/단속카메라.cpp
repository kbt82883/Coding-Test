#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool cmp(vector<int> a, vector<int> b){
    return a[1] < b[1];
}

int solution(vector<vector<int>> routes) {
    int ans = 0;
    int camera = -30001;
    
    sort(routes.begin(), routes.end(), cmp);
    
    for (auto x : routes){
        if (camera >= x[0] && camera <= x[1]){
            continue;
        } else{
            camera = x[1];
            ans++;
        }
    }
    
    return ans;
}