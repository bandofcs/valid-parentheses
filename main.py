class Solution:
    def isValid(self, s: str) -> bool:
        checklist=[0]
        for i in range(len(s)):
            if s[i]=="(":
                checklist.append(")")
            elif s[i]=="{":
                checklist.append("}")
            elif s[i]=="[":
                checklist.append("]")
            elif s[i]==checklist[-1]:
                checklist.pop()
            else:
                return False
        if len(checklist)==1:
            return True
        else:
            return False
