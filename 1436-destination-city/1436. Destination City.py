class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        has_outgoing = set()

        for i in range(len(paths)):
            has_outgoing.add(paths[i][0])
        
        for i in range(len(paths)):
            city = paths[i][1]
            if city not in has_outgoing:
                return city
        
        return ''