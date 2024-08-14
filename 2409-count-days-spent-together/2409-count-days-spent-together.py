class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        """
        遍历365天，全部转换成天
        """
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        n = len(months)
        prefix = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + months[i - 1]
        
        arriveAlice, leaveAlice, arriveBob, leaveBob = arriveAlice.split('-'), leaveAlice.split('-'), arriveBob.split('-'), leaveBob.split('-')
        arriveAliceTime = prefix[int(arriveAlice[0]) - 1] + int(arriveAlice[1])
        print(arriveAliceTime)
        leaveAliceTime = prefix[int(leaveAlice[0]) - 1] + int(leaveAlice[1])
        arriveBobTime = prefix[int(arriveBob[0]) - 1] + int(arriveBob[1])
        leaveBobTime = prefix[int(leaveBob[0]) - 1] + int(leaveBob[1])
        
        res = 0
        for i in range(1, 366):
            if arriveAliceTime <= i <= leaveAliceTime and arriveBobTime <= i <= leaveBobTime:
                res += 1
                
        return res