class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        n = len(transactions)
        for i in range(n):
            transactions[i] = transactions[i].split(',')
        
        res = []
        for i, transaction in enumerate(transactions):
            if int(transaction[2]) > 1000:
                res.append(','.join(transaction))
                continue
            
            for j in range(n):
                if transactions[j][0] == transaction[0]:
                    if abs(int(transactions[j][1]) - int(transaction[1])) <= 60 and transactions[j][3] != transaction[3]:
                        res.append(','.join(transaction))
                        break

        return res