class Solution:
    def getLongestSubsequence(self, words, groups):
        def build_sequence(start):
            res = []
            expect = start
            for i in range(len(words)):
                if groups[i] == expect:
                    res.append(words[i])
                    expect ^= 1
            return res
        
        seq1 = build_sequence(0)
        seq2 = build_sequence(1)
        return seq1 if len(seq1) >= len(seq2) else seq2
        
