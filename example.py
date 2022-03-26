from login import Login

uid = "PB19190810"
pwd = "LyeaChanKawaii~"

login = Login(uid, pwd)

session = login.login()

print(session.cookies)