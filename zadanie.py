class Solution(object):
   def romanToInt(self, s):

      roman = {'I': 1,
               'V': 5,
               'X': 10,
               'L': 50,
               'C': 100,
               'D': 500,
               'M': 1000,
               'IV': 4,
               'IX': 9,
               'XL': 40,
               'XC': 90,
               'CD':400,
               'CM':900
               }
      i = 0
      summ = 0
      while i < len(s):
         if i + 1 < len(s) and s[i:i+2] in roman:
            summ += roman[s[i:i+2]]
            i += 2
         else:
            summ += roman[s[i]]
            i += 1
      return summ
s = Solution()

enter_num = str(input("Введите число: "))
if enter_num <= ("MMMCMXCIX"):
    if 1 <= len(enter_num) <= 15:
        print(s.romanToInt(enter_num))
    else:
        print('Длинна больше 15')
else:
    print("Введённое число превышает диапозон ")
