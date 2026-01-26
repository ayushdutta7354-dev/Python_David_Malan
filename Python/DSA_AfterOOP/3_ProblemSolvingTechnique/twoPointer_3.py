# chek plaindrome:


class Palindrome:
    def isAlpha(self, str: str, i: int) -> bool:
        x = ord(str[i])
        if 97 <= x <= 122 or 45 <= x <= 57:
            return True
        else:
            return False

    def isPalindrome(self, str: str) -> bool:
        i = 0
        j = len(str) - 1

        while i < j:
            if not self.isAlpha(str, i):
                i += 1
                continue

            if not self.isAlpha(str, j):
                j -= 1
                continue
            if str[i] == str[j]:
                i += 1
                j -= 1
            else:
                return False
        return True


a = Palindrome()

print(a.isPalindrome("radar"))
print(a.isPalindrome("ayush"))
print(a.isPalindrome("121"))
print(a.isPalindrome("radar ii radar"));
