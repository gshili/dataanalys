import time
import smtplib
from email.mime.text import MIMEText
# email 用于构建邮件内容
from email.mime.multipart import MIMEMultipart
# 用于构建附件
from email.header import Header

import datetime
import SendMail_To_Quyu

dict_name_Quyu = (
    {
        '曾少锐': 'zengsr@knowbox.cn',
        '陈煜旸': 'chenyy@knowbox.cn',
        '董文超':'dongwc@knowbox.cn',
        '刘洪超':'liuhc@knowbox.cn',
        '罗春苟':'luocg@knowbox.cn',
        '罗茄文':'luojw@knowbox.cn',
        '王志勇':'wangzy@knowbox.cn',
        '莫源波':'moyb@knowbox.cn',
        '吴泽创':'wuzc@knowbox.cn',
        '袁军':'yuanjun@knowbox.cn',
        '张凯':'zhangkai@knowbox.cn',
    }
)
path = r'D:\数据记录\新增注册学生大于5老师明细/'

for d in dict_name_Quyu.keys():
    name_Quyu = d
    to_addr = dict_name_Quyu[d]
    SendMail_To_Quyu.send_email_to_quyu(name_Quyu,to_addr,path)
    time.sleep(1)