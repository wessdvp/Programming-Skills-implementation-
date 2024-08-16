class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # constraints
        if not 1 <= len(bills) <= 10**5:
            print("the length of bills array should be between 1 and 10^5")
            return None
        if not all(i == 5 or i == 10 or i == 20 for i in bills):
            print("the bills accepted are only 5, 10 and 20$")
            return None
        # logic
        count_5 = 0
        count_10 = 0
        
        for bill in bills:
            if bill == 5:
                count_5 += 1
            elif bill == 10:
                if count_5 > 0:
                    count_5 -= 1
                    count_10 += 1
                else:
                    return False
            elif bill == 20:
                # Prefer to give one $10 bill and one $5 bill as change
                if count_10 > 0 and count_5 > 0:
                    count_10 -= 1
                    count_5 -= 1
                # Otherwise, give three $5 bills
                elif count_5 >= 3:
                    count_5 -= 3
                else:
                    return False
        
        return True
