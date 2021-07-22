from flask import Flask, render_template, jsonify, request, session, escape, redirect,send_file
from mydao_user_info import MyDaoUserInfo
from mydao_order import MyDaoOrder
import smtplib                             
from email.mime.text import MIMEText
from mydao_notice import MyDaoNotice
from werkzeug.utils import secure_filename
from datetime import datetime
import os
from mydao_room import MyDaoRoom
from mydao_store_info import MyDaoStoreInfo
from mydao_menu import MyDaoMenu
from mydao_qna import MyDaoQna
from mydao_comm import MyDaoComm
from mydao_reply import MyDaoReply
from mydao_store_code import MyDaoStoreCode
import requests
import sys
from sdk.api.message import Message
from sdk.exceptions import CoolsmsException



DIR_UPLOAD = "Y:/"


app = Flask(__name__,static_url_path="", static_folder="static")
app.secret_key = "ABCDEFG"   










# -------------------------------------------------------------------------------------------------------
# 상빈
@app.route('/dupl.ajax', methods=['POST'])
def dupl_ajax_render():
    
    user_id = request.form["user_id"]
    
    list = MyDaoUserInfo().mydupl(user_id)

    msg = ""
    if len(list) == 1:
        msg = "ng"
    else:
        msg = "ok"
    return jsonify(msg=msg)

@app.route("/register")
def room_select_render():
    flag_ses,  user_id = getSession()
    
    list = MyDaoRoom().select_register()
    return render_template('register.html', list=list, enumerate=enumerate)



@app.route('/register.ajax', methods=['POST'])
def register_ajax_render():
    user_id = request.form["user_id"]
    room_seq = request.form["room_seq"]
    user_pwd = request.form["user_pwd"]
    user_name = request.form["user_name"]
    user_mobile = request.form["user_mobile"]
    
    user_email = request.form["user_email"]
    user_gubun = "s"
    graduation_flag = "n"
    
    cnt = MyDaoUserInfo().myinsert(user_id, room_seq , user_pwd, user_name, user_mobile, user_email, user_gubun, graduation_flag, "", user_id, "", user_id)
    
    msg = ""
    if cnt == 1:
        msg = "ok"
    else:
        msg = "ng"

    return jsonify(msg=msg)


@app.route('/send_number.ajax', methods=['POST'])
def send_number_ajax():
    user_email = request.form["user_email"]
    email_ran = request.form["email_ran"]
    
    msg = ""
    if True:
        smtpName = "smtp.naver.com"  # smtp 서버 주소
        smtpPort = 587  # smtp 포트 번호
        
        sendEmail = "qkrtkdqls21@naver.com"
        password = "asdf753!@"
        recvEmail = user_email
        
        title = "나도시락 이메일 인증번호 입니다."  # 메일 제목
        content = "이메일 인증칸에 넣어주세요\n 메일 인증번호는 " + email_ran + " 입니다."    
        
        msg = MIMEText(content)  # MIMEText(text , _charset = "utf8")
        msg['From'] = sendEmail
        msg['To'] = recvEmail
        msg['Subject'] = title
        
#         print(msg.as_string())                        
        
        s = smtplib.SMTP(smtpName , smtpPort)  # 메일 서버 연결
        s.starttls()  # TLS 보안 처리
        s.login(sendEmail , password)  # 로그인
        s.sendmail(sendEmail, recvEmail, msg.as_string())  # 메일 전송, 문자열로 변환하여 보냅니다.
        s.close()  # smtp 서버 연결을 종료합니다.
        
        msg = "ok"
    else:
        msg = "ng"
    return jsonify(msg=msg)

# comm==================================================
@app.route("/comm")
def comm_render():
    flag_ses, user_id = getSession()
    if not flag_ses:
        return redirect("login.html")   
    comm_seq = request.args.get('comm_seq')
    search = request.args.get('comm_title_search', '')
    list   = MyDaoComm().myselect(search)
    
    return render_template('comm.html', list=list)




####gms 나나나나 수정 
# comm_detail==================================================
@app.route("/comm_detail", methods=['GET'])
def comm_detail_render():
    flag_ses, user_id = getSession()
    comm_seq    = request.args.get('comm_seq')
    
    obj         = MyDaoComm().myselect_detail(comm_seq, user_id) #커뮤니티글을 보여준다.
    list_reply  = MyDaoReply().myselect(comm_seq)#댓글을 보여준다.
    hit         = MyDaoComm().myupdate_hit(comm_seq)#좋아요보여준다.
    return render_template('comm_detail.html', obj=obj, list_reply=list_reply, hit=hit)



@app.route("/comm_detail_del")
def comm_detail_del_render():
    comm_seq = request.args.get('comm_seq')
    user_id = escape(session['user_id'])
    
    cnt = MyDaoComm().myupdate_del(comm_seq, user_id)
    return redirect('/comm')




#0416내가 좋아요 한 리스트만 select
@app.route("/comm_myheart")
def comm_myheart_render():
    flag_ses,  user_id = getSession()
    if not flag_ses:
        return redirect("login.html")
    
    user_id = request.args.get('user_id')
    list = MyDaoComm().comm_myheart(user_id);
    
    return render_template('comm_myheart.html', list=list)

  


#좋아요한거
@app.route("/comm_like_upd.ajax", methods=['POST'])
def comm_like_upd_render():
    flag_ses,  user_id = getSession()
    comm_seq =request.form["comm_seq"]
    
    cnt = MyDaoComm().mymerge(user_id, comm_seq)
    list = MyDaoComm().mycountgood(comm_seq)
    
    finalcnt = list[0]['finalcnt']
    
    msg = ""
    if cnt == 1:
        msg = "ok"
    else:
        msg = "ng"

    return jsonify(msg = msg, finalcnt=finalcnt)
    






# comm_add ==================================================
@app.route("/comm_add")
def comm_add_render():
    return render_template('comm_add.html')


@app.route("/comm_addact", methods=['POST'])
def comm_addact_render():
    flag_ses, user_id = getSession()
    if not flag_ses:
        return redirect("login.html")    
    
    comm_title = request.form["comm_title"]
    comm_content = request.form["comm_content"]
    file = request.files['file']
    attach_file_temp = secure_filename(file.filename)
    attach_path_temp = str(datetime.today().strftime("%Y%m%d%H%M%S")) + "_" + attach_file_temp 
    
    file.save(os.path.join(DIR_UPLOAD, attach_path_temp))
    
    attach_path = ""
    attach_file = ""
    if file:
        attach_path = attach_path_temp
        attach_file = attach_file_temp
        print("file o")
    else:
        print("file x")   
    
    cnt = MyDaoComm().myinsert('', comm_title, comm_content, '', '', attach_file, attach_path, '', user_id, '', user_id)
    return render_template('comm_addact.html', cnt=cnt, enumerate=enumerate)







# reply===================================================
@app.route('/reply_list.ajax', methods=['POST'])
def reply_list_render():
    comm_seq = request.form['comm_seq']
    
    blist  = MyDaoReply().myselect(comm_seq)#댓글을 보여준다.
    return jsonify(blist = blist)


@app.route('/reply_insert.ajax', methods=['POST'])
def reply_insert_render():
    flag_ses, user_id = getSession()
    if not flag_ses:
        return redirect("login.html") 
    
    comm_seq        = request.form["comm_seq"]
    reply_content   = request.form["reply_content"]
    user_id = escape(session['user_id'])
     
    cnt = MyDaoReply().myinsert(comm_seq, reply_content, user_id)
 
    msg = ""
    if cnt == 1:
        msg = "ok"
    else:
        msg = "ng"
    return jsonify(msg=msg)


@app.route('/reply_del.ajax', methods=['POST'])
def reply_del_render():
    reply_seq   = request.form["reply_seq"]
    comm_seq    = request.form["comm_seq"]
    print('reply_seq=',reply_seq)
    print('comm_seq=',comm_seq)
    
    cnt = MyDaoReply().mydel(reply_seq, comm_seq)
    
    msg = ""
    if cnt == 1:
        msg = "ok"
    else:
        msg = "ng"
    return jsonify(msg=msg)









































































































































#######################################################################
#예진
@app.route("/")
@app.route("/home")
def main_render():
    list = MyDaoNotice().myselect_list()
    list_len = len(list)
    print(list)
    print(list_len)
    return render_template('home.html', list=list , list_len=list_len,enumerate=enumerate)


@app.route("/find_id") 
def find_id_render():
    return render_template('find_id.html')

@app.route("/find_pwd")
def find_pwd_render():
    return render_template('find_pwd.html')


@app.route('/login.ajax', methods=['POST'])
def login_ajax():
    user_id =request.form["user_id"]
    pwd =request.form["pwd"]
    list =MyDaoUserInfo().mylogin(user_id, pwd)
    msg=""
    if len(list)==1:
        session["user_id"] = list[0]['user_id']
        session["user_name"] = list[0]['user_name']
        session["user_gubun"] = list[0]['user_gubun']
        msg="ok"
    else:
        msg="ng"
    return jsonify(msg=msg)

@app.route('/find_id.ajax', methods=['POST'])
def find_id_ajax():
    user_name =request.form["user_name"]
    user_email =request.form["user_email"]
    
    list =MyDaoUserInfo().myselect_findId(user_name, user_email)
    
    msg=""
    if len(list)==1:
        smtpName = "smtp.naver.com"                  # smtp 서버 주소
        smtpPort = 587                               # smtp 포트 번호
        
        sendEmail = "jung_ye_jin@naver.com"
        password = "uichan0303"
        recvEmail = user_email
        
        title = "나도시락 아이디입니다."                                 # 메일 제목
        content = "나도시락을 이용해주셔서 감사합니다~~\n당신의 아이디는 " + list[0]['user_id'] + " 입니다."                                # 메일 내용
        
        msg = MIMEText(content)                       # MIMEText(text , _charset = "utf8")
        msg['From'] = sendEmail
        msg['To'] = recvEmail
        msg['Subject'] = title
        
        
        s = smtplib.SMTP(smtpName , smtpPort)         # 메일 서버 연결
        s.starttls()                                  # TLS 보안 처리
        s.login(sendEmail , password)                 # 로그인
        s.sendmail(sendEmail, recvEmail, msg.as_string())  # 메일 전송, 문자열로 변환하여 보냅니다.
        s.close()                                     # smtp 서버 연결을 종료합니다.
        
        msg="ok"
    else:
        msg="ng"
    return jsonify(msg=msg)


@app.route('/find_pwd.ajax', methods=['POST'])
def find_pwd_ajax():
    user_id =request.form["user_id"]
    user_email =request.form["user_email"]
    
    list =MyDaoUserInfo().myselect_findPw(user_id, user_email)
    
    msg=""
    if len(list)==1:
        smtpName = "smtp.naver.com"                  # smtp 서버 주소
        smtpPort = 587                               # smtp 포트 번호
        
        sendEmail = "jung_ye_jin@naver.com"
        password = "uichan0303"
        recvEmail = user_email
        
        title = "나도시락 비밀번호입니다."                                 # 메일 제목
        content = "나도시락을 이용해주셔서 감사합니다~~\n당신의 비밀번호는는 " + list[0]['user_pwd'] + " 입니다."                                # 메일 내용
        
        msg = MIMEText(content)                       # MIMEText(text , _charset = "utf8")
        msg['From'] = sendEmail
        msg['To'] = recvEmail
        msg['Subject'] = title
        
        
        s = smtplib.SMTP(smtpName , smtpPort)         # 메일 서버 연결
        s.starttls()                                  # TLS 보안 처리
        s.login(sendEmail , password)                 # 로그인
        s.sendmail(sendEmail, recvEmail, msg.as_string())  # 메일 전송, 문자열로 변환하여 보냅니다.
        s.close()                                     # smtp 서버 연결을 종료합니다.
        
        msg="ok"
    else:
        msg="ng"
    return jsonify(msg=msg)


@app.route('/logout')
def logout_render():
    session.clear()
    return redirect('home')

def getSession():
    user_id = ""
    try:
        user_id = str(escape(session['user_id']))
    except:
        pass
    
    if user_id == "":
        return False, user_id
    else:
        return True, user_id

@app.route('/mypage')
def mypage_render():
    flag_ses,  user_id = getSession()
    
    if not flag_ses:
        return redirect("login.html")
    
    
    
    list =MyDaoUserInfo().myselect(user_id)
    
    print(list)
    
    return render_template('mypage.html',list=list)


@app.route("/mypage_mod")
def mypage_mod_render():
    flag_ses,  user_id = getSession()
    
    if not flag_ses:
        return redirect("login.html")
    
    list =MyDaoUserInfo().myselect(user_id)
    return render_template('mypage_mod.html',list=list)


@app.route('/user_info_upd.ajax', methods=['POST'])
def user_info_upd_ajax():
    flag_ses,  user_id = getSession()
    
    if not flag_ses:
        return redirect("login.html")
    
    user_id =str(escape(session['user_id']))
    room_seq =request.form["room_seq"]
    user_name =request.form["user_name"]
    user_mobile =request.form["user_mobile"]
    user_gubun =request.form["user_gubun"]
    user_email =request.form["user_email"]
    up_user_id = str(escape(session['user_id']))
    
    
    
    list = MyDaoUserInfo().myselect_banjang(room_seq)
    
    if len(list)<=0:
        cnt = MyDaoUserInfo().myupdate(user_id, user_name, user_mobile, user_gubun, user_email, up_user_id) 
    else :
                
        b_id = list[0]['b_id']
        b_cnt = list[0]['b_cnt']
    
    
        if user_gubun == 'b' and b_cnt >= 1 and user_id == b_id:
            cnt = MyDaoUserInfo().myupdate(user_id, user_name, user_mobile, user_gubun, user_email, up_user_id)
            
            list = MyDaoUserInfo().myselect(user_id)
            session['user_name'] = list[0]['user_name']
            session['user_gubun'] = list[0]['user_gubun']
        elif user_gubun == 's':
            cnt = MyDaoUserInfo().myupdate(user_id, user_name, user_mobile, user_gubun, user_email, up_user_id)
            list = MyDaoUserInfo().myselect(user_id)
            session['user_name'] = list[0]['user_name']
            session['user_gubun'] = list[0]['user_gubun']
        else:
            cnt = 0
            
        print(session['user_name'])
        print(session['user_gubun'])
    
    msg=""
    if cnt==1:
        msg="ok"
    else:
        msg="ng"
        
    return jsonify(msg=msg)


@app.route('/banjang_flag.ajax', methods=['POST'])
def banjang_flag_ajax():
    
    
    
    user_id =request.form["user_id"]
    
    list =MyDaoUserInfo().myselect(user_id)
    
    msg=""
    if list[0]['user_gubun'] == 'b':
        msg="b"
    else:
        msg="s"
    print("msg" ,msg)
    return jsonify(msg=msg)



@app.route("/notice_detail")
def notice_detail_render():
    notice_seq = request.args.get('notice_seq')
    
    flag_ses,  user_id = getSession()
    
    if not flag_ses:
        return redirect("login.html")
    
     
    list = MyDaoNotice().myselect(notice_seq)
    return render_template('notice_detail.html', list=list, enumerate=enumerate)



@app.route("/notice_add")
def notice_add_render():
    flag_ses,  user_id = getSession()
    
    if not flag_ses:
        return redirect("login.html")
    
    list = MyDaoNotice().myselect_seq()
    max_seq = list[0]['max_seq'] + 1
    
    return render_template('notice_add.html', max_seq = max_seq)


@app.route("/notice_addact", methods=['POST'])
def snotice_addact_render():
    flag_ses, user_id = getSession()
    if not flag_ses:
        return redirect("login.html")    
    
    notice_title       = request.form["notice_title"]
    notice_content     = request.form["notice_content"]
        
    file = request.files['file']
    print(file)
    attach_file_temp = secure_filename(file.filename)
    attach_path_temp = str(datetime.today().strftime("%Y%m%d%H%M%S")) + "_" + attach_file_temp 
    
    print(attach_file_temp)
    print(attach_path_temp)
    
    file.save(os.path.join(DIR_UPLOAD, attach_path_temp))
    
    
    attach_path = ""
    attach_file = ""
    if file :
        attach_path = attach_path_temp
        attach_file = attach_file_temp
        print("file o")
    else:
        print("file x")   
    
    print("file",file )
    print("attach_file",attach_file)
    print("attach_path",attach_path)
    
    cnt = MyDaoNotice().myinsert('', notice_title, notice_content, attach_file, attach_path, '', '', user_id, '', user_id)
        
    return render_template('notice_addact.html',cnt=cnt, enumerate=enumerate)


@app.route('/notice_hit_upd.ajax', methods=['POST'])
def notice_hit_upd_ajax():
    notice_seq =request.form["notice_seq"]
    print(notice_seq)
    
    cnt = MyDaoNotice().myupdate_hit(notice_seq)
    
    if cnt==1:
        msg="ok"
    else:
        msg="ng"
        
    return jsonify(msg=msg)


@app.route('/download')
def download():
    attach_path = request.args.get('attach_path')
    attach_file = request.args.get('attach_file')

    file_name = DIR_UPLOAD + "/" + attach_path
    return send_file(file_name,
                     mimetype='image/png',
                     attachment_filename=attach_file,# 다운받아지는 파일 이름. 
                     as_attachment=True)


@app.route("/notice_mod")
def notice_mod_render():
    flag_ses, user_id = getSession()
    if not flag_ses:
        return redirect("login.html") 
    notice_seq = request.args.get('notice_seq')
    print(notice_seq)
    list = MyDaoNotice().myselect(notice_seq)
    print(list)
    
    return render_template('notice_mod.html', list=list)


@app.route('/notice_del_img.ajax', methods=['POST'])
def notice_del_img_ajax():
    
    notice_seq =request.form["notice_seq"]
    
    cnt = MyDaoNotice().mydelete_img(notice_seq)
    print(cnt)
    
    if cnt==1:
        msg="ok"
    else:
        msg="ng"
        
    return jsonify(msg=msg)


@app.route("/notice_modact", methods=['POST'])
def snotice_modact_render():
    flag_ses, user_id = getSession()
    if not flag_ses:
        return redirect("login.html")    
    
    notice_seq         = request.form["notice_seq"]
    notice_title       = request.form["notice_title"]
    notice_content     = request.form["notice_content"]
        
    file = request.files['file']
    attach_file_temp = secure_filename(file.filename)
    attach_path_temp = str(datetime.today().strftime("%Y%m%d%H%M%S")) + "_" + attach_file_temp 
    file.save(os.path.join(DIR_UPLOAD, attach_path_temp))
    
    attach_path = ""
    attach_file = ""
    if file :
        attach_path = attach_path_temp
        attach_file = attach_file_temp
        print("file o")
    else:
        print("file x")   
    
    print("file",file )
    print("attach_file",attach_file)
    print("attach_path",attach_path)
    
    cnt = MyDaoNotice().myupdate(notice_seq, notice_title, notice_content, attach_file, attach_path)
        
    return render_template('notice_modact.html',cnt=cnt, enumerate=enumerate,notice_seq = notice_seq)

@app.route('/notice_del.ajax', methods=['POST'])
def notice_del_ajax():
    
    notice_seq =request.form["notice_seq"]
    
    cnt = MyDaoNotice().mydelete(notice_seq)
    
    if cnt==1:
        msg="ok"
    else:
        msg="ng"
        
    return jsonify(msg=msg)



@app.route("/qna")
def qna_render():
    flag_ses,  user_id = getSession()
    
    if not flag_ses:
        return redirect("login.html")
    
    list =MyDaoQna().myselect_list()
    
    list_len = len(list)
    
    return render_template('qna.html',list=list, list_len=list_len, enumerate=enumerate)
    
    
@app.route("/qna_detail")
def qna_detail_render():
    flag_ses,  user_id = getSession()
    
    if not flag_ses:
        return redirect("login.html")
    
    qna_seq = request.args.get('qna_seq')
    
    list = MyDaoQna().myselect(qna_seq)
    print(list)
    return render_template('qna_detail.html',list=list)



@app.route("/qna_add")
def qna_add_render():
    flag_ses,  user_id = getSession()
    
    if not flag_ses:
        return redirect("login.html")
    
    list = MyDaoQna().myselect_seq()
    max_seq = list[0]['max_seq'] + 1
    
    return render_template('qna_add.html', max_seq = max_seq)
    



@app.route("/qna_addact", methods=['POST'])
def qna_addact_render():
    flag_ses, user_id = getSession()
    if not flag_ses:
        return redirect("login.html")    
    
    qna_title       = request.form["qna_title"]
    qna_content     = request.form["qna_content"]
        
    file = request.files['file']
    print(file)
    attach_file_temp = secure_filename(file.filename)
    attach_path_temp = str(datetime.today().strftime("%Y%m%d%H%M%S")) + "_" + attach_file_temp 
    
    print(attach_file_temp)
    print(attach_path_temp)
    
    file.save(os.path.join(DIR_UPLOAD, attach_path_temp))
    
    
    attach_path = ""
    attach_file = ""
    if file :
        attach_path = attach_path_temp
        attach_file = attach_file_temp
        print("file o")
    else:
        print("file x")   
    
    print("file",file )
    print("attach_file",attach_file)
    print("attach_path",attach_path)
    
    cnt = MyDaoQna().myinsert('', qna_title, qna_content, attach_file, attach_path, user_id, user_id)
        
    return render_template('qna_addact.html',cnt=cnt, enumerate=enumerate)


@app.route('/qna_del.ajax', methods=['POST'])
def qna_del_ajax():
    
    qna_seq =request.form["qna_seq"]
    
    cnt = MyDaoQna().mydelete(qna_seq)
    
    if cnt==1:
        msg="ok"
    else:
        msg="ng"
        
    return jsonify(msg=msg)


@app.route('/qna_anwer_add.ajax', methods=['POST'])
def qna_anwer_add_ajax():
    qna_seq =request.form["qna_seq"]
    qna_answer =request.form["qna_answer"]
    

    cnt = MyDaoQna().myinsert_answer(qna_seq, qna_answer)
    
    if cnt==1:
        msg="ok"
    else:
        msg="ng"
        
    return jsonify(msg=msg)


@app.route('/qna_anwer_del.ajax', methods=['POST'])
def qna_anwer_del_ajax():
    qna_seq =request.form["qna_seq"]
    
    cnt = MyDaoQna().mydelete_answer(qna_seq)
    
    if cnt==1:
        msg="ok"
    else:
        msg="ng"
        
    return jsonify(msg=msg)






@app.route('/store_ins.ajax', methods=['POST'])
def store_ins_ajax():
    flag_ses,  user_id = getSession()
    if not flag_ses:
        return redirect("login.html")
    
    store_name = request.form["store_name"]
    store_tel = request.form["store_tel"]
    store_code = request.form["store_code"]
    print(store_name)
    print(store_tel)
    print(store_code)
    
    cnt = MyDaoStoreInfo().myinsert(store_name, store_tel,user_id,user_id)
    cnt_1 = MyDaoStoreCode().myinsert(store_code, '', user_id)
    print("cnt:",cnt)
    print("cnt_1:",cnt_1)
    
    msg = ""
    if cnt == 1 and cnt_1 ==1:
        msg = "ok"
    else:
        msg = "ng"

    return jsonify(msg = msg)





@app.route("/kakaopay/paymethod.ajax", methods=['POST'])
def paymethod():
    if request.method == 'POST':
        URL = 'https://kapi.kakao.com/v1/payment/ready'
        headers = {
            'Authorization': "KakaoAK " + "a4c40ce9330b1686d78b12cb9fc095c1",
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
        }
        store_seq = request.form["store_seq"]
        store_code = request.form["store_code"]
        store_name = request.form["store_name"]
        total_price = request.form["total_price"]
        
        print(store_code)
        print(store_name)
        print(total_price)
        
        
        params = {
            "cid": "TC0ONETIME", #store_code
            "partner_order_id": "1001",  
            "partner_user_id": "testuser",  
            "item_name": store_name, 
            "quantity": 1, 
            "total_amount": total_price, 
            "tax_free_amount": 0,  
            "vat_amount" : 0,
            "approval_url": "http://127.0.0.1:5002/kakaopay/success",
            "cancel_url": "http://127.0.0.1:5002/kakaopay/cancel",
            "fail_url": "http://127.0.0.1:5002/kakaopay/fail",
        }

        res = requests.post(URL, headers=headers, params=params)
        
        print(res.json())
        app.tib = res.json()['tid']  # 결제 승인시 사용할 tid를 세션에 저장
        app.cid = params['cid']
        app.sseq = store_seq

        return jsonify({'next_url': res.json()['next_redirect_pc_url']})

    return render_template('order.html')




@app.route("/kakaopay/cancel", methods=['POST', 'GET'])
def cancel():
    URL = "https://kapi.kakao.com/v1/payment/order"
    headers = {
        "Authorization": "KakaoAK " + "a4c40ce9330b1686d78b12cb9fc095c1",
        "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
    }
    params = {
        "cid": "TC0ONETIME",  # 가맹점 코드
        "tid": app.tib,  # 결제 고유 코드

    }

    res = requests.post(URL, headers=headers, params=params)
    print(res.text)
    amount = res.json()['cancel_available_amount']['total']

    context = {
        'res': res,
        'cancel_available_amount': amount,
    }
    
    if res.json()['status'] == "QUIT_PAYMENT":
        res = res.json()
        return render_template('order_cancel.html', params=params, res=res, context=context)


@app.route("/kakaopay/fail", methods=['POST', 'GET'])
def fail():

    return render_template('order_fail.html')



@app.route('/kakaopay/pay_flag.ajax', methods=['POST'])
def pay_flag_ajax():
    flag_ses,  user_id = getSession()
      
    if not flag_ses:
        return redirect("login.html")
      
    
    store_seq = request.form["store_seq"]
    print(store_seq)
      
    cnt = MyDaoOrder().mypay_flag(store_seq)
    print(cnt)
    
    msg = ""
    if cnt >= 1:
        msg = "ok"
    else:
        msg = "ng"
  
    return jsonify(msg = msg)



@app.route('/order_pay_flag.ajax', methods=['POST'])
def order_pay_flag_ajax():
    flag_ses,  user_id = getSession()
      
    if not flag_ses:
        return redirect("login.html")
    
    store_seq =request.form["store_seq"]
    print(store_seq)
    
    list1 = MyDaoUserInfo().myselect(user_id);
    room_seq = list1[0]['room_seq']
    
    list = MyDaoOrder().myselect_pay_flag(room_seq,store_seq)
                                                                                                                                                                                                                                             
    txt_tel,txt_msg = MyDaoOrder().myselect_sms(store_seq,room_seq)
    session['txt_tel'] = txt_tel
    session['txt_msg'] = txt_msg
    

    msg=""
    if list[0]['pay_flag'] == 'y':
        msg = "ng"
    else:
        msg = "ok"

    return jsonify(msg=msg)

@app.route("/msg_send.ajax", methods=['POST']) 
def msg_send_ajax():        
    api_key = "NCSVDVNCRIIHWTR1"
    api_secret = "WVU0LBZ7JQUZXQECBRQ7OCHPZHVSZWPJ"
    
    ## 4 params(to, from, type, text) are mandatory. must be filled
    params = dict()
    params['type'] = 'lms' # Message type ( sms, lms, mms, ata )
    params['to'] = session['txt_tel'] # Recipients Number '01000000000,01000000001'
    params['from'] = '01094866829' # Sender number
    params['text'] = session['txt_msg'] # Message
  
    cool = Message(api_key, api_secret)
    try:
        response = cool.send(params)
        print("Success Count : %s" % response['success_count'])
        print("Error Count : %s" % response['error_count'])
        print("Group ID : %s" % response['group_id'])
  
        if "error_list" in response:
            print("Error List : %s" % response['error_list'])
  
    except CoolsmsException as e:
        print("Error Code : %s" % e.code)
        print("Error Message : %s" % e.msg)
  
#     sys.exit()
    
    return jsonify(msg = "ok")

  
  
  
  

@app.route("/kakaopay/success", methods=['POST', 'GET'])
def sucess():
    
    flag_ses,  user_id = getSession()
      
    if not flag_ses:
        return redirect("login.html")
    
    txt_msg = session['txt_msg']
    txt_tel = session['txt_tel']
    
    
    URL = 'https://kapi.kakao.com/v1/payment/approve'
    headers = {
        "Authorization": "KakaoAK " + "a4c40ce9330b1686d78b12cb9fc095c1",
        "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
    }
    params = {
        "cid": app.cid,
        "tid": app.tib,  # 결제 요청시 세션에 저장한 tid
        "partner_order_id": "1001",  # 주문번호
        "partner_user_id": "testuser",  # 유저 아이디
        "pg_token": request.args.get("pg_token"),  # 쿼리 스트링으로 받은 pg토큰
    }

    res = requests.post(URL, headers=headers, params=params)
    print("res.text",res.text)
    print("res.json()",res.json())
    
    amount = res.json()['amount']['total']
    res = res.json()
    context = {
        'res': res,
        'amount': amount,
    }
    
    
    list= MyDaoUserInfo().myselect(user_id)
    room_seq = list[0]['room_seq']
    cnt = MyDaoOrder().mypay_flag(room_seq,app.sseq)
    
    transaction_yn = ""
    url_success_fail = ""
    if cnt > 0:
        transaction_yn = "y"
        url_success_fail = "order_success.html"
        
    else:
        transaction_yn = "n"
        url_success_fail = "order_fail.html"

    return render_template('order_success.html', context=context, res=res,transaction_yn=transaction_yn)

@app.route('/order_person.ajax', methods=['POST'])
def order_person_ajax():
    flag_ses,  user_id = getSession()
      
    if not flag_ses:
        return redirect("login.html")
    
    menu_seq =request.form["menu_seq"]
    room_seq =request.form["room_seq"]
    now_date =request.form["now_date"]


    print("오더퍼슨")
    print(menu_seq)    
    print(room_seq)    
    print(now_date)
    
        
    list = MyDaoOrder().order_person(menu_seq, room_seq, now_date)
    print(list)
    
    msg=""
    if len(list)>=1:
        msg = 'ok'
    else:
        msg="ng"
    
    return jsonify(msg=msg, op_list = list)


@app.route('/menu_recomm.ajax', methods=['POST'])
def menu_recomm_ajax():
    flag_ses,  user_id = getSession()
      
    if not flag_ses:
        return redirect("login.html")
    
    print("ddsfsfsfs")
    
    menu_name = ""
    list = MyDaoOrder().myselect_recomm_menu(user_id)
    if len(list) > 0:
        menu_seq = list[0]['menu_seq']
        
        list_2 = MyDaoMenu().myselect_menu(menu_seq)
        menu_name = list_2[0]['menu_name']
          
    msg=""
    if len(list)>=1:
        msg = 'ok'
    else:
        msg="ng"
    
    return jsonify(msg=msg, menu_name = menu_name)


















































#민선

@app.route("/today_order")
def today_order_render():
    flag_ses,  user_id = getSession()
    
    if not flag_ses:
        return redirect("login.html")
    
    list = MyDaoOrder().myselect_graph();
    slist = MyDaoOrder().mystore_name_select();
    
    d = list[0][0]['indate']
    date = d[0:4]+'년 '+d[4:6]+'월 '+d[6:8]+'일'
    return render_template('today_order.html',list=list, enumerate=enumerate, slist=slist, date = date)


@app.route("/admin_order_list")
def admin_order_list_render():
    flag_ses,  user_id = getSession()
    
    if not flag_ses:
        return redirect("login.html")
    
    search = request.args.get('search', '')
    list = MyDaoOrder().myadmin_select(search);
    return render_template('admin_order_list.html',list=list, search=search)




@app.route("/admin_order_list_date")
def admin_order_list_date_render():
    flag_ses,  user_id = getSession()
    
    if not flag_ses:
        return redirect("login.html")
    
    date = request.args.get('date', '')
    list = MyDaoOrder().myadmin_select_date(date);
    return render_template('admin_order_list.html',list=list, date=date)


@app.route("/admin_order_list_name")
def admin_order_list_name_render():
    flag_ses,  user_id = getSession()
    
    if not flag_ses:
        return redirect("login.html")
    
    name = request.args.get('name', '')
    list = MyDaoOrder().myadmin_select_name(name);
    return render_template('admin_order_list.html',list=list, name=name)



@app.route("/today_store_detail")
def today_store_detail_render():
    flag_ses,  user_id = getSession()
    
    if not flag_ses:
        return redirect("login.html")
    
    store_seq = request.args.get('store_seq')
    list = MyDaoOrder().select_store_detail(store_seq)
    
    return render_template('today_store_detail.html', store_seq=store_seq, list=list, enumerate=enumerate)



##################오더########################오더~~~~###############################################
@app.route("/order")
def order_render():
    flag_ses,  user_id = getSession()
    if not flag_ses:
        return redirect("login.html")
    slist = MyDaoOrder().mystore_name_select()
    gra_list = MyDaoUserInfo().myselect_list(user_id)
    print(slist)
    print("gra_list",gra_list)


    return render_template('order.html', enumerate=enumerate, slist=slist, gra_list=gra_list)
    

@app.route("/order_menu_select.ajax", methods=['POST'])
def order_menu_select_render():
    flag_ses,  user_id = getSession()
    if not flag_ses:
        return redirect("login.html")
    
    store_seq =request.form["store_seq"]
    list = MyDaoOrder().order_menu_select(store_seq)
    
    return jsonify(list=list)



#반장만 보이는 div
@app.route('/banjang_order.ajax', methods=['POST'])
def banjang_order_ajax():
    
    user_id =request.form["user_id"]
    
    ulist =MyDaoUserInfo().myselect(user_id)
    
    msg=""
    if ulist[0]['user_gubun'] == 'b':
        msg="b"
        
        
    else:
        msg="s"
    
    blist = MyDaoOrder().banjang_select(user_id)
    return jsonify(blist=blist, msg=msg)



####주문하기 버튼!!!!
@app.route("/order_add.ajax", methods=['POST'])
def order_add_render():
    flag_ses,  user_id = getSession()
     
    if not flag_ses:
        return redirect("login.html")
     
    store_seq =request.form["store_seq"]
    menu_seq =request.form["menu_seq"]
    order_cnt =request.form["order_cnt"]
    
    user_info = MyDaoUserInfo().myselect(user_id);
    room_seq = user_info[0]['room_seq'];
    
    list = MyDaoOrder().myselect_pay_flag(room_seq, store_seq)
    
    if len(list) <= 0:
        cnt = MyDaoOrder().orderinsert(menu_seq, order_cnt, user_id)
    
    
        if cnt == 1:
            msg = "ok"
        else:
                msg = "ng"

        return jsonify(msg = msg)
        
    msg = ""
    if list[0]['pay_flag'] == 'y' :
        msg = "pay_com"
        return jsonify(msg = msg)
    else :
        cnt = MyDaoOrder().orderinsert(menu_seq, order_cnt, user_id)
    
    
        if cnt == 1:
            msg = "ok"
        else:
                msg = "ng"

        return jsonify(msg = msg)

#호실관리#####################################################################################
@app.route("/room_list")
def room_list_render():
    flag_ses,  user_id = getSession()
    
    if not flag_ses:
        return redirect("login.html")
    
    list = MyDaoRoom().myselect()
    #print(list)
    return render_template('room_list.html', list=list, enumerate=enumerate)




@app.route("/room_del")
def room_select_del_render():
    flag_ses,  user_id = getSession()
     
    if not flag_ses:
        return redirect("login.html")
     
    list = MyDaoRoom().mydelete_room()
     
    return render_template('room_del.html', list=list, enumerate=enumerate)


@app.route("/room_upd.ajax", methods=['POST'])
def room_upd_render():
    flag_ses,  user_id = getSession()
    
    if not flag_ses:
        return redirect("login.html")
    
    room_seq =request.form["room_seq"]
    del_flag =request.form["del_flag"]
    
    #print(del_flag)
    if del_flag == 'y':
        cnt = MyDaoRoom().myupdate_yton(room_seq)
        print("위에꺼")
    elif del_flag == 'n':
        cnt = MyDaoRoom().myupdate_ntoy(room_seq)
        print("밑에꺼")

    msg = ""
    if cnt == 1:
        msg = "ok"
    else:
        msg = "ng"

    return jsonify(msg = msg)    

###호실추가
@app.route("/room_add.ajax", methods=['POST'])
def room_add_render():
    flag_ses,  user_id = getSession()
    
    if not flag_ses:
        return redirect("login.html")
    
    room_seq =request.form["room_seq"]
    
    list = MyDaoRoom().mycheck(room_seq)
    #print(list[0]['cnt'])
    
    msg = ""
    if list[0]['cnt'] == 1:
        msg = "ng"
    else :
        cnt = MyDaoRoom().myinsert(room_seq)
        msg = "ok"
        
    return jsonify(msg = msg)    


@app.route("/room_del.ajax", methods=['POST'])
def room_del_render():
    flag_ses,  user_id = getSession()
    
    if not flag_ses:
        return redirect("login.html")
    
    room_seq =request.form["room_seq"]
    print(room_seq)
    cnt = MyDaoRoom().mydelete(room_seq)
    print(cnt)
    msg = ""
    if cnt == 1:
        msg = "ok"
    else:
        msg = "ng"
        
    return jsonify(msg = msg) 

















































###############################################################

###############################################################
# 민정
@app.route("/myorder_list")
def myorder_list_render():
    flag_ses, user_id = getSession()
    if not flag_ses:
        return redirect("login.html")
    
    list = MyDaoOrder().myselect_list(user_id)
    
    return render_template('myorder_list.html',list=list,enumerate=enumerate)



@app.route("/user_list")
def user_list_render():
    graduation_flag = request.args.get('graduation_flag')
    flag_ses, user_id = getSession()
    if not flag_ses:
        return redirect("login.html")
    
    list = MyDaoUserInfo().myselect_list_b()
    print(list)
    return render_template('user_list.html',list=list,enumerate=enumerate, graduation_flag=graduation_flag)




@app.route("/user_list_detail")
def user_list_detail_render():
    room_seq = request.args.get('room_seq')
    user_name = request.args.get('user_name')
    graduation_flag = request.args.get('graduation_flag')
    flag_ses, user_id = getSession()
    if not flag_ses:
        return redirect("login.html")
     
    list = MyDaoUserInfo().myselect_list_detail(room_seq)
    return render_template('user_list_detail.html', list=list, enumerate=enumerate, user_name=user_name, graduation_flag=graduation_flag,room_seq=room_seq)


@app.route('/user_flag_upd.ajax', methods=['POST'])
def user_flag_upd_ajax():
    room_seq = request.form["room_seq"]

    print("room_seq", room_seq)
    
    cnt = MyDaoUserInfo().myupdate_gflag(room_seq)
    print(cnt)
    msg = ""
    if cnt >= 1:
        msg = "ok"
    else:
        msg = "ng"

    return jsonify(msg = msg)


@app.route("/store_list")
def store_list_render():
    flag_ses, user_id = getSession()
    if not flag_ses:
        return redirect("login.html")
    list = MyDaoStoreInfo().myselect()
    print(list)
    return render_template('store_list.html',list=list,enumerate=enumerate)

@app.route('/store_flag_upd.ajax', methods=['POST'])
def store_flag_upd_ajax():
    store_seq = request.form["store_seq"]
    print("store_seq", store_seq)
    
    cnt = MyDaoStoreInfo().myupdate(store_seq)
    print(cnt)
    msg = ""
    if cnt >= 1:
        msg = "ok"
    else:
        msg = "ng"

    return jsonify(msg = msg)

@app.route("/store_add")
def store_add_render():
    flag_ses, user_id = getSession()
    if not flag_ses:
        return redirect("login.html")
    
    return render_template('store_add.html', enumerate=enumerate)


@app.route("/store_detail")
def store_detail_render():
    flag_ses, user_id = getSession()
    if not flag_ses:
        return redirect("login.html")
    
    store_name = request.args.get('store_name')
    store_seq = request.args.get('store_seq')
    store_tel = request.args.get('store_tel')
    print("store_seq", store_seq)
    print("store_name", store_name)
    
    list_1 = MyDaoStoreInfo().myselect_d(store_seq)
    list = MyDaoMenu().myselect(store_seq)
    print(list_1)
    print(list)
    return render_template('store_detail.html',list_1=list_1, list=list,enumerate=enumerate,store_name=store_name,store_tel=store_tel)
    

@app.route('/store_tel_upd.ajax', methods=['POST'])
def store_tel_upd_ajax():
    flag_ses, user_id = getSession()
    if not flag_ses:
        return redirect("login.html")
    
    store_mobile = request.form["store_mobile"]
    store_seq = request.form["store_seq"]
#     store_tel = request.form["store_tel"]
#     print("store_mobile", store_mobile)
#     print("store_seq", store_seq)
    
    cnt = MyDaoStoreInfo().myupdate_tel(store_seq,'',store_mobile,'','',user_id,'',user_id)
    print(cnt)
    msg = ""
    if cnt >= 1:
        msg = "ok"
    else:
        msg = "ng"

    return jsonify(msg = msg)


@app.route("/store_detail_add")
def store_detail_add_render():
    flag_ses, user_id = getSession()
    if not flag_ses:
        return redirect("login.html")
       
    store_seq = request.args.get('store_seq')
#     print("store_seq", store_seq)
      
    list = MyDaoStoreInfo().myselect_d(store_seq)
    list_1 = MyDaoMenu().myselect(store_seq)
    print(list)
    return render_template('store_detail_add.html', list=list, list_1=list_1, enumerate=enumerate)



@app.route("/menu_addact", methods=['POST'])
def menu_addact_render():
    flag_ses, user_id = getSession()
    if not flag_ses:
        return redirect("login.html")    
    
      
    menu_cnt  = request.form["menu_cnt"]
    store_seq  = request.form["store_seq"]
    print(menu_cnt)
    print(store_seq)
    
    for i in range(int(menu_cnt)):
        temp_m = "n"+ str(i)
        temp_p = "p"+ str(i)
        
        
        menu_name  = request.form[temp_m]
        print("mn : ",menu_name)
        menu_price  = request.form[temp_p]
        print("mp : ",menu_price)
        cnt = MyDaoMenu().myinsert(store_seq, menu_name, menu_price, '', '', user_id, '', user_id)
        print(cnt)
#         print("cnt : ",cnt)
#         if cnt == 0:
#             cnt = cnt*-1;
        
#         menu_price = request.form["p'+i+'"]
#      
#         cnt = MyDaoMenu().myinsert('', '', menu_name, menu_price, '', '', user_id, '', user_id)
#      
    return render_template('menu_addact.html',cnt=cnt, enumerate=enumerate)




@app.route("/store_detail_del")
def store_detail_del_render():
    flag_ses, user_id = getSession()
    if not flag_ses:
        return redirect("login.html")
    
    store_seq = request.args.get('store_seq')
    print("store_seq", store_seq)
    
    list = MyDaoMenu().myselect(store_seq)
    print(list)
    return render_template('store_detail_del.html', list=list,enumerate=enumerate)



@app.route('/store_menu_mod_del.ajax', methods=['POST'])
def store_menu_mod_del_ajax():
    flag_ses, user_id = getSession()
    if not flag_ses:
        return redirect("login.html")
    
    menu_seq = request.form["menu_seq"]
    store_seq = request.form["store_seq"]
    menu_name = request.form["menu_name"]
    menu_price = request.form["menu_price"]
    del_flag = request.form["del_flag"]
    print("menu_seq", menu_seq)
    print("store_seq", store_seq)
    print("menu_name", menu_name)
    print("menu_price", menu_price)
    print("del_flag", del_flag)
    
    
    cnt = MyDaoMenu().myupdate_menu(menu_seq, '', menu_name, menu_price, del_flag, '', '', '', user_id)
    print(cnt)
    msg = ""
    if cnt >= 1:
        msg = "ok"
    else:
        msg = "ng"

    return jsonify(msg = msg)










































































































if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5002")