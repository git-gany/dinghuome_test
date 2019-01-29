import sys; sys.path.append('../')  # 将上级目录添加到sys.path中
import jsq
jsq.starttime()  # 计时器，开始计时

import os
import smtplib
import time
import CONFIG
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import parseaddr, formataddr
from email.mime.base import MIMEBase
from email import encoders

# 发送邮件
def Run_email(receiver):

    def _format_addr(s):  # 定义署名格式化函数
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    username=CONFIG.Email_send()['username']  # 发送人
    password=CONFIG.Email_send()['password']  # 授权码
    # receiver = '748809692@qq.com' # 测试数据


    # 格式化的署名和接收人信息
    message = MIMEMultipart()
    message['From'] = _format_addr('木易的邮件派送员<%s>' % username)
    message['To'] = _format_addr(receiver)
    message['Subject'] = ('接口测试报告%s' % time.strftime('%Y-%m-%d'))
    message.attach(MIMEText('接口测试报告已送达,请注意查看~'))

    # 添加html文件
    try:
        file_path = 'log/%s/%s' % (filename, report_name)
        with open(file_path, 'rb') as f:
            mime = MIMEBase(report_name, 'html', filename=report_name)
            mime.add_header('Content-Disposition', 'attachment', filename=report_name)
            mime.add_header('Content-ID', '<0>')
            mime.add_header('X-Attachment-Id', '0')
            mime.set_payload(f.read())
            encoders.encode_base64(mime)
            message.attach(mime)
    except Exception as error:
        print('写入html文件时发生异常-->>%s' % error)

    # # 添加css文件
    # try:
    #     file_path1 = 'E:/log/%s/assets/style.css' % time.strftime('%Y_%m_%d')
    #     with open(file_path1, 'rb') as f:
    #         mime1 = MIMEBase('style.css', 'css', filename='style.css')
    #         mime1.add_header('Content-Disposition', 'attachment', filename='style.css')
    #         mime1.add_header('Content-ID', '<0>')
    #         mime1.add_header('X-Attachment-Id', '0')
    #         mime1.set_payload(f.read())
    #         encoders.encode_base64(mime1)
    #         message.attach(mime1)
    # except Exception as error:
    #     print('写入html样式文件时发生异常-->>%s' % error)


    # 发送邮件!
    try:
        smtpobj=smtplib.SMTP_SSL('smtp.qq.com', 465)
        smtpobj.login(username, password)
        smtpobj.sendmail(username, [receiver], message.as_string())
        print('邮件发送成功,接收人:%s' % receiver)
        smtpobj.quit()
    except Exception as error:
        print('邮件发送失败-->>%s' % error)


print('\n正在执行测试用例···\n')

# 生成的报告名称
report_name = 'TestReport_' + time.strftime('%Y_%m_%d_%H%M%S') + '.html'

# 创建文件夹
try:
    filename = time.strftime('%Y_%m_%d')
    os.mkdir('report\%s' % filename)  # 创建文件夹
except Exception as error:
    pass
    # print('文件夹已存在，跳过创建-->>日志: %s' % error)

# 执行用例并生成html文件   # --self-contained-html   css与html合并，去除的话html与css会独立开来
os.system('py.test TestProcedure.py --html=log\%s\%s --self-contained-html' % (filename, report_name))  # 生成测试报告(css与html合并)
#os.system('py.test TestCase.py --html=log\%s\%s --self-contained-html' % (filename, report_name))  # 生成测试报告(css与html合并)

# print('py.test TestProcedure.py --html=E:\log\%s\%s --self-contained-html' % (filename, reporm_name))
print('测试报告已生成--> [ %s ]' % report_name)

os.system('rd /Q /S __pycache__')  # 清空缓存文件
print('已清除缓存--> [ __pycache__ ]')



# 发送邮件
email_list = ['raiceg@163.com']  # , '1945509914@qq.com'
for email_ in email_list:
    Run_email(email_)

jsq.overtime()  # 结束计时
jsq.sumtime()   # 运行时间


input('自动化接口用例执行完毕，按下回车键结束···')
