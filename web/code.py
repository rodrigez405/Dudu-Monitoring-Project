# -*- coding: utf-8 -*- 
#!/usr/bin/python

import web
import json, MySQLdb

########################################################################
# 网站访问地址设置，一般设置为服务器的ip地址或者域名+端口号
# 端口号默认为8080，可以在执行code.py文件时设置其它端口号
# 例如执行"python code.py 8089"，那么端口号就应该为8089
url = 'http://localhost:8080'

# 网站基本信息配置
config = web.storage(
    # 网站名称，显示在导航栏的LOGO位置
    site_name = U"Dudu Montior",
    # 网站描述，显示在网页窗口标题的位置
    site_desc = U'',
    # 以下三项请勿修改
    root =  url + '',
    refer = url + '/',
    static = url + '/static',
)

# 数据库连接配置，host=数据库服务器地址，user=用户名，pw=密码，db=数据库名称
db = web.database(dbn='mysql', host="localhost", user='root', pw='root', db='cancer')
# 自定义配置区结束，请勿修改以下内容 #
########################################################################

render = web.template.render('templates/')

web.template.Template.globals['render'] = render
web.template.Template.globals['config'] = config

# route
urls = (
    '/', 'index',
)

class index:
    def GET(self):
        return render.index('index')

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
