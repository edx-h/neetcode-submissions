/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
private:
priority_queue<int,vector<int>,greater<int>> pq;

public:
    int minMeetingRooms(vector<Interval>& intervals) {
        int counter = 0;
        sort(intervals.begin(), intervals.end(),[](const Interval& a, const Interval&b){return a.start < b.start;});
        for(const auto& m: intervals){
            if (pq.empty() || !(pq.top() <= m.start)) counter+=1;
            else pq.pop();
            pq.push(m.end);
        }
        return counter;
    }
};
