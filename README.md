# flask_create

flask项目结构创建

创建flask项目的基本结构

蓝图创建时，在main接口文件夹中init创建蓝图，在main中子模块导入使用

蓝图注册时，在创建app文件的文件中进行注册

config配置文件:

- 配置项目相同的配置文件
- 配置mysql


manage.py文件完全控制程序的启动，

问题：无能的表现，循环导入问题
解决:双方任意一方，延迟导入，或者在使用时再导入

开启csfr保护机制

问题1：KeyError: 'A secret key is required to use CSRF.' // Werkzeug Debugger

解决：SECRET_KEY = 'y8P8rzqR0HOgWq+beq6g+KfGYw+xTLyRqr0QZCQEOXM='

问题2：The CSRF token is missing

解决：