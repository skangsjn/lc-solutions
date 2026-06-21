from collections import defaultdict
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        outgoing = defaultdict(str)
        cities = set()

        for path in paths:
            outgoing[path[0]] = path[1]
            cities.add(path[0])
            cities.add(path[1])
        
        return list(cities - set(outgoing.keys()))[0]