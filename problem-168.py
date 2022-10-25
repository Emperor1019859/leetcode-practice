class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        border = [0,26]
        loop_count = 1
        for n in range(2,10):
            border.append(pow(26,n) + border[-1])

        for i in range(len(border)):
            if columnNumber <= border[i]:
                loop_count = i
                break

        for _ in range(loop_count):
            int_result, remainder = divmod(columnNumber, 26)
            if remainder:
                Letter = chr(64 + remainder)
                columnNumber = int_result
            else:
                Letter = "Z"
                columnNumber = int_result - 1
            result = Letter + result

        return result