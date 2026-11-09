3. 无重复字符的最长子串
已解答
中等
相关标签
premium lock icon
相关企业
提示
给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。

 

示例 1:

输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。注意 "bca" 和 "cab" 也是正确答案。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。


     class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a=set()
        n=len(s)
        r,ans=-1,0
        for i in range(n):
            if i!=0:
                a.remove(s[i-1])
            while r+1<n and s[r+1] not in a:
                a.add(s[r+1])
                r+=1
            ans=max(ans,r-i+1)
        return ans
