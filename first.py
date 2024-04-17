palindrome = input('Введи паліндром.')
reversed = palindrome[::-1]
print(reversed)
if reversed == palindrome:
    print('Слово - є паліндромом.')
else :
    print('Слово - не є паліндромом.')