import cx_Oracle
import mybatis_mapper2sql
from mylog import MyLog



class MyDaoQna:
    def __init__(self):
        self.conn = cx_Oracle.connect('team2/java@192.168.41.6:1521/xe')
        self.cs = self.conn.cursor()
        self.mapper = mybatis_mapper2sql.create_mapper(xml='mybatis_qna.xml')[0]
    
            
    def myselect_list(self):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_list")
        MyLog().getLogger().debug(sql)
         
        rs = self.cs.execute(sql)
 
        list = []
        for record in rs:
            list.append({'qna_seq':record[0],'qna_title':record[1],'qna_content':record[2],'qna_answer':record[3],'del_flag':record[4],'attach_file':record[5],'attach_path':record[6],'in_date':record[7],'in_user_id':record[8],'up_date':record[9],'up_user_id':record[10]})
        return list
     
    def myselect(self,qna_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select")
        MyLog().getLogger().debug(sql)
          
        rs = self.cs.execute(sql,(qna_seq,))
  
        list = []
        for record in rs:
            list.append({'qna_seq':record[0],'qna_title':record[1],'qna_content':record[2],'qna_answer':record[3],'del_flag':record[4],'attach_file':record[5],'attach_path':record[6],'in_date':record[7],'in_user_id':record[8],'up_date':record[9],'up_user_id':record[10]})
        return list
      
    def myselect_seq(self):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_seq")
        MyLog().getLogger().debug(sql)
              
        rs = self.cs.execute(sql)
      
        list = []
        for record in rs:
            list.append({'max_seq':record[0]})
        return list
 
    def myinsert(self, qna_seq,qna_title,qna_content,attach_file,attach_path,in_user_id,up_user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "insert")
        MyLog().getLogger().debug(sql)
        self.cs.execute(sql, (qna_title,qna_content,attach_file,attach_path,in_user_id,up_user_id))
        print("ok")
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt
    
    def myinsert_answer(self, qna_seq,qna_answer):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "insert_answer")
        MyLog().getLogger().debug(sql)
        self.cs.execute(sql, (qna_answer,qna_seq))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt
    
    def mydelete_answer(self,qna_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "delete_answer")
        MyLog().getLogger().debug(sql)
  
        self.cs.execute(sql,(qna_seq,))
        cnt = self.cs.rowcount
          
        return cnt
    
    def mydelete(self,qna_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "delete")
        MyLog().getLogger().debug(sql)
  
        self.cs.execute(sql,(qna_seq,))
        cnt = self.cs.rowcount
          
        return cnt

#     
#     
#     
#     def myupdate(self,notice_seq,notice_title, notice_content, attach_file, attach_path):
#         sql = mybatis_mapper2sql.get_child_statement(self.mapper, "update")
#         MyLog().getLogger().debug(sql)
#          
#         self.cs.execute(sql,(notice_title, notice_content, attach_file, attach_path,notice_seq))
#         cnt = self.cs.rowcount
#      
#      
#      
#          
#         return cnt
#     
#     def myupdate_hit(self,notice_seq):
#         sql = mybatis_mapper2sql.get_child_statement(self.mapper, "update_hit")
#         MyLog().getLogger().debug(sql)
#          
#         self.cs.execute(sql,(notice_seq,))
#         cnt = self.cs.rowcount
#      
#         return cnt
#     
#     

# 
#     


#     

    
#     위에꺼 메모리에서 지울때 실행이 된다
    def __del__(self):
        self.conn.commit()
        self.cs.close()
        self.conn.close() 
        

# if __name__ == '__main__':
#     dao = MyDaoUserInfo()
#     list = dao.myselect()
#     print(list)
    
#     cnt = dao.myinsert('10','10', '10', '10', '10', '10', '10', '10', '10', '10')
#     print(cnt)
    
#     cnt=dao.myupdate('10','5', '5', '5', '5', '10', '10', '10', '10', '10')
#     print(cnt)
#     
#     cnt = dao.mydelete('10')
#     print(cnt)
    
    
    
    