import mysql.connector
import tools.timelist

spl_connecter = mysql.connector.connect(
    user="root",
    password="root",
    host="localhost",
    database="discord_py"
)


class md:
    def __init__(self):
        self.cur = spl_connecter.cursor()

    def GetMember(self):
        l = []
        sql = "select user_id,server_id from discord"
        self.cur.execute(sql)
        for x in self.cur.fetchall():
            l.append(x[0] + x[1])
        return l

    def GetTodayLoginMember(self):
        l = []
        timelist = tools.timelist.timelist().CreateTimeList()
        sql = "select user_id,server_id from discord where month={0} and day ={1}".format(timelist[0], timelist[1])

        '''
            MEMO
            あとで今の時間から月と日数を取得できるモジュールを作ること
            追記
            修正済み
        '''

        self.cur.execute(sql)
        for x in self.cur.fetchall():
            l.append(x[0] + x[1])

        '''
            ここは上の関数で同じ処理をしているので後々一つの処理にまとめよう
        '''

        return l

    def InsertNewMember(self, UserName, UserId, ServerId, MessageAmount):

        timelist = tools.timelist.timelist().CreateTimeList()

        '''
            n,m,dをあとで別の関数から今の日時を取得できるようにする
            追記　修正
        '''

        sql = "insert into discord Value" \
              "('{0}','{1}','{2}',1,{3},{4},{5},1)" \
              "".format(UserId, UserName, ServerId, MessageAmount, timelist[0], timelist[1])
        try:
            self.cur.execute(sql)
            spl_connecter.commit()
        except:
            spl_connecter.rollback()
            raise
