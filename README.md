# chatgpt_qqbot
从安装Python开始，逐步教学如何在自己的电脑上部署属于自己的ChatGPT机器人


step0:配置Mirai环境

Mirai挂上机器人QQ的教程:https://wiki.mrxiaom.top/mirai
Mirai显示登陆成功即可继续下一步

step1:基本配置参数
打开chatgpt_qqbot.py
修改你的bot的QQ号,以及mirai-http的监听端口(如果你没有改动，请忽略)


step2:打开moduel文件夹的ero.py
修改为你自己的ChatGPT API


之后直接运行chatgpt_qqbot.py即可

注:本项目部署依赖于120$的API,如果API的每分钟可调用次数过低，会导致内容无法完全生成
