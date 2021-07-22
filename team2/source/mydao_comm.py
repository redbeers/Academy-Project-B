import cx_Oracle
import mybatis_mapper2sql
from mylog import MyLog

class MyDaoComm:
    def __init__(self):
        self.conn = cx_Oracle.connect('team2/java@192.168.41.6:1521/xe')
        self.cs = self.conn.cursor()
        self.mapper = mybatis_mapper2sql.create_mapper(xml='mybatis_comm.xml')[0]
        
    def myselect(self,search):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select")
        rs = self.cs.execute(sql,(search,))
        MyLog().getLogger().debug(sql)
        list = []
        for record in rs:
            list.append({'comm_seq':record[0],'comm_title':record[1],'comm_content':record[2],
                         'comm_hit':record[3],'del_flag':record[4],
                         'attach_file':record[5],'attach_path':record[6],'in_date':record[7],
                         'in_user_id':record[8],'up_date':record[9],'up_user_id':record[10], 
                         'cnt':record[11],'good_cnt':record[12]})
        self.conn.commit()
        return list 
    

    def myselect_detail(self,comm_seq,in_user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_detail")
        rs = self.cs.execute(sql,(comm_seq,comm_seq,in_user_id,comm_seq,comm_seq))
        obj = None
        for record in rs:
            obj = {'comm_seq':record[0],'comm_title':record[1],'comm_content':record[2],
                   'comm_hit':record[3],'del_flag':record[4],'attach_file':record[5],'attach_path':record[6],
                   'in_date':record[7],'in_user_id':record[8],'up_date':record[9],'up_user_id':record[10], 
                   'cnt':record[11],'ccnt':record[12],'totalcnt':record[13]}
        self.conn.commit()
        
        
        return obj

    def myinsert(self, comm_seq, comm_title, comm_content, comm_hit, del_flag, attach_file, attach_path, in_date, in_user_id, up_date ,up_user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "insert")
        MyLog().getLogger().debug(sql)
        self.cs.execute(sql,(comm_title, comm_content, attach_file, attach_path, in_user_id, up_user_id))
        self.conn.commit()
        self.conn.commit() 
        cnt = self.cs.rowcount  
        return cnt
    

    def myupdate_hit(self,comm_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "update_hit")
        MyLog().getLogger().debug(sql)
        self.cs.execute(sql,(comm_seq,))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt

    
    def myupdate_del(self, comm_seq,user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "update_del")
        MyLog().getLogger().debug(sql)
        self.cs.execute(sql,(user_id, comm_seq))
        cnt = self.cs.rowcount
        self.conn.commit()
        return cnt






    #민선이가한거
    def mymerge(self,user_id, comm_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "merge")
        self.cs.execute(sql,(user_id, comm_seq))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt  
    
    


    def mycountgood(self,comm_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "countgood")
        rs = self.cs.execute(sql,(comm_seq,))
        list = []
        for record in rs:
            list.append({'finalcnt':record[0]})
        self.conn.commit()
        return list



    def mygoodlist_select(self,user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "mygoodlist_select")
        rs = self.cs.execute(sql,(user_id,))
        list = []
        for record in rs:
            list.append({'comm_seq':record[0],'comm_title':record[1],'comm_content':record[2],
                         'comm_hit':record[3],'del_flag':record[4],
                         'attach_file':record[5],'attach_path':record[6],'in_date':record[7],
                         'in_user_id':record[8],'up_date':record[9],'up_user_id':record[10], 
                         'cnt':record[11],'good_cnt':record[12]})
        self.conn.commit()
        return list




    def comm_myheart(self, user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "comm_myheart")
        rs = self.cs.execute(sql, (user_id,))
        list = []
        for record in rs:
            list.append({'comm_seq':record[0],'comm_title':record[1],'comm_content':record[2],
                         'comm_hit':record[3],'del_flag':record[4],
                         'attach_file':record[5],'attach_path':record[6],'in_date':record[7],
                         'in_user_id':record[8],'up_date':record[9],'up_user_id':record[10], 
                         'cnt':record[11],'good_cnt':record[12]})
        self.conn.commit()
        return list





    def __del__(self):
        self.conn.commit()
        self.cs.close()
        self.conn.close() 




    
     
     
 
if __name__ == '__main__':
    dao = MyDaoComm()


    
    