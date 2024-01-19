class Solution:
    def intToRoman(self, num: int) -> str:
        
        def converter(num,ans):
            if num>=1000:
                ans+= 'M'
                return num-1000,ans   
            if num>=900:
                ans+= 'CM'
                return num-900,ans  
            elif num>=500:
                ans+= 'D'
                return num-500,ans
            elif num>=400:
                ans+= 'CD'
                return num-400,ans
            elif num>=100:
                ans+= 'C'
                return num-100,ans
            elif num>=90:
                ans+= 'XC'
                return num-90,ans
            elif num>=50:
                ans+= 'L'
                return num-50,ans
            elif num>=40:
                ans+= 'XL'
                return num-40,ans
            elif num>=10:
                ans+= 'X'
                return num-10,ans
            elif num>=9:
                ans+= 'IX'
                return num-9,ans
            elif num>=5:
                ans+= 'V'
                return num-5,ans
            elif num>=4:
                ans+= 'IV'
                return num-5,ans
            
            elif num>=1:
                ans+= 'I'
                return num-1,ans
            else:
                print('error')
        
        ans = ''
        while not num <= 0:
            num,ans = converter(num,ans)
            
        return ans
        
            
            
            