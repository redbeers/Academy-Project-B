import cx_Oracle
import mybatis_mapper2sql
from mylog import MyLog

class MyDaoReply:
    def __init__(self):
        self.conn = cx_Oracle.connect('team2/java@192.168.41.6:1521/xe')
        self.cs = self.conn.cursor()
        self.mapper = mybatis_mapper2sql.create_mapper(xml='mybatis_reply.xml')[0]
        
    def myselect(self, comm_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select")
        rs = self.cs.execute(sql,(comm_seq,))
        MyLog().getLogger().debug(sql)
        list = []
        for record in rs:
            list.append({'reply_seq':record[0],'comm_seq':record[1],'reply_content':record[2],'in_date':record[3],'in_user_id':record[4],'up_date':record[5],'up_user_id':record[6]})
        self.conn.commit()
        return list

 

    def myinsert(self, comm_seq, reply_content, user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "insert")
        MyLog().getLogger().debug(sql)
        self.cs.execute(sql, (comm_seq, reply_content, user_id, user_id))
        self.conn.commit()  
        cnt = self.cs.rowcount  
        return cnt
    
    
    def mydel(self, reply_seq, comm_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "del")
        MyLog().getLogger().debug(sql)
        
        self.cs.execute(sql,(comm_seq, reply_seq))
        
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt






    
     
    
     
     
 
if __name__ == '__main__':
    dao = MyDaoReply()
#     list = dao.myselect_list()
#     print(list)
 
#     obj = dao.myselect('10')
#     print(obj)
     
#     cnt = dao.myinsert("10", "1", "10", "10", "10", "10", "10", "10", "10", "10", "10")
#     print(cnt)
     
#     cnt=dao.myupdate("10", "1", "1", "1", "10", "10", "10", "10", "10", "10", "10")
#     print(cnt)
     
#    cnt = dao.mydelete('10','10')
#   print(cnt)
    
    
    
    