# USTC-JWC-Login

中国科学技术大学 教务系统 统一身份认证登录

例程见 `example.py` 

获取 `CAS_LT` 部分取自 [Kobe972/ustc-passport-login](https://github.com/Kobe972/ustc-passport-login) 

该脚本能够绕过验证码并登录教务系统

`requests` 顺序：

 - 请求 `login` 获取 `CAS_LT`
 - 请求 `validatecode` 获取验证码图片
 - 向 `login` 发送账号密码
 - 获取重定向链接 `Location` ，并向 `CAS` 申请 `ST`
 - 在重定向链接中查找 `fineReportPw` ，并计算 `fine_password`
 - 向 `domain` 发送 `fine_username` 与 `fine_password`