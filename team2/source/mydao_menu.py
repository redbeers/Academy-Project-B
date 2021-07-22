import cx_Oracle
import mybatis_mapper2sql
from mylog import MyLog

class MyDaoMenu:
    def __init__(self):
        self.conn = cx_Oracle.connect('team2/java@192.168.41.6:1521/xe')
        self.cs = self.conn.cursor()
        self.mapper = mybatis_mapper2sql.create_mapper(xml='mybatis_menu.xml')[0]
        
    def myselect(self,store_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select")
        MyLog().getLogger().debug(sql)
         
        rs = self.cs.execute(sql,(store_seq,))
 
        list = []
        for record in rs:
            list.append({'menu_seq':record[0],'store_seq':record[1],'menu_name':record[2],'menu_price':record[3],'del_flag':record[4],'in_date':record[5],'in_user_id':record[6],'up_date':record[7],'up_user_id':record[8]})
#         print(list)
        return list
    
    
    
    def myselect_menu(self,menu_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_menu")
        MyLog().getLogger().debug(sql)
         
        rs = self.cs.execute(sql,(menu_seq,))
 
        list = []
        for record in rs:
            list.append({'menu_seq':record[0],'menu_name':record[1]})
#         print(list)
        return list
    
    
    
    
    def myinsert(self,store_seq,menu_name,menu_price,del_flag,in_date,in_user_id,up_date,up_user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "insert")
        MyLog().getLogger().debug(sql)
        self.cs.execute(sql,(store_seq, menu_name,menu_price,in_user_id,up_user_id))
        cnt = self.cs.rowcount  
        
        return cnt
    
    def myupdate(self,store_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "update_sflag")
        MyLog().getLogger().debug(sql)
        self.cs.execute(sql,(store_seq,))
        cnt = self.cs.rowcount
        
        return cnt

    def myupdate_menu(self,menu_seq,store_seq,menu_name,menu_price,del_flag,in_date,in_user_id,up_date,up_user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "update_munu")
        MyLog().getLogger().debug(sql)
        self.cs.execute(sql,(menu_name,menu_price,del_flag,up_user_id,menu_seq))
        cnt = self.cs.rowcount
        
        return cnt
    
    
    def myinsert_recomm(self,menu_seq, user_id, in_date, in_user_id, up_date, up_user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "insert_recomm")
        MyLog().getLogger().debug(sql)
        self.cs.execute(sql,(menu_seq, user_id, in_user_id, up_user_id))
        self.conn.commit()
        cnt = self.cs.rowcount  
        return cnt


    
#     위에꺼 메모리에서 지울때 실행이 된다
    def __del__(self):
        self.conn.commit()
        self.cs.close()
        self.conn.close() 
        

if __name__ == '__main__':
    dao = MyDaoMenu()
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
    
    
    
    