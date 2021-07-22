import cx_Oracle
import mybatis_mapper2sql
from mylog import MyLog



class MyDaoNotice:
    def __init__(self):
        self.conn = cx_Oracle.connect('team2/java@192.168.41.6:1521/xe')
        self.cs = self.conn.cursor()
        self.mapper = mybatis_mapper2sql.create_mapper(xml='mybatis_notice.xml')[0]
    
            
    def myselect_list(self):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_list")
        MyLog().getLogger().debug(sql)
         
        rs = self.cs.execute(sql)
 
        list = []
        for record in rs:
            list.append({'notice_seq':record[0],'notice_title':record[1],'notice_hit':record[2]})
        return list
     
    def myselect(self,notice_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select")
        MyLog().getLogger().debug(sql)
         
        rs = self.cs.execute(sql,(notice_seq,))
 
        list = []
        for record in rs:
            list.append({'notice_seq':record[0],'notice_title':record[1],'notice_content':record[2],'attach_file':record[3],'attach_path':record[4],'notice_hit':record[5],'in_date':record[6],'in_user_id':record[7],'up_date':record[8],'up_user_id':record[9]})
        return list
     
    def myselect_seq(self):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_seq")
        MyLog().getLogger().debug(sql)
             
        rs = self.cs.execute(sql)
     
        list = []
        for record in rs:
            list.append({'max_seq':record[0]})
        return list

    def myinsert(self, notice_seq,notice_title,notice_content,attach_file,attach_path,notice_hit,in_date,in_user_id,up_date,up_user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "insert")
        MyLog().getLogger().debug(sql)
        self.cs.execute(sql, (notice_title,notice_content,attach_file,attach_path,in_user_id,up_user_id))
        print("ok")
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt
    
    
    
    def myupdate(self,notice_seq,notice_title, notice_content, attach_file, attach_path):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "update")
        MyLog().getLogger().debug(sql)
         
        self.cs.execute(sql,(notice_title, notice_content, attach_file, attach_path,notice_seq))
        cnt = self.cs.rowcount
     
     
     
         
        return cnt
    
    def myupdate_hit(self,notice_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "update_hit")
        MyLog().getLogger().debug(sql)
         
        self.cs.execute(sql,(notice_seq,))
        cnt = self.cs.rowcount
     
        return cnt
    
    
    def mydelete_img(self,notice_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "delete_img")
        MyLog().getLogger().debug(sql)
 
        self.cs.execute(sql,(notice_seq,))
        cnt = self.cs.rowcount
         
        return cnt

    
    def mydelete(self,notice_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "delete")
        MyLog().getLogger().debug(sql)
 
        self.cs.execute(sql,(notice_seq,))
        cnt = self.cs.rowcount
         
        return cnt
#     
#     def myselect_findPw(self,user_id, user_email):
#         sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_id_email")
#         MyLog().getLogger().debug(sql)
# #         print(sql)
#         
#         rs = self.cs.execute(sql,(user_id, user_email))
# 
#         list = []
#         for record in rs:
#             list.append({'user_id':record[0],'room_seq':record[1],'user_pwd':record[2],'user_name':record[3],'user_mobile':record[4],'user_email':record[5],'user_gubun':record[6],'graduation_flag':record[7],'in_date':record[8],'in_user_id':record[9],'up_date':record[10],'up_user_id':record[11]})
#         return list
#     
#     
#     def myselect_banjang(self,room_seq):
#         print(room_seq)
#         sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_banjang")
#         MyLog().getLogger().debug(sql)
#         
#         rs = self.cs.execute(sql,(room_seq,))
#         
#         list=[]
#         for record in rs:
#             list.append({'b_id' : record[0],'b_cnt' : record[1]})
#         return list
#     
#     
#     def myselect_list_b(self):
#         sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_list_b")
#         MyLog().getLogger().debug(sql)
# #         print(sql)
#         
#         rs = self.cs.execute(sql)
# 
#         list = []
#         for record in rs:
#             list.append({'room_seq':record[0],'user_name':record[1]})
#         return list
# 
#     
#     def myselect_list_detail(self,room_seq):
#         sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_list_detail")
#         MyLog().getLogger().debug(sql)
# #         print(sql)
#         
#         rs = self.cs.execute(sql,(room_seq,))
# 
#         list = []
#         for record in rs:
#             list.append({'room_seq':record[0],'user_name':record[1],'user_id':record[2],'user_gubun':record[3],'graduation_flag':record[4],' in_date':record[5],'in_user_id':record[6],'up_date':record[7],'up_user_id':record[8]})
#         return list
# 
#     
#     

# 
#     

#     
#     def myupdate_gflag(self,user_id,room_seq,user_pwd,user_name,user_mobile,user_email,user_gubun,graduation_flag,in_date,in_user_id,up_date,up_user_id):
#         sql = mybatis_mapper2sql.get_child_statement(self.mapper, "update_gflag")
#         MyLog().getLogger().debug(sql)
#         
#         self.cs.execute(sql,(room_seq,))
#         cnt = self.cs.rowcount
#         print(cnt)
#         
#         return cnt
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
    
    
    
    