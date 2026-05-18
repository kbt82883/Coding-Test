#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

bool cmp(pair<string,int> a, pair<string,int> b){
    return a.second > b.second;
}

bool cmp2(pair<int,int> a, pair<int,int> b){
    if (a.first == b.first){
        return a.second < b.second;
    }
    return a.first > b.first;
}

vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> ans;
    
    unordered_map<string, int> mp; //장르별 재생수
    unordered_map<string, vector<pair<int,int>>> mp2; // 장르별 노래별 재생수, 인덱스
    
    for (int i=0; i<genres.size(); i++){
        mp[genres[i]] += plays[i];
        mp2[genres[i]].push_back({plays[i], i});
    }
    
    vector<pair<string, int>> arr;
    
    for (auto x : mp){
        arr.push_back({x.first, x.second});
    }
    
    sort(arr.begin(), arr.end(), cmp);
    
    for (auto x : arr){
        sort(mp2[x.first].begin(), mp2[x.first].end(), cmp2);
        ans.push_back(mp2[x.first][0].second);
        if(mp2[x.first].size() > 1){
            ans.push_back(mp2[x.first][1].second);   
        }
    }
    
    return ans;
}