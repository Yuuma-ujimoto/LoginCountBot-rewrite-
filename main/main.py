import discord
import module.module_main
import wordcount.wordcount
import command.cmd
import tools.timelist
import log.writelog
import Botconfig.BotConfig

timelist = tools.timelist.timelist().CreateTimeList()
# bot起動時の日時取得
client = discord.Client()

login_member = module.module_main.md().GetMember()
# 既に登録されているユーザーの情報取得
today_login_member = module.module_main.md().GetTodayLoginMember()


# 今日既にログインしたユーザーの取得

@client.event
async def on_ready():
    print("console log -> ログイン完了")
    print("--------------------------")


@client.event
async def on_message(message):
    global login_member
    global today_login_member
    global timelist

    nowtimelist = tools.timelist.timelist().CreateTimeList()
    # 起動時と日時が違っている
    Sender = message.author
    UserId = str(Sender.id)

    if message.server != None:
        ServerId = str(message.server.id)
        if timelist[0] != nowtimelist[0] or timelist[1] != nowtimelist[1]:
            timelist = nowtimelist
            today_login_member = []
            print("console log -> 日付が更新されました")
            print("----------------------------------")
        if UserId + ServerId in login_member:
            wordcount.wordcount.DiscrdCount().word_count(UserId, ServerId, len(message.content))
            if UserId + ServerId not in today_login_member:
                wordcount.wordcount.DiscrdCount().login_count(UserId, ServerId)
                today_login_member.append(UserId + ServerId)

                print("console log -> ユーザーがログインしました\nユーザー名" + Sender.name)
                print("---------------------------------------")

        else:
            module.module_main.md().InsertNewMember(
                Sender.name,
                UserId,
                ServerId,
                len(message.content)
            )
            login_member.append(UserId + ServerId)
            today_login_member.append(UserId + ServerId)

            print("console log -> ユーザーが登録されました\nユーザー名" + Sender.name)
            print("--------------------------------------")

        command_ = message.content
        ServerName = message.server.name
        UserName = message.author.name
        # 各コマンドに必要な変数の確保

        if command_ == ".mc":
            log.writelog.writelog().Log(UserName, ServerName, ".mc")
            m = command.cmd.Command().CommandMC(
                UserId,
                ServerId
            )
            await client.send_message(message.channel, str(m))
        if command_ == ".lc":
            log.writelog.writelog().Log(UserName, ServerName, ".lc")
            m = command.cmd.Command().CommandLC(
                UserId,
                ServerId
            )
            await client.send_message(message.channel, str(m))
        if command_ == ".md":
            log.writelog.writelog().Log(UserName, ServerName, ".md")
            m = command.cmd.Command().CommandMD(
                UserId,
                ServerId
            )
            await client.send_message(message.channel, str(m))
        if command_ == ".update":
            log.writelog.writelog().Log(UserName, ServerName, ".update")
            m = command.cmd.Command().CommandUPDATE(
                Sender.name,
                UserId
            )
            await client.send_message(message.channel, str(m))
        if command_ == ".help":
            log.writelog.writelog().Log(UserName, ServerName, ".help")
            m = command.cmd.Command().CommandHelp()
            await client.send_message(message.channel, str(m))


client.run(config.BotConfig.BotToken)
