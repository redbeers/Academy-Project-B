
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
	-- 관리자아이디
	admin_id varchar2(30) NOT NULL,
	-- 관리자비밀번호
	admin_pw varchar2(1000),
	-- 관리자명
	admin_name varchar2(100),
	PRIMARY KEY (admin_id)
);


CREATE TABLE bfree
(
	-- 순번
	bfree_seq number NOT NULL,
	-- 제목
	bfree_title varchar2(1000),
	-- 내용
	bfree_content varchar2(4000),
	-- 첨부파일명
	bfree_filename varchar2(1000),
	-- 첨부파일경로
	bfree_filepath varchar2(1000),
	-- 조회수
	bfree_hit number,
	-- 댓글번호
	bfree_rpseq number,
	-- 작성일자
	in_date varchar2(30),
	-- 작성자
	in_user_id varchar2(60),
	-- 수정일자
	up_date varchar2(30),
	-- 수정자
	up_user_id varchar2(30),
	-- 차량번호
	mem_carnum varchar2(60) NOT NULL,
	PRIMARY KEY (bfree_seq)
);


CREATE TABLE bnotice
(
	-- 일련번호
	bnotice_seq number NOT NULL,
	-- 제목
	bnotice_title varchar2(1000) NOT NULL,
	-- 내용
	bnotice_content varchar2(4000),
	-- 첨부파일명
	bnotice_filename varchar2(1000),
	-- 첨부파일경로
	bnotice_filepath varchar2(1000),
	-- 조회수
	bnotice_hit number,
	in_date varchar2(30),
	-- 작성자
	in_user_id varchar2(100),
	-- 수정일자
	up_date varchar2(30),
	-- 관리자아이디
	admin_id varchar2(30) NOT NULL,
	PRIMARY KEY (bnotice_seq)
);


CREATE TABLE book
(
	-- 예약번호
	book_seq varchar2(30) NOT NULL,
	-- 구매날짜
	book_buydate varchar2(30),
	-- 예약날짜
	book_sdate varchar2(30),
	-- 종료일자
	book_edate varchar2(30),
	-- 취소여부
	book_cel_yn varchar2(3),
	-- 차량번호
	mem_carnum varchar2(60) NOT NULL,
	-- 자리번호
	parkinfo_seq number NOT NULL,
	-- 상품코드
	prod_code varchar2(30) NOT NULL,
	PRIMARY KEY (book_seq)
);


CREATE TABLE bsug
(
	-- 제목
	bnotice_title varchar2(1000) NOT NULL,
	-- 제목
	bsug_title varchar2(1000),
	-- 내용
	bsug_content varchar2(4000),
	-- 첨부파일명
	bsug_filename varchar2(1000),
	-- 첨부파일경로
	bsug_filepath varchar2(1000),
	-- 조회수
	bsug_hit number,
	-- 댓글번호
	bsug_rpseq number,
	-- 작성일자
	in_date varchar2(30),
	-- 작성자
	in_user_id varchar2(100),
	-- 수정일자
	up_date varchar2(30),
	-- 차량번호
	mem_carnum varchar2(60) NOT NULL,
	PRIMARY KEY (bnotice_title)
);


CREATE TABLE members
(
	-- 차량번호
	mem_carnum varchar2(60) NOT NULL,
	-- 이름
	mem_name varchar2(30),
	-- 이메일
	mem_email varchar2(100),
	-- 전화번호
	mem_tel varchar2(30),
	-- 비밀번호
	mem_pw varchar2(1000),
	-- 정기권여부
	mem_ticket_yn varchar2(1),
	-- 탈퇴여부
	mem_exit_yn varchar2(1),
	mem_tow_yn varchar2(1),
	-- 블랙리스트여부
	mem_black_yn varchar2(1),
	-- 회원가입일
	sign_date varchar2(30),
	-- 회원탈퇴일
	signout_date varchar2(30),
	PRIMARY KEY (mem_carnum)
);


CREATE TABLE nticket
(
	-- 순번
	nticket_seq number NOT NULL,
	-- 입차시간
	nticket_indate varchar2(30),
	-- 출차시간
	nticket_outdate varchar2(30),
	-- 차량번호
	mem_carnum varchar2(60) NOT NULL,
	-- 자리번호
	parkinfo_seq number NOT NULL,
	-- 상품코드
	prod_code varchar2(30) NOT NULL,
	PRIMARY KEY (nticket_seq)
);


CREATE TABLE parkinfo
(
	-- 자리번호
	parkinfo_seq number NOT NULL,
	-- 정기권유무
	parkinfo_ticket_yn varchar2(1),
	-- 예약유무
	parkinfo_book_yn varchar2(1),
	-- 사용중여부
	parkinfo_use_yn varchar2(1),
	PRIMARY KEY (parkinfo_seq)
);


CREATE TABLE prod
(
	-- 상품코드
	prod_code varchar2(30) NOT NULL,
	-- 정기권인지, 일반권인지, 회원예약지, 비회원예약인지
	-- 종류를 나타내는 코드
	prod_dcode varchar2(30),
	-- 상품명
	prod_name varchar2(300),
	-- 상품가격
	prod_price number,
	PRIMARY KEY (prod_code)
);


CREATE TABLE ticket
(
	-- 순번
	ticket_seq number NOT NULL,
	-- 이용시작일
	ticket_sdate varchar2(30),
	-- 이용종료일
	ticket_edate varchar2(30),
	-- 차량번호
	mem_carnum varchar2(60) NOT NULL,
	-- 상품코드
	prod_code varchar2(30) NOT NULL,
	PRIMARY KEY (ticket_seq)
);


CREATE TABLE tow
(
	-- 순번
	tow_seq number NOT NULL,
	-- 견인날짜
	tow_date varchar2(30),
	-- 견인사유
	tow_reason varchar2(4000),
	-- 차량번호
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

COMMENT ON COLUMN admins.admin_id IS '관리자아이디';
COMMENT ON COLUMN admins.admin_pw IS '관리자비밀번호';
COMMENT ON COLUMN admins.admin_name IS '관리자명';
COMMENT ON COLUMN bfree.bfree_seq IS '순번';
COMMENT ON COLUMN bfree.bfree_title IS '제목';
COMMENT ON COLUMN bfree.bfree_content IS '내용';
COMMENT ON COLUMN bfree.bfree_filename IS '첨부파일명';
COMMENT ON COLUMN bfree.bfree_filepath IS '첨부파일경로';
COMMENT ON COLUMN bfree.bfree_hit IS '조회수';
COMMENT ON COLUMN bfree.bfree_rpseq IS '댓글번호';
COMMENT ON COLUMN bfree.in_date IS '작성일자';
COMMENT ON COLUMN bfree.in_user_id IS '작성자';
COMMENT ON COLUMN bfree.up_date IS '수정일자';
COMMENT ON COLUMN bfree.up_user_id IS '수정자';
COMMENT ON COLUMN bfree.mem_carnum IS '차량번호';
COMMENT ON COLUMN bnotice.bnotice_seq IS '일련번호';
COMMENT ON COLUMN bnotice.bnotice_title IS '제목';
COMMENT ON COLUMN bnotice.bnotice_content IS '내용';
COMMENT ON COLUMN bnotice.bnotice_filename IS '첨부파일명';
COMMENT ON COLUMN bnotice.bnotice_filepath IS '첨부파일경로';
COMMENT ON COLUMN bnotice.bnotice_hit IS '조회수';
COMMENT ON COLUMN bnotice.in_user_id IS '작성자';
COMMENT ON COLUMN bnotice.up_date IS '수정일자';
COMMENT ON COLUMN bnotice.admin_id IS '관리자아이디';
COMMENT ON COLUMN book.book_seq IS '예약번호';
COMMENT ON COLUMN book.book_buydate IS '구매날짜';
COMMENT ON COLUMN book.book_sdate IS '예약날짜';
COMMENT ON COLUMN book.book_edate IS '종료일자';
COMMENT ON COLUMN book.book_cel_yn IS '취소여부';
COMMENT ON COLUMN book.mem_carnum IS '차량번호';
COMMENT ON COLUMN book.parkinfo_seq IS '자리번호';
COMMENT ON COLUMN book.prod_code IS '상품코드';
COMMENT ON COLUMN bsug.bnotice_title IS '제목';
COMMENT ON COLUMN bsug.bsug_title IS '제목';
COMMENT ON COLUMN bsug.bsug_content IS '내용';
COMMENT ON COLUMN bsug.bsug_filename IS '첨부파일명';
COMMENT ON COLUMN bsug.bsug_filepath IS '첨부파일경로';
COMMENT ON COLUMN bsug.bsug_hit IS '조회수';
COMMENT ON COLUMN bsug.bsug_rpseq IS '댓글번호';
COMMENT ON COLUMN bsug.in_date IS '작성일자';
COMMENT ON COLUMN bsug.in_user_id IS '작성자';
COMMENT ON COLUMN bsug.up_date IS '수정일자';
COMMENT ON COLUMN bsug.mem_carnum IS '차량번호';
COMMENT ON COLUMN members.mem_carnum IS '차량번호';
COMMENT ON COLUMN members.mem_name IS '이름';
COMMENT ON COLUMN members.mem_email IS '이메일';
COMMENT ON COLUMN members.mem_tel IS '전화번호';
COMMENT ON COLUMN members.mem_pw IS '비밀번호';
COMMENT ON COLUMN members.mem_ticket_yn IS '정기권여부';
COMMENT ON COLUMN members.mem_exit_yn IS '탈퇴여부';
COMMENT ON COLUMN members.mem_black_yn IS '블랙리스트여부';
COMMENT ON COLUMN members.sign_date IS '회원가입일';
COMMENT ON COLUMN members.signout_date IS '회원탈퇴일';
COMMENT ON COLUMN nticket.nticket_seq IS '순번';
COMMENT ON COLUMN nticket.nticket_indate IS '입차시간';
COMMENT ON COLUMN nticket.nticket_outdate IS '출차시간';
COMMENT ON COLUMN nticket.mem_carnum IS '차량번호';
COMMENT ON COLUMN nticket.parkinfo_seq IS '자리번호';
COMMENT ON COLUMN nticket.prod_code IS '상품코드';
COMMENT ON COLUMN parkinfo.parkinfo_seq IS '자리번호';
COMMENT ON COLUMN parkinfo.parkinfo_ticket_yn IS '정기권유무';
COMMENT ON COLUMN parkinfo.parkinfo_book_yn IS '예약유무';
COMMENT ON COLUMN parkinfo.parkinfo_use_yn IS '사용중여부';
COMMENT ON COLUMN prod.prod_code IS '상품코드';
COMMENT ON COLUMN prod.prod_dcode IS '정기권인지, 일반권인지, 회원예약지, 비회원예약인지 종류를 나타내는 코드';
COMMENT ON COLUMN prod.prod_name IS '상품명';
COMMENT ON COLUMN prod.prod_price IS '상품가격';
COMMENT ON COLUMN ticket.ticket_seq IS '순번';
COMMENT ON COLUMN ticket.ticket_sdate IS '이용시작일';
COMMENT ON COLUMN ticket.ticket_edate IS '이용종료일';
COMMENT ON COLUMN ticket.mem_carnum IS '차량번호';
COMMENT ON COLUMN ticket.prod_code IS '상품코드';
COMMENT ON COLUMN tow.tow_seq IS '순번';
COMMENT ON COLUMN tow.tow_date IS '견인날짜';
COMMENT ON COLUMN tow.tow_reason IS '견인사유';
COMMENT ON COLUMN tow.mem_carnum IS '차량번호';

CREATE OR REPLACE VIEW VW_SALES
AS
SELECT MEM_CARNUM, PROD_CODE, (SELECT PROD_PRICE FROM PROD WHERE PROD_CODE = PROD_CODE) PROD_PRICE FROM BOOK
UNION ALL
SELECT MEM_CARNUM, PROD_CODE, (SELECT PROD_PRICE FROM PROD WHERE PROD_CODE = PROD_CODE) PROD_PRICE FROM NTICKET
UNION ALL
SELECT MEM_CARNUM, PROD_CODE, (SELECT PROD_PRICE FROM PROD WHERE PROD_CODE = PROD_CODE) PROD_PRICE FROM TICKET;

SELECT *
FROM   VW_SALES;