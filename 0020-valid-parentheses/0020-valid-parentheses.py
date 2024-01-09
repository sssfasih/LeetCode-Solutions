class Solution:
    def isValid(self, s: str) -> bool:
        lst = []
        while s:
            a,s = s[0],s[1::]
            
            if lst == []:
                if a in ['[','(','{']:
                    lst.append(a)
                else:
                    return False
            else:
                if a in ['[','(','{']:
                    lst.append(a)
                else:
                    if a == "}" and lst[-1] != '{':
                        return False
                    elif a == ")" and lst[-1] != '(':
                        return False
                    elif a == "]" and lst[-1] != '[':
                        return False
                    else:

                        lst = lst[:-1:]
            
            
        if lst:
            return False
        else:
            return True
        