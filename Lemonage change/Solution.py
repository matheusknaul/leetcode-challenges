class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        our_wallet = []
        
        for bill in range(len(bills)):
            give_rest = []
            rest = bills[bill] - 5

            if bills[bill] == 5:
                our_wallet.append(bills[bill])

            if rest in our_wallet:
                our_wallet.remove(rest)
                our_wallet.append(bills[bill])