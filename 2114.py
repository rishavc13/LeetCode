# Return maximum number of words found in a sentence
# Runtime : 75 ms ; Memory : 13.9 MB

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        length = [len(i.split(" ")) for i in sentences]
        return max(length)