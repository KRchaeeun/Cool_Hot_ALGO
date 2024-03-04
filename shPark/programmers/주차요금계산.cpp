#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>

using namespace std;

map<string, pair<int, int>> info;
int basic_time, basic_fee, unit_time, unit_fee;

int stacked_time(string key_val, int exit_time) {
    return exit_time - info[key_val].first + info[key_val].second;
}

int cal_fee(string key_val, int total_time) {
    // 23:59 == 1439
    if (info[key_val].first != 0 || (info[key_val].first == 0 && total_time == 0)) {
        total_time += 1439 - info[key_val].first;
    }
    if (total_time <= basic_time) {
        return basic_fee;
    } else {
        int return_value =  (total_time - basic_time) / unit_time;
        if ((total_time - basic_time) % unit_time == 0) {
            return basic_fee + return_value * unit_fee;
        }
        return basic_fee + (return_value + 1) * unit_fee;
    }
}

vector<int> solution(vector<int> fees, vector<string> records) {
    vector<int> answer;
    basic_time = fees[0];
    basic_fee = fees[1];
    unit_time = fees[2];
    unit_fee = fees[3];
    
    for(int i=0; i<records.size(); i++) {
        string key_val = records[i].substr(6, 4);
        int time_min = stoi(records[i].substr(0,2)) * 60 + stoi(records[i].substr(3,2));
        
        if (records[i].substr(11) == "IN") {
            int tmp_value = 0;
            if (info.count(key_val) == 1) {
                tmp_value = info[key_val].second;
            }
            info[key_val] = make_pair(time_min, tmp_value);
        } else {
            info[key_val] = make_pair(0, stacked_time(key_val, time_min));
            // cout << info[key_val].second << " ";
        }
    }
    
    // map<int, pair<int, int>>::iterator it;
    for (auto it = info.begin(); it!=info.end(); it++) {
        answer.push_back(cal_fee(it->first, it->second.second));
    }

    return answer;
}