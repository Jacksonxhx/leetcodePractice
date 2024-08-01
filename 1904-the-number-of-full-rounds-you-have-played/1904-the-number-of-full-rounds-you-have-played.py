class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        """
        转换成分钟
        """
        login = loginTime.split(':')
        logout = logoutTime.split(':')
        login = int(login[0]) * 60 + int(login[1])
        logout = int(logout[0]) * 60 + int(logout[1])
        
        if login > logout:
            logout += 1440
        if logout - login < 15:
            return 0
        
            
        while login % 15 != 0:
            login += 1
            
        while logout % 15 != 0:
            logout -= 1
        
        mins = logout - login
        
        return mins // 15