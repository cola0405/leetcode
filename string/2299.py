class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False

        lower = False
        upper = False
        number = False
        special = False
        repeat = False

        for i in range(len(password)):
            if 'a' <= password[i] <= 'z':
                lower = True
            elif 'A' <= password[i] <= 'Z':
                upper = True
            elif '0' <= password[i] <= '9':
                number = True
            elif password[i] in "!@#$%^&*()-+":
                special = True

            if i+1 < len(password) and password[i] == password[i+1]:
                repeat = True

        return lower and upper and number and special and not repeat

