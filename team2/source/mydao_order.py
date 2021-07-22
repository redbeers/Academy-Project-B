import cx_Oracle
import mybatis_mapper2sql

class MyDaoOrder:
    def __init__(self):
        self.conn = cx_Oracle.connect('team2/java@192.168.41.6:1521/xe')
        self.cs = self.conn.cursor()
        self.mapper = mybatis_mapper2sql.create_mapper(xml='mybatis_order.xml')[0]
        
    def myselect_list(self,user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_list")
        
        rs = self.cs.execute(sql,(user_id,))

        list = []
        for record in rs:
            list.append({'store_name':record[0],'menu_name':record[1],'order_cnt':record[2],'menu_price':record[3],'in_date':record[4],'in_user_id':record[5],'pay_flag':record[6]})
        return list
     
    
    
    def mypay_flag(self,room_seq,store_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "update_flag")
#         MyLog().getLogger().debug(sql)
        self.cs.execute(sql,(room_seq,store_seq))
        cnt = self.cs.rowcount
         
        return cnt
     
    def myselect_recomm(self,user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_recomm")
        
        rs = self.cs.execute(sql,(user_id,))

        list = []
        for record in rs:
            list.append({'recomm':record[0]})
        return list

    def myselect_recomm_menu(self,user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_recomm_menu")
        rs = self.cs.execute(sql,(user_id,))
        list = []
        for record in rs:
            list.append({'menu_seq':record[0]})
        return list


    def myselect_recomm_not(self,user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_recomm_not")
        
        rs = self.cs.execute(sql,(user_id,))

        list = []
        for record in rs:
            list.append({'recomm':record[0]})
        return list

    ############################################################
    #민선
    
    def myselect_graph(self):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_store")
        rs = self.cs.execute(sql, )
        list = []
        for r in rs:
            list.append({'store':r[0]})
        
        
        mlist = []
        for i in list:
            num = i['store']
            #print(num)
            sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_graph")
            ls = self.cs.execute(sql, (num,))
            
            nlist = []
            
            for r in ls:
                nlist.append({'room':r[0],'cnt':r[1], 'indate':r[2]})
            mlist.append(nlist)
            
        return mlist
    
    def mystore_name_select(self):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_storename")
        rs = self.cs.execute(sql, )
        slist = []
        for record in rs:
            slist.append({'store_name':record[0], 'store_seq':record[1]})
        return slist 
    
    
    def mymenu_name_select(self, store_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_menulist")
        rs = self.cs.execute(sql, (store_seq,))
        mlist = []
        for record in rs:
            mlist.append({'menu_name':record[0], 'menu_price':record[1], 'menu_seq':record[2]})
        return mlist 
 
    
    def myadmin_select(self, search):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "admin_select")
        rs = self.cs.execute(sql, (search,))
        list = []
        for record in rs:
            list.append({'in_date':record[0],'user_name':record[1],'user_id':record[2],'store_name':record[3],'menu_name':record[4],'sum':record[5]} )
        return list 
    
  #이름 검색
    def myadmin_select_name(self, name):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "admin_select_name")
        rs = self.cs.execute(sql, (name,))
        list = []
        for record in rs:
            list.append({'in_date':record[0],'user_name':record[1],'user_id':record[2],'store_name':record[3],'menu_name':record[4],'sum':record[5]} )
        return list 
        
    def myadmin_select_date(self, date):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "admin_select_date")
        rs = self.cs.execute(sql, (date,))
        list = []
        for record in rs:
            list.append({'in_date':record[0],'user_name':record[1],'user_id':record[2],'store_name':record[3],'menu_name':record[4],'sum':record[5]} )
        return list     
    
    
    def select_store_detail(self, store_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_store_detail")
        rs = self.cs.execute(sql, (store_seq,))
        list = []
        for record in rs:
            list.append({'mname':record[0], 'sum':record[1], 'sname':record[2]})
        return list 
     
    def order_menu_select(self, store_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "order_menu")
        rs = self.cs.execute(sql, (store_seq,))
        mlist = []
        for record in rs:
            mlist.append({'menu_seq':record[0], 'menu_name':record[1], 'menu_price':record[2]})
        return mlist 
 
 
 
    def orderinsert(self,menu_seq, order_cnt, user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "myorderinsert")
        self.cs.execute(sql, (menu_seq, order_cnt, user_id))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt
    
    
    def banjang_select(self, user_id):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_store")
        rs = self.cs.execute(sql, )
        list = []
        for r in rs:
            list.append({'store':r[0]})
        
        
        mlist = []
        for i in list:
            num = i['store']
            
            sql = mybatis_mapper2sql.get_child_statement(self.mapper, "banjang_select")
            ls = self.cs.execute(sql, (user_id, num))
            
            nlist = []
            
            for r in ls:
                nlist.append({'store_seq':r[0],'store_name':r[1],'menu_name':r[2], 'menu_price':r[3], 'order_cnt':r[4], 'store_code':r[5],'menu_seq':r[6],'room_seq':r[7],'in_date':r[8]})
            mlist.append(nlist)
            
        return mlist
    
    
    def myselect_pay_flag(self,room_seq,store_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_pay_flag")
        
        rs = self.cs.execute(sql,(room_seq,store_seq,))

        list = []
        for record in rs:
            list.append({'order_seq':record[0],'pay_flag':record[1],'menu_seq':record[2],'store_seq':record[3],'in_date':record[4]})
        
        print(list)
        return list


    
    def myselect_sms(self,store_seq,room_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "sms_list")
        rs = self.cs.execute(sql,(store_seq,room_seq))
 
        txt_room = ""
        txt_tel = ""
        txt_msg = ""
        
        txt_header = ""
        txt_content = ""
        txt_footer = ""
        
        tot_price = 0
        sms_list = []
        for record in rs:
            txt_tel     = record[3]
            txt_room    = record[1]
            tot_price += int(record[5])
            txt_content += record[2]+" "+str(record[4])+"개"+"\n"
            
            sms_list.append({'store_seq':record[0],'room_seq':record[1],'menu_name':record[2],'store_tel':record[3],'order_cnt':record[4],'order_sum':record[5]})
       
        txt_header += str(txt_room)+"호 주문내역"+"\n"
        txt_footer += "총"+str(tot_price)+"원 입금되었습니다."+"\n"
       
       
        txt_msg += txt_header
        txt_msg += txt_content
        txt_msg += txt_footer
        
        print("txt_tel",txt_tel)
        print("txt_msg",txt_msg)
       
        return txt_tel,txt_msg
    
    def order_person(self, menu_seq, room_seq, in_date):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "order_person")
        rs = self.cs.execute(sql, (menu_seq, room_seq, in_date))
        mlist = []
        for record in rs:
            mlist.append({'user_id':record[0], 'user_name':record[1]})
        return mlist 
    
#     위에꺼 메모리에서 지울때 실행이 된다
    def __del__(self):
        self.conn.commit()
        self.cs.close()
        self.conn.close() 
 
if __name__ == '__main__':
    dao = MyDaoOrder()
    cnt = dao.banjang_select('S00001')
    print(cnt)

#     list = dao.mystore_name_select()
#     print(list)
    

    
    
    
    