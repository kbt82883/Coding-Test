#include <string>
#include <vector>

using namespace std;

double solution(vector<int> arr) {
    double sum = 0;
    for (int x : arr){
        sum+=x;
    }
    return sum/arr.size();
}