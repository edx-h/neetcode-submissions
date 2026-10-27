class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "a" + s
        return result

    def decode(self, s: str) -> List[str]:
        self.s = s
        strs = []
        cursor = 0
        while cursor < len(self.s):
            length, len_digit = self.findPrefix(cursor)
            str_start_idx = cursor + len_digit + 1
            str_end_idx = str_start_idx + length - 1
            strs.append(s[str_start_idx:str_end_idx + 1])
            cursor = str_end_idx + 1
        return strs

    def findPrefix(self, local_cursor):
        init_idx = local_cursor
        len_digit = 0
        while self.s[local_cursor] != "a":
            local_cursor += 1
            len_digit += 1

        return int(self.s[init_idx:init_idx + len_digit]), len_digit