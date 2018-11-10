import mysql.connector
spl_connecter = mysql.connector.connect(
    user="root",
    password="root",
    host="localhost",
    database="discord_py"
)
'''
    MEMO
    ここの処理module_main.pyで同じことしてるのであとで一つにまとめること
'''

class Command:
    def __init__(self):
        self.cur = spl_connecter.cursor()

    def CommandMC(self,UserId,ServerId):
        sql="select user_name, message_count, word_count from discord " \
            "where user_id = '{0}' and server_id = '{1}'" \
            "".format(UserId,ServerId)
        self.cur.execute(sql)
        x = self.cur.fetchall()
        xx = x[0]
        m = "```" \
            +str(xx[0])+"さんは"+str(xx[1])+"回発言し\n累計発言文字数は"\
            +str(xx[2])+"回\n一回当たりの平均使用文字数は"+str(xx[2]//xx[1])+"です。```"
        return m

    def CommandLC(self,UserId,ServerId):
        sql = "select user_name,login_count from discord " \
              "where user_id = '{0}' and server_id = '{1}'" \
              "".format(UserId,ServerId)
        self.cur.execute(sql)
        x = self.cur.fetchall()
        xx = x[0]
        m = "```"+str(xx[0])+"さんはこのサーバーで"\
            +str(xx[1])+"日発言しています。```"
        return m

    def CommandMD(self,UserId,ServerId):
        sql = "select user_name,login_count, message_count from discord " \
              "where user_id = '{0}' and server_id = '{1}'" \
              "".format(UserId,ServerId)
        self.cur.execute(sql)
        x = self.cur.fetchall()
        xx = x[0]
        m = "```"+str(xx[0])+"さんの一日当たりの平均発言回数は"\
            +str(xx[2]//xx[1])+"です。```"
        return m
    def CommandUPDATE(self,UserName,UserId):
        sql="update discord set user_name=" \
            "'{0}' where user_id ='{1}'".format(UserName,UserId)
        self.cur.execute(sql)
        m="```ユーザー名を更新しました```"
        return m

    def CommandHelp(self):
        m = "```.mc\t発言回数と発言文字数とそれらの平均を表示します。\n" \
               ".lc\t今いるサーバーで何日発言したかを表示します。\n" \
               ".md\t一日当たりの平均発言回数を表示します。\n" \
               ".update\t登録名を更新します。```"
        return m