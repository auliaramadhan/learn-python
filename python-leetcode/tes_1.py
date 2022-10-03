from __future__ import annotations
from functools import reduce
from typing import  Optional


class ListNode:
    def __init__(self, val: int=0, next : Optional[ListNode] = None) -> None:
        self.val = val
        self.next = next


class Solution:

    # Leetcode 1
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashDict: dict[int, int] = {}
        for i, v in enumerate(nums) :
            # data = hashDict[target - v]
            if (index := (target - v ))in hashDict :
                return [hashDict[index], i]
            else :
                hashDict[v]=i
        return[0,0]

    # Leetcode 2
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Best answer
        # root = ListNode(None)
        # zero, carry, result = ListNode(), 0, root
        # while l1 or l2 or carry:
        #     l1, l2 = l1 or zero, l2 or zero
        #     rval = l1.val + l2.val + carry
        #     carry = rval // 10
        #     result.next = ListNode(rval % 10, None)
        #     result, l1, l2 = result.next, l1.next, l2.next
        # #12:29 12:41
        # return root.next
        lData: list[int] = []
        carry = 0
        while l1 or l2 :
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            sumN = val1 + val2 + carry
            carry, sumN = sumN //10, sumN %10
            lData.append(sumN)
            l2 = l2.next if l2 else None
            l1 = l1.next if l1 else None

        # should justy do this inside while
        def setRecursiveLinked(x: ListNode, y : int) -> ListNode:
            if x.next is None :
                x.next = ListNode(y)
            else :
                x.next = setRecursiveLinked(x.next , y)
            return x

        dummy = reduce( setRecursiveLinked, lData, ListNode(lData[0]))  # type: ignore

        return dummy


    def romanToInt(self, s: str) -> int:
        dictNumber: dict[str, int] = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        total: int = 0
        prevR: str = "M"

        for r in s:
            if dictNumber[r] > dictNumber[prevR]:
                total += dictNumber[r] - dictNumber[prevR]
            else:
                total += dictNumber[r]
            prevR = r

        return total

    def intToRoman(self, num: int) -> str:
        romansDict: dict[int, str] = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }

        res = ""
        while num > 0:
            for k in reversed(romansDict):  # type: ignore
                while k <= num:
                    res += romansDict[k]
                    num -= k

        return res

    def numberToWords(self, num: int) -> str:

        res = ""
        THOUSANDS = ["", "Thousand ", "Million ", "Billion ", "Trillion "]

        LESS_THAN_TWENTY = [
            "",
            "One ",
            "Two ",
            "Three ",
            "Four ",
            "Five ",
            "Six ",
            "Seven ",
            "Eight ",
            "Nine ",
            "Ten ",
            "Eleven ",
            "Twelve ",
            "Thirteen ",
            "Fourteen ",
            "Fifteen ",
            "Sixteen ",
            "Seventeen ",
            "Eighteen ",
            "Nineteen ",
        ]

        TENS = [
            "",
            "",
            "Twenty ",
            "Thirty ",
            "Forty ",
            "Fifty ",
            "Sixty ",
            "Seventy ",
            "Eighty ",
            "Ninety ",
        ]

        if num == 0:
            return "Zero"


        divTh = 0
        while (num // 1000 ** (divTh + 1)) > 0:
            divTh += 1

        while divTh >= 0:
            modhundred = num // 1000**divTh
            if modhundred == 0 :
                num = num % 1000**divTh 
                divTh -= 1
                continue
            modTens = modhundred % 100
            modhundred //= 100
            mon20 = modTens if modTens < 20 else modTens %10
            res += f'{(LESS_THAN_TWENTY[modhundred] + "Hundred ") if modhundred > 0 else ""}{TENS[modTens//10] }{LESS_THAN_TWENTY[mon20]}{THOUSANDS[divTh]}'
            num = num % 1000**divTh 
            divTh -= 1

        return res.strip()


tes = Solution()

data = tes.twoSum([2,7,11,15],9 )
# data = tes.romanToInt("MC")
# data2 = tes.intToRoman(20)
# data3 = tes.numberToWords(1_000_000)

val1 = ListNode(1, ListNode(2, ListNode(3)))
val2 = ListNode(1, ListNode(2, ListNode(3)))

data3 = tes.addTwoNumbers(val1, val2)



print(data3)
