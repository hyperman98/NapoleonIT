class Solution: 
    def romanToInt(self, s: str) -> int:
        romanDict= {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        numbers = []
        res = 0

        #разбиваем на отдельные символы
        for i in romanSymbols:
            numbers.append(romanDict[i])

        #все собираем и выводим
        for i,j in zip(numbers[:-1], numbers[1:]) :
            if i >= j:
                res += i 
            else : 
                res -= i
        res += numbers[-1]
        print(f'Ответ: {summ}')    

if __name__ == "__main__":
    s = input()
    convert = Solution().romanToInt(s)