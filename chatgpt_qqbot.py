import pkgutil

from creart import create
from graia.ariadne.app import Ariadne
from graia.ariadne.connection.config import (
    HttpClientConfig,
    WebsocketClientConfig,
    config,
)
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.model import Group
from graia.saya import Saya

saya = create(Saya)




app = Ariadne(
    connection=config(
        1234567890,  # 你的机器人的 qq 号
        "1234567890",  # 填入你的 mirai-api-http 配置中的 verifyKey
        # 以下两行（不含注释）里的 host 参数的地址
        # 是你的 mirai-api-http 地址中的地址与端口
        # 他们默认为 "http://localhost:8080"
        # 如果你 mirai-api-http 的地址与端口也是 localhost:8080
        # 就可以删掉这两行，否则需要修改为 mirai-api-http 的地址与端口

    ),
)




with saya.module_context():
    for module_info in pkgutil.iter_modules(["modules"]):
        saya.require(f"modules.{module_info.name}")
while(1):
    app.launch_blocking()
