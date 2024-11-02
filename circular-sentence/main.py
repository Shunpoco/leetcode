class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        ss = sentence.split(" ")

        for i in range(len(ss)):
            if ss[i][-1] != ss[(i+1)%len(ss)][0]:
                return False

        return True

