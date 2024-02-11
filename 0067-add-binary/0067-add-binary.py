class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = []
        #We add zeros in start if not equal length
        if len(a) > len(b):
            x = ['0' for i in range(len(a)-len(b))]
            x.append(b)
            b = ''.join(x)
        if len(b) > len(a):
            x = ['0' for i in range(len(b)-len(a))]
            x.append(a)
            a = ''.join(x)

        carry = False
        for i in range(len(a)-1,-1,-1):
            if a[i] == '1' and b[i] == '1' and carry:
                carry=True
                ans.append('1')
            elif a[i] == '1' and b[i] == '1':
                carry = True
                ans.append('0')
            elif (a[i] == '1' or b[i] == '1') and carry:
                carry = True
                ans.append('0')
            elif a[i] == '1' or b[i] == '1':
                ans.append('1')
            elif a[i] == '0' and b[i] == '0' and carry:
                carry = False
                ans.append('1')
            elif a[i] == '0' and b[i] == '0':
                ans.append('0')
                
        if carry:ans.append('1')
        return ''.join(ans[::-1])
                
        