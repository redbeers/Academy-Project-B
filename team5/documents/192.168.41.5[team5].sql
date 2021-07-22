
/* Drop Tables */

DROP TABLE bnotice CASCADE CONSTRAINTS;
DROP TABLE admins CASCADE CONSTRAINTS;
DROP TABLE bfree CASCADE CONSTRAINTS;
DROP TABLE book CASCADE CONSTRAINTS;
DROP TABLE bsug CASCADE CONSTRAINTS;
DROP TABLE nticket CASCADE CONSTRAINTS;
DROP TABLE ticket CASCADE CONSTRAINTS;
DROP TABLE tow CASCADE CONSTRAINTS;
DROP TABLE members CASCADE CONSTRAINTS;
DROP TABLE parkinfo CASCADE CONSTRAINTS;
DROP TABLE prod CASCADE CONSTRAINTS;




/* Create Tables */

CREATE TABLE admins
(
	-- �����ھ��̵�
	admin_id varchar2(30) NOT NULL,
	-- �����ں�й�ȣ
	admin_pw varchar2(1000),
	-- �����ڸ�
	admin_name varchar2(100),
	PRIMARY KEY (admin_id)
);


CREATE TABLE bfree
(
	-- ����
	bfree_seq number NOT NULL,
	-- ����
	bfree_title varchar2(1000),
	-- ����
	bfree_content varchar2(4000),
	-- ÷�����ϸ�
	bfree_filename varchar2(1000),
	-- ÷�����ϰ��
	bfree_filepath varchar2(1000),
	-- ��ȸ��
	bfree_hit number,
	-- ��۹�ȣ
	bfree_rpseq number,
	-- �ۼ�����
	in_date varchar2(30),
	-- �ۼ���
	in_user_id varchar2(60),
	-- ��������
	up_date varchar2(30),
	-- ������
	up_user_id varchar2(30),
	-- ������ȣ
	mem_carnum varchar2(60) NOT NULL,
	PRIMARY KEY (bfree_seq)
);


CREATE TABLE bnotice
(
	-- �Ϸù�ȣ
	bnotice_seq number NOT NULL,
	-- ����
	bnotice_title varchar2(1000) NOT NULL,
	-- ����
	bnotice_content varchar2(4000),
	-- ÷�����ϸ�
	bnotice_filename varchar2(1000),
	-- ÷�����ϰ��
	bnotice_filepath varchar2(1000),
	-- ��ȸ��
	bnotice_hit number,
	in_date varchar2(30),
	-- �ۼ���
	in_user_id varchar2(100),
	-- ��������
	up_date varchar2(30),
	-- �����ھ��̵�
	admin_id varchar2(30) NOT NULL,
	PRIMARY KEY (bnotice_seq)
);


CREATE TABLE book
(
	-- �����ȣ
	book_seq varchar2(30) NOT NULL,
	-- ���ų�¥
	book_buydate varchar2(30),
	-- ���೯¥
	book_sdate varchar2(30),
	-- ��������
	book_edate varchar2(30),
	-- ��ҿ���
	book_cel_yn varchar2(3),
	-- ������ȣ
	mem_carnum varchar2(60) NOT NULL,
	-- �ڸ���ȣ
	parkinfo_seq number NOT NULL,
	-- ��ǰ�ڵ�
	prod_code varchar2(30) NOT NULL,
	PRIMARY KEY (book_seq)
);


CREATE TABLE bsug
(
	-- ����
	bnotice_title varchar2(1000) NOT NULL,
	-- ����
	bsug_title varchar2(1000),
	-- ����
	bsug_content varchar2(4000),
	-- ÷�����ϸ�
	bsug_filename varchar2(1000),
	-- ÷�����ϰ��
	bsug_filepath varchar2(1000),
	-- ��ȸ��
	bsug_hit number,
	-- ��۹�ȣ
	bsug_rpseq number,
	-- �ۼ�����
	in_date varchar2(30),
	-- �ۼ���
	in_user_id varchar2(100),
	-- ��������
	up_date varchar2(30),
	-- ������ȣ
	mem_carnum varchar2(60) NOT NULL,
	PRIMARY KEY (bnotice_title)
);


CREATE TABLE members
(
	-- ������ȣ
	mem_carnum varchar2(60) NOT NULL,
	-- �̸�
	mem_name varchar2(30),
	-- �̸���
	mem_email varchar2(100),
	-- ��ȭ��ȣ
	mem_tel varchar2(30),
	-- ��й�ȣ
	mem_pw varchar2(1000),
	-- ����ǿ���
	mem_ticket_yn varchar2(1),
	-- Ż�𿩺�
	mem_exit_yn varchar2(1),
	mem_tow_yn varchar2(1),
	-- ������Ʈ����
	mem_black_yn varchar2(1),
	-- ȸ��������
	sign_date varchar2(30),
	-- ȸ��Ż����
	signout_date varchar2(30),
	PRIMARY KEY (mem_carnum)
);


CREATE TABLE nticket
(
	-- ����
	nticket_seq number NOT NULL,
	-- �����ð�
	nticket_indate varchar2(30),
	-- �����ð�
	nticket_outdate varchar2(30),
	-- ������ȣ
	mem_carnum varchar2(60) NOT NULL,
	-- �ڸ���ȣ
	parkinfo_seq number NOT NULL,
	-- ��ǰ�ڵ�
	prod_code varchar2(30) NOT NULL,
	PRIMARY KEY (nticket_seq)
);


CREATE TABLE parkinfo
(
	-- �ڸ���ȣ
	parkinfo_seq number NOT NULL,
	-- ���������
	parkinfo_ticket_yn varchar2(1),
	-- ��������
	parkinfo_book_yn varchar2(1),
	-- ����߿���
	parkinfo_use_yn varchar2(1),
	PRIMARY KEY (parkinfo_seq)
);


CREATE TABLE prod
(
	-- ��ǰ�ڵ�
	prod_code varchar2(30) NOT NULL,
	-- ���������, �Ϲݱ�����, ȸ��������, ��ȸ����������
	-- ������ ��Ÿ���� �ڵ�
	prod_dcode varchar2(30),
	-- ��ǰ��
	prod_name varchar2(300),
	-- ��ǰ����
	prod_price number,
	PRIMARY KEY (prod_code)
);


CREATE TABLE ticket
(
	-- ����
	ticket_seq number NOT NULL,
	-- �̿������
	ticket_sdate varchar2(30),
	-- �̿�������
	ticket_edate varchar2(30),
	-- ������ȣ
	mem_carnum varchar2(60) NOT NULL,
	-- ��ǰ�ڵ�
	prod_code varchar2(30) NOT NULL,
	PRIMARY KEY (ticket_seq)
);


CREATE TABLE tow
(
	-- ����
	tow_seq number NOT NULL,
	-- ���γ�¥
	tow_date varchar2(30),
	-- ���λ���
	tow_reason varchar2(4000),
	-- ������ȣ
	mem_carnum varchar2(60) NOT NULL,
	PRIMARY KEY (tow_seq)
);



/* Create Foreign Keys */

ALTER TABLE bnotice
	ADD FOREIGN KEY (admin_id)
	REFERENCES admins (admin_id)
;


ALTER TABLE bfree
	ADD FOREIGN KEY (mem_carnum)
	REFERENCES members (mem_carnum)
;


ALTER TABLE book
	ADD FOREIGN KEY (mem_carnum)
	REFERENCES members (mem_carnum)
;


ALTER TABLE bsug
	ADD FOREIGN KEY (mem_carnum)
	REFERENCES members (mem_carnum)
;


ALTER TABLE nticket
	ADD FOREIGN KEY (mem_carnum)
	REFERENCES members (mem_carnum)
;


ALTER TABLE ticket
	ADD FOREIGN KEY (mem_carnum)
	REFERENCES members (mem_carnum)
;


ALTER TABLE tow
	ADD FOREIGN KEY (mem_carnum)
	REFERENCES members (mem_carnum)
;


ALTER TABLE book
	ADD FOREIGN KEY (parkinfo_seq)
	REFERENCES parkinfo (parkinfo_seq)
;


ALTER TABLE nticket
	ADD FOREIGN KEY (parkinfo_seq)
	REFERENCES parkinfo (parkinfo_seq)
;


ALTER TABLE book
	ADD FOREIGN KEY (prod_code)
	REFERENCES prod (prod_code)
;


ALTER TABLE nticket
	ADD FOREIGN KEY (prod_code)
	REFERENCES prod (prod_code)
;


ALTER TABLE ticket
	ADD FOREIGN KEY (prod_code)
	REFERENCES prod (prod_code)
;



/* Comments */

COMMENT ON COLUMN admins.admin_id IS '�����ھ��̵�';
COMMENT ON COLUMN admins.admin_pw IS '�����ں�й�ȣ';
COMMENT ON COLUMN admins.admin_name IS '�����ڸ�';
COMMENT ON COLUMN bfree.bfree_seq IS '����';
COMMENT ON COLUMN bfree.bfree_title IS '����';
COMMENT ON COLUMN bfree.bfree_content IS '����';
COMMENT ON COLUMN bfree.bfree_filename IS '÷�����ϸ�';
COMMENT ON COLUMN bfree.bfree_filepath IS '÷�����ϰ��';
COMMENT ON COLUMN bfree.bfree_hit IS '��ȸ��';
COMMENT ON COLUMN bfree.bfree_rpseq IS '��۹�ȣ';
COMMENT ON COLUMN bfree.in_date IS '�ۼ�����';
COMMENT ON COLUMN bfree.in_user_id IS '�ۼ���';
COMMENT ON COLUMN bfree.up_date IS '��������';
COMMENT ON COLUMN bfree.up_user_id IS '������';
COMMENT ON COLUMN bfree.mem_carnum IS '������ȣ';
COMMENT ON COLUMN bnotice.bnotice_seq IS '�Ϸù�ȣ';
COMMENT ON COLUMN bnotice.bnotice_title IS '����';
COMMENT ON COLUMN bnotice.bnotice_content IS '����';
COMMENT ON COLUMN bnotice.bnotice_filename IS '÷�����ϸ�';
COMMENT ON COLUMN bnotice.bnotice_filepath IS '÷�����ϰ��';
COMMENT ON COLUMN bnotice.bnotice_hit IS '��ȸ��';
COMMENT ON COLUMN bnotice.in_user_id IS '�ۼ���';
COMMENT ON COLUMN bnotice.up_date IS '��������';
COMMENT ON COLUMN bnotice.admin_id IS '�����ھ��̵�';
COMMENT ON COLUMN book.book_seq IS '�����ȣ';
COMMENT ON COLUMN book.book_buydate IS '���ų�¥';
COMMENT ON COLUMN book.book_sdate IS '���೯¥';
COMMENT ON COLUMN book.book_edate IS '��������';
COMMENT ON COLUMN book.book_cel_yn IS '��ҿ���';
COMMENT ON COLUMN book.mem_carnum IS '������ȣ';
COMMENT ON COLUMN book.parkinfo_seq IS '�ڸ���ȣ';
COMMENT ON COLUMN book.prod_code IS '��ǰ�ڵ�';
COMMENT ON COLUMN bsug.bnotice_title IS '����';
COMMENT ON COLUMN bsug.bsug_title IS '����';
COMMENT ON COLUMN bsug.bsug_content IS '����';
COMMENT ON COLUMN bsug.bsug_filename IS '÷�����ϸ�';
COMMENT ON COLUMN bsug.bsug_filepath IS '÷�����ϰ��';
COMMENT ON COLUMN bsug.bsug_hit IS '��ȸ��';
COMMENT ON COLUMN bsug.bsug_rpseq IS '��۹�ȣ';
COMMENT ON COLUMN bsug.in_date IS '�ۼ�����';
COMMENT ON COLUMN bsug.in_user_id IS '�ۼ���';
COMMENT ON COLUMN bsug.up_date IS '��������';
COMMENT ON COLUMN bsug.mem_carnum IS '������ȣ';
COMMENT ON COLUMN members.mem_carnum IS '������ȣ';
COMMENT ON COLUMN members.mem_name IS '�̸�';
COMMENT ON COLUMN members.mem_email IS '�̸���';
COMMENT ON COLUMN members.mem_tel IS '��ȭ��ȣ';
COMMENT ON COLUMN members.mem_pw IS '��й�ȣ';
COMMENT ON COLUMN members.mem_ticket_yn IS '����ǿ���';
COMMENT ON COLUMN members.mem_exit_yn IS 'Ż�𿩺�';
COMMENT ON COLUMN members.mem_black_yn IS '������Ʈ����';
COMMENT ON COLUMN members.sign_date IS 'ȸ��������';
COMMENT ON COLUMN members.signout_date IS 'ȸ��Ż����';
COMMENT ON COLUMN nticket.nticket_seq IS '����';
COMMENT ON COLUMN nticket.nticket_indate IS '�����ð�';
COMMENT ON COLUMN nticket.nticket_outdate IS '�����ð�';
COMMENT ON COLUMN nticket.mem_carnum IS '������ȣ';
COMMENT ON COLUMN nticket.parkinfo_seq IS '�ڸ���ȣ';
COMMENT ON COLUMN nticket.prod_code IS '��ǰ�ڵ�';
COMMENT ON COLUMN parkinfo.parkinfo_seq IS '�ڸ���ȣ';
COMMENT ON COLUMN parkinfo.parkinfo_ticket_yn IS '���������';
COMMENT ON COLUMN parkinfo.parkinfo_book_yn IS '��������';
COMMENT ON COLUMN parkinfo.parkinfo_use_yn IS '����߿���';
COMMENT ON COLUMN prod.prod_code IS '��ǰ�ڵ�';
COMMENT ON COLUMN prod.prod_dcode IS '���������, �Ϲݱ�����, ȸ��������, ��ȸ���������� ������ ��Ÿ���� �ڵ�';
COMMENT ON COLUMN prod.prod_name IS '��ǰ��';
COMMENT ON COLUMN prod.prod_price IS '��ǰ����';
COMMENT ON COLUMN ticket.ticket_seq IS '����';
COMMENT ON COLUMN ticket.ticket_sdate IS '�̿������';
COMMENT ON COLUMN ticket.ticket_edate IS '�̿�������';
COMMENT ON COLUMN ticket.mem_carnum IS '������ȣ';
COMMENT ON COLUMN ticket.prod_code IS '��ǰ�ڵ�';
COMMENT ON COLUMN tow.tow_seq IS '����';
COMMENT ON COLUMN tow.tow_date IS '���γ�¥';
COMMENT ON COLUMN tow.tow_reason IS '���λ���';
COMMENT ON COLUMN tow.mem_carnum IS '������ȣ';

CREATE OR REPLACE VIEW VW_SALES
AS
SELECT MEM_CARNUM, PROD_CODE, (SELECT PROD_PRICE FROM PROD WHERE PROD_CODE = PROD_CODE) PROD_PRICE FROM BOOK
UNION ALL
SELECT MEM_CARNUM, PROD_CODE, (SELECT PROD_PRICE FROM PROD WHERE PROD_CODE = PROD_CODE) PROD_PRICE FROM NTICKET
UNION ALL
SELECT MEM_CARNUM, PROD_CODE, (SELECT PROD_PRICE FROM PROD WHERE PROD_CODE = PROD_CODE) PROD_PRICE FROM TICKET;

SELECT *
FROM   VW_SALES;