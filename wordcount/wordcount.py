import mysql.connector
import tools.timelist

spl_connecter = mysql.connector.connect(
    user="root",
    password="root",
    host="localhost",
    database="discord_py"
)
class DiscrdCount:
    def __init__(self):
        self.cur =spl_connecter.cursor()

    def word_count(self,UserId,ServerId,len):
        sql ="update discord set message_count = message_count+1,word_count = word_count+{0} where user_id ='{1}' and server_id = '{2}'".format(len,UserId,ServerId)

        try:
            self.cur.execute(sql)
            spl_connecter.commit()
        except:
            spl_connecter.rollback()
            raise

    def login_count(self,UserId,ServerId):

        dt = tools.timelist.timelist().CreateTimeList()
        '''
        memo
        ここのdatetimeも最終的には一か所に統合すること
        追記 修正
        '''
        sql="update discord set login_count = login_count+1,month = {0},day = {1} where user_id ='{2}' and server_id = '{3}'".format(dt[0],dt[1],UserId,ServerId)

        try:
            self.cur.execute(sql)
            spl_connecter.commit()
        except:
            spl_connecter.rollback()
            raise