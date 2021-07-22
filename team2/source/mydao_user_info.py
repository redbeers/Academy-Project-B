import cx_Oracle
import mybatis_mapper2sql
from mylog import MyLog



class MyDaoUserInfo:
    def __init__(self):
        self.conn = cx_Oracle.connect('team2/java@192.168.41.6:1521/xe')
        self.cs = self.conn.cursor()
        self.mapper = mybatis_mapper2sql.create_mapper(xml='mybatis_user_info.xml')[0]
    
    def mydupl(self,user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_dupl")
        MyLog().getLogger().debug(sql)
        rs = self.cs.execute(sql,(user_id,))
        list = []
        for record in rs:
            list.append({'user_id':record[0]})
        return list

    
    def mylogin(self,user_id,pwd):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_login")
        MyLog().getLogger().debug(sql)
        rs = self.cs.execute(sql,(user_id,pwd))
        list = []
        for record in rs:
            list.append({'user_id':record[0],'room_seq':record[1],'user_pwd':record[2],'user_name':record[3],'user_mobile':record[4],'user_email':record[5],'user_gubun':record[6],'graduation_flag':record[7],'in_date':record[8],'in_user_id':record[9],'up_date':record[10],'up_user_id':record[11]})
        return list
            
    def myselect_list(self,user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_list")
        MyLog().getLogger().debug(sql)
#         print(sql)
        
        rs = self.cs.execute(sql,(user_id,))

        list = []
        for record in rs:
            list.append({'user_id':record[0],'room_seq':record[1],'user_pwd':record[2],'user_name':record[3],'user_mobile':record[4],'user_email':record[5],'user_gubun':record[6],'graduation_flag':record[7],'in_date':record[8],'in_user_id':record[9],'up_date':record[10],'up_user_id':record[11]})
        print(list)
        return list
    
    def myselect(self,user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select")
        MyLog().getLogger().debug(sql)
#         print(sql)
        
        rs = self.cs.execute(sql,(user_id,))

        list = []
        for record in rs:
            list.append({'user_id':record[0],'room_seq':record[1],'user_pwd':record[2],'user_name':record[3],'user_mobile':record[4],'user_email':record[5],'user_gubun':record[6],'graduation_flag':record[7],'in_date':record[8],'in_user_id':record[9],'up_date':record[10],'up_user_id':record[11]})
        return list
    
    # dddddddd
    def myselect_findId(self,user_name, user_email):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_name_email")
        MyLog().getLogger().debug(sql)
#         print(sql)
        
        rs = self.cs.execute(sql,(user_name, user_email))

        list = []
        for record in rs:
            list.append({'user_id':record[0],'room_seq':record[1],'user_pwd':record[2],'user_name':record[3],'user_mobile':record[4],'user_email':record[5],'user_gubun':record[6],'graduation_flag':record[7],'in_date':record[8],'in_user_id':record[9],'up_date':record[10],'up_user_id':record[11]})
        return list
    
    
    def myselect_findPw(self,user_id, user_email):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_id_email")
        MyLog().getLogger().debug(sql)
#         print(sql)
        
        rs = self.cs.execute(sql,(user_id, user_email))

        list = []
        for record in rs:
            list.append({'user_id':record[0],'room_seq':record[1],'user_pwd':record[2],'user_name':record[3],'user_mobile':record[4],'user_email':record[5],'user_gubun':record[6],'graduation_flag':record[7],'in_date':record[8],'in_user_id':record[9],'up_date':record[10],'up_user_id':record[11]})
        return list
    
    
    def myselect_banjang(self,room_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_banjang")
        MyLog().getLogger().debug(sql)
        
        rs = self.cs.execute(sql,(room_seq,))
        
        list=[]
        for record in rs:
            list.append({'b_id' : record[0],'b_cnt' : record[1]})
        return list
    
    
    def myselect_list_b(self):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_list_b")
        MyLog().getLogger().debug(sql)
#         print(sql)
        
        rs = self.cs.execute(sql)

        list = []
        for record in rs:
            list.append({'room_seq':record[0],'user_name':record[1],'graduation_flag':record[2]})
        return list


    
    def myselect_list_detail(self,room_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_list_detail")
        MyLog().getLogger().debug(sql)
#         print(sql)
        
        rs = self.cs.execute(sql,(room_seq,))

        list = []
        for record in rs:
            list.append({'room_seq':record[0],'user_name':record[1],'user_id':record[2],'user_gubun':record[3],'graduation_flag':record[4],' in_date':record[5],'in_user_id':record[6],'up_date':record[7],'up_user_id':record[8]})
        return list
    
    

    
    
    def myinsert(self, user_id,room_seq,user_pwd,user_name,user_mobile,user_email,user_gubun,graduation_flag,in_date,in_user_id,up_date,up_user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "insert")
        MyLog().getLogger().debug(sql)
        self.cs.execute(sql, (user_id,room_seq,user_pwd,user_name,user_mobile,user_email,user_gubun,graduation_flag,in_user_id,up_user_id))
        print("ok")
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt

    
    def myupdate(self,user_id,user_name,user_mobile,user_gubun,user_email,up_user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "update")
        MyLog().getLogger().debug(sql)
        
        self.cs.execute(sql,(user_name,user_mobile,user_gubun,user_email,user_id))
        cnt = self.cs.rowcount
    
    
    
        
        return cnt
    
    def myupdate_gflag(self,room_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "update_gflag")
        MyLog().getLogger().debug(sql)
        
        self.cs.execute(sql,(room_seq,))
        cnt = self.cs.rowcount
        print(cnt)
        
        return cnt

    
    def mydelete(self,user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "delete")
        MyLog().getLogger().debug(sql)
#         print(sql)

        self.cs.execute(sql,(user_id,))
        cnt = self.cs.rowcount
        
        return cnt
    
    
    #상빈이가 카카오 로그인
    def kakao_join(self, user_id, user_name, up_user_id, room_seq, user_pwd, user_mobile, user_email, user_gubun, graduation_flag, in_date, in_user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "kakao_merge")        
        self.cs.execute(sql, (user_id, user_name, up_user_id, room_seq, user_pwd, user_mobile, user_email, in_user_id))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt
    
    
    
    
    ###민선
    def myselect_gubun(self, user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "myselect_gubun")
        MyLog().getLogger().debug(sql)
        rs = self.cs.execute(sql,(user_id,))
        list = []
        for record in rs:
            list.append({'user_gubun':record[0]})
        return list
    
    
    def myselect_recomm(self):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_recomm")
        rs = self.cs.execute(sql)
        list = []
        for record in rs:
            list.append({'user_id':record[0]})
        return list   
 
    
    
#     위에꺼 메모리에서 지울때 실행이 된다
    def __del__(self):
        self.conn.commit()
        self.cs.close()
        self.conn.close() 
        

if __name__ == '__main__':
    dao = MyDaoUserInfo()
#     list = dao.myselect()
#     print(list)
    
#     cnt = dao.myinsert('10','10', '10', '10', '10', '10', '10', '10', '10', '10')
#     print(cnt)
    
#     cnt=dao.myupdate('10','5', '5', '5', '5', '10', '10', '10', '10', '10')
#     print(cnt)
#     
#     cnt = dao.mydelete('10')
#     print(cnt)

    list = dao.myselect_gubun()
    blist = list[0]['user_id']
    blist = list[1]['user_id']
    blist = list[2]['user_id']
    print(blist)
    
    
    
    