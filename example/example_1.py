# encoding: utf-8
# 最简单的工作流，使用logger的一个简单实例

from qg_botsdk.qg_bot import BOT
from qg_botsdk.model import *


def deliver(data: MESSAGE):
    print(data)
    bot.logger.debug(data)
    bot.logger.info('收到消息啦！')
    if '你好' in data.treated_msg:
        bot.send_msg('你好，世界', str(data.id), str(data.channel_id))


if __name__ == '__main__':
    bot = BOT(bot_id='', bot_token='', is_private=True, is_sandbox=True, max_shard=1)
    bot.bind_msg(deliver, treated_data=True)
    bot.start()
