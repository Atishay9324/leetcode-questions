class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int>mp;
        vector<int>vec;
        for(int i=0; i<nums.size(); i++){
            int ab = target - nums[i];
            if(mp.count(ab)){
                vec.push_back(i);
                vec.push_back(mp[ab]);
                return vec;
            }
            else mp[nums[i]]=i;
        }
        return vec;
    }
};