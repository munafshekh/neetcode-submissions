class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        # 'act' : ["act", "cat"]
        # 'opts': ["pots", "tops", "stop"]


        for i in range(len(strs)):
            
            curr_string = ' '.join(sorted(strs[i]))

            if curr_string not in map:
                map[curr_string] = [strs[i]]
            else:
                map[curr_string].append(strs[i])
        
        return list(map.values())
            
        