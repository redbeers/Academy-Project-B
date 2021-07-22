import cx_Oracle
import mybatis_mapper2sql

class MyDaoRoom:
    def __init__(self):
        self.conn = cx_Oracle.connect('team2/java@192.168.41.6:1521/xe')
        self.cs = self.conn.cursor()
        self.mapper = mybatis_mapper2sql.create_mapper(xml='mybatis_room.xml')[0]
        
    
    def myselect(self):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "myselect")
        rs = self.cs.execute(sql,)
        self.conn.commit()
        list = []
        for record in rs:
            list.append({'room_seq':record[0], 'cnt':record[1], 'del_flag':record[2]})
        return list 
    
    
    def select_register(self):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "select_register")
        rs = self.cs.execute(sql,)
        self.conn.commit()
        list = []
        for record in rs:
            list.append({'room_seq':record[0]})
        return list 
     
    def myupdate_ntoy(self, room_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "update_ntoy")        
        self.cs.execute(sql, (room_seq,))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt
    
    
    def myupdate_yton(self, room_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "update_yton")        
        self.cs.execute(sql, (room_seq,))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt
    
    def myinsert(self, room_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "myinsert")
        self.cs.execute(sql,(room_seq,))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt
    
    
    def mycheck(self, room_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "mycheck")
        rs = self.cs.execute(sql,(room_seq,))
        self.conn.commit()
        list = []
        for record in rs:
            list.append({'cnt':record[0]})
        return list
    
    def mydelete_room(self):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "mydel_select_room")  
        rs = self.cs.execute(sql, )
        self.conn.commit()
        list = []
        for record in rs:
            list.append({'room_seq':record[0], 'cnt':record[1], 'del_flag':record[2]})
        return list
    
    def mydelete(self, room_seq):
        sql = mybatis_mapper2sql.get_child_statement(self.mapper, "mydel_room")
        self.cs.execute(sql,(room_seq,))
        self.conn.commit()
        cnt = self.cs.rowcount
        return cnt
    
    
if __name__ == '__main__':
    dao = MyDaoRoom();


