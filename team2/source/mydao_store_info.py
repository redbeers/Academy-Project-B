import cx_Oracle
import mybatis_mapper2sql
from mylog import MyLog

class MyDaoStoreInfo:
    def __init__(self):
        self.conn = cx_Oracle.connect('team2/java@192.168.41.6:1521/xe')
        self.cs = self.conn.cursor()
        self.mapper = mybatis_mapper2sql.create_mapper(xml='mybatis_store_info.xml')[0]
        
    def myselect(self):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select")
        MyLog().getLogger().debug(sql)
        
        rs = self.cs.execute(sql)
 
        list = []
        for record in rs:
            list.append({'store_seq':record[0],'store_name':record[1],'store_tel':record[2],'del_flag':record[3],'in_date':record[4],'in_user_id':record[5],'up_date':record[6],'up_user_id':record[7]})
        return list

    def myselect_d(self,store_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_d")
        MyLog().getLogger().debug(sql)
         
        rs = self.cs.execute(sql,(store_seq,))
 
        list = []
        for record in rs:
            list.append({'store_seq':record[0],'store_name':record[1],'store_tel':record[2],'del_flag':record[3],'in_date':record[4],'in_user_id':record[5],'up_date':record[6],'up_user_id':record[7]})
        return list

   
    def myselect_max(self):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_max")
        MyLog().getLogger().debug(sql)
         
        rs = self.cs.execute(sql)
 
        list = []
        for record in rs:
            list.append({'store_seq_max':record[0]})
        return list
    
    
    def myinsert(self,store_name,store_tel,in_user_id,up_user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "insert")
        MyLog().getLogger().debug(sql)
        self.cs.execute(sql,(store_name,store_tel,in_user_id,up_user_id))
        cnt = self.cs.rowcount  
        
        return cnt
    
    def myupdate(self,store_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "update_sflag")
        MyLog().getLogger().debug(sql)
        self.cs.execute(sql,(store_seq,))
        cnt = self.cs.rowcount
        print("cnt",cnt)
        
        return cnt


    def myupdate_tel(self,store_seq,store_name,store_tel,del_flag,in_date,in_user_id,up_date,up_user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "update_stel")
        MyLog().getLogger().debug(sql)
        self.cs.execute(sql,(store_tel,up_user_id,store_seq))
        cnt = self.cs.rowcount
#         print(sql)
        return cnt
#         print(cnt)

    
    def mydel_img(self,b_seq,user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "del_img")
        MyLog().getLogger().debug(sql)
        self.cs.execute(sql,(user_id,b_seq))
        cnt = self.cs.rowcount
        
        return cnt


    
#     위에꺼 메모리에서 지울때 실행이 된다
    def __del__(self):
        self.conn.commit()
        self.cs.close()
        self.conn.close() 
        

if __name__ == '__main__':
    dao = MyDaoStoreInfo()
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
    
    
    
    