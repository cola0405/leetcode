class Solution:
    def reverseMessage(self, message: str) -> str:
        return ' '.join(message.strip().split()[::-1])