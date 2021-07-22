import cx_Oracle
import mybatis_mapper2sql
from mylog import MyLog

class MyDaoStoreCode:
    def __init__(self):
        self.conn = cx_Oracle.connect('team2/java@192.168.41.6:1521/xe')
        self.cs = self.conn.cursor()
        self.mapper = mybatis_mapper2sql.create_mapper(xml='mybatis_store_code.xml')[0]
        
    def myselect_list(self):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_list")
        MyLog().getLogger().debug(sql)
        
        rs = self.cs.execute(sql)
 
        list = []
        for record in rs:
            list.append({'store_seq':record[0],'store_code':record[1],'in_date':record[2],'in_user_id':record[3]})
        return list

    def myinsert(self,store_code,in_date,in_user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "insert")
        MyLog().getLogger().debug(sql)
        self.cs.execute(sql,(store_code,in_user_id))
        cnt_1 = self.cs.rowcount  
        
        return cnt_1
    
#     위에꺼 메모리에서 지울때 실행이 된다
    def __del__(self):
        self.conn.commit()
        self.cs.close()
        self.conn.close() 
        

# if __name__ == '__main__':
#     dao = MyDaoStoreInfo()
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
    
    
    
    