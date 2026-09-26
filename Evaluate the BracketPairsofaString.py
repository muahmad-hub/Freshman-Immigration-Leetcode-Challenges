class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        lookup = {}

        for key, value in knowledge:
            lookup[key] = value

        i = 0
        final = ""
        while i < len(s):
            if s[i] == "(":
                otherIndex = s.find(")", i)
                tag = s[i + 1:otherIndex]
                if tag in lookup:
                    final += lookup[tag]
                else:
                    final += "?"
                i = otherIndex + 1
            else:
                final += s[i]
                i += 1
        return final