class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # creates an a dictonary where every new key automatically starts with an empty list
        for s in strs:
            count = [0] * 26 #creates a list with 26 0
            for c in s:
                count[ord(c) - ord('a')] += 1 #figures out wich letter is c and then increases it by a 1
            res[tuple(count)].append(s) #takes the current word s and and puts it into the correct anagram group
        return list(res.values())