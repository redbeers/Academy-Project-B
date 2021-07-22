# 필요한 라이브러리 불러오기
from flask import Flask, render_template, jsonify, request, session, escape, redirect,send_file
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
import cv2
import numpy as np
from mydao_order import MyDaoOrder
from mydao_menu import MyDaoMenu
from mydao_user_info import MyDaoUserInfo

userlist = MyDaoUserInfo().myselect_recomm()

for i in userlist:
    list_user_id = i['user_id']
    
    recomm_flag = MyDaoOrder().myselect_recomm_not(list_user_id)
    
    if len(recomm_flag) >= 9 :
        
        list = MyDaoOrder().myselect_recomm(list_user_id)
        
        menu = []
        
        for i in list:
            menu.append(i['recomm'])
            
        menu.reverse()
        
        cnt_menu  = len(menu)
        
        
        train_l=[]
        
        row, column = cnt_menu, cnt_menu*4
        train_x = [[0] * column for i in range(row)]
        
        
        for i in range(cnt_menu):
            increase = 0+i
            print(increase)
            for j in range(cnt_menu * 4):
                if j == increase:
                    if j%cnt_menu == cnt_menu-1:
                        train_x[i][j] = 1 
                        increase += 1
                    else :
                        increase = increase + cnt_menu+1
                        train_x[i][j] = 1 
                
            
        
        
        train_l_ex = train_x[cnt_menu-1]
        
        
        
        for i in range(cnt_menu):
            train_l.append(train_x[i][0:cnt_menu])
            
        train_x_n = np.array(train_x)
        train_l_n = np.array(train_l)
        
        
        model = models.Sequential()
        model.add(layers.Dense(50, activation='relu', input_shape=(cnt_menu*4,)))
        model.add(layers.Dense(cnt_menu, activation='softmax'))
        
        
        model.compile(optimizer='rmsprop',
                        loss='categorical_crossentropy',
                        metrics=['accuracy'])
        
        
        model.fit(train_x_n, train_l_n, epochs=5, batch_size=4)
        
        
        predictions = model.predict(train_x_n)
        
        
        
        print("predict" , np.argmax(predictions[0]))
        result = np.argmax(predictions[0])
        print(menu[result])
        
        list = MyDaoMenu().myselect_menu(menu[result])
        print(list)
        
        
        print('menu_seq',list[0]['menu_seq'])
        
        cnt = MyDaoMenu().myinsert_recomm(list[0]['menu_seq'], list_user_id, '', list_user_id, '', list_user_id)
        
        print(cnt)
    
