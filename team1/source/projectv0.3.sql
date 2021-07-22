
/* Drop Tables */

DROP TABLE comm CASCADE CONSTRAINTS;
DROP TABLE bbs CASCADE CONSTRAINTS;
DROP TABLE bkmk CASCADE CONSTRAINTS;
DROP TABLE evl CASCADE CONSTRAINTS;
DROP TABLE faq CASCADE CONSTRAINTS;
DROP TABLE reco CASCADE CONSTRAINTS;
DROP TABLE movie CASCADE CONSTRAINTS;
DROP TABLE genre CASCADE CONSTRAINTS;
DROP TABLE nation CASCADE CONSTRAINTS;
DROP TABLE notice CASCADE CONSTRAINTS;
DROP TABLE PAYMENT CASCADE CONSTRAINTS;
DROP TABLE qestn CASCADE CONSTRAINTS;
DROP TABLE ticket CASCADE CONSTRAINTS;
DROP TABLE users CASCADE CONSTRAINTS;




/* Create Tables */

CREATE TABLE bbs
(
	-- 글번호
	bss_no number NOT NULL UNIQUE,
	-- 사용자아이디
	user_id varchar2(15 char) NOT NULL UNIQUE,
	-- 제목
	titile varchar2(30 char),
	-- 내용
	content varchar2(4000),
	-- 첨부파일
	-- 
	attach_file varchar2(50),
	-- 파일경로
	attach_path varchar2(100 char),
	-- 조회수
	rdcnt number,
	-- 작성자
	writer varchar2(20 char),
	-- 등록일
	in_date varchar2(20 char),
	-- 등록자아이디
	in_user_id varchar2(15 char),
	-- 수정일자
	up_date varchar2(20 char),
	-- 수정자아이디
	up_user_id varchar2(15 char),
	PRIMARY KEY (bss_no)
);


CREATE TABLE bkmk
(
	-- 사용자아이디
	user_id varchar2(15 char) NOT NULL UNIQUE,
	-- 영화번호
	movie_no number NOT NULL UNIQUE,
	-- 등록일
	in_date varchar2(20 char),
	-- 등록자아이디
	in_user_id varchar2(15 char),
	-- 수정일
	up_date varchar2(20 char),
	-- 수정자아이디
	up_user_id varchar2(15 char),
	PRIMARY KEY (user_id, movie_no)
);


CREATE TABLE comm
(
	-- 글번호
	bss_no number NOT NULL UNIQUE,
	-- 댓글번호
	comm_no number NOT NULL,
	-- 사용자아이디
	user_id varchar2(15 char) NOT NULL UNIQUE,
	-- 댓글내용
	content varchar2(4000),
	-- 좋아요
	likes number,
	-- 싫어요
	dislike number,
	-- 등록일
	in_date varchar2(20 char),
	-- 등록자아이디
	in_user_id varchar2(15 char),
	-- 수정일
	up_date varchar2(20 char),
	-- 수정자아이디
	up_user_id varchar2(15 char),
	PRIMARY KEY (bss_no, comm_no)
);


CREATE TABLE evl
(
	-- 사용자아이디
	user_id varchar2(15 char) NOT NULL UNIQUE,
	-- 영화코드
	-- 
	movie_no number NOT NULL UNIQUE,
	-- 평점
	rate number(1,1),
	-- 등록일
	in_date varchar2(20 char),
	-- 등록자아이디
	in_user_id varchar2(15 char),
	up_date varchar2(20 char),
	-- 수정자아이디
	up_user_id varchar2(15 char),
	PRIMARY KEY (user_id, movie_no)
);


CREATE TABLE faq
(
	-- faq번호
	faq_no number NOT NULL UNIQUE,
	-- 사용자아이디
	user_id varchar2(15 char) NOT NULL UNIQUE,
	-- faq제목
	title varchar2(30 char),
	-- faq내용
	content varchar2(4000),
	-- faq작성자
	writer varchar2(20 char),
	-- 등록일
	in_date varchar2(20 char),
	-- 등록자아이디
	in_user_id varchar2(15 char),
	-- 수정일자
	up_date varchar2(20 char),
	up_user_id varchar2(15 char),
	PRIMARY KEY (faq_no)
);


CREATE TABLE genre
(
	-- 장르코드
	genre_code varchar2(10 char) NOT NULL UNIQUE,
	-- 장르명
	name varchar2(20 char),
	-- 등록일
	in_date varchar2(20 char),
	-- 등록자아이디
	in_user_id varchar2(15 char),
	-- 수정일
	up_date varchar2(20 char),
	-- 수정자아이디
	up_user_id varchar2(15 char),
	PRIMARY KEY (genre_code)
);


CREATE TABLE movie
(
	-- 영화번호
	movie_no number NOT NULL UNIQUE,
	-- 장르코드
	genre_code varchar2(10 char) NOT NULL UNIQUE,
	-- 국가코드
	nation_code varchar2(3 char) NOT NULL UNIQUE,
	-- 영화제목
	title varchar2(50 char),
	-- 감독
	director varchar2(30 char),
	-- 배우
	actor varchar2(100 char),
	-- 런타임
	runtime varchar2(10 char),
	-- 개봉일
	release_date varchar2(20 char),
	-- 포스터
	poster varchar2(100 char),
	-- 영상경로
	url varchar2(300 char),
	-- 스트리밍 회수
	stream_cnt number,
	-- 등록일
	in_date varchar2(20 char),
	-- 등록자아이디
	in_user_id varchar2(15 char),
	-- 수정일
	up_date varchar2(20 char),
	-- 수정자아이디
	up_user_id varchar2(15 char),
	PRIMARY KEY (movie_no)
);


CREATE TABLE nation
(
	-- 국가코드
	nation_code varchar2(3 char) NOT NULL UNIQUE,
	-- 국가명
	name varchar2(20 char),
	-- 등록일
	in_date varchar2(20 char),
	-- 등록자아이디
	in_user_id varchar2(15 char),
	-- 수정일
	up_date varchar2(20 char),
	-- 수정자아이디
	up_user_id varchar2(15 char),
	PRIMARY KEY (nation_code)
);


CREATE TABLE notice
(
	-- 공지번호
	notice_no number NOT NULL UNIQUE,
	-- 사용자아이디
	user_id varchar2(15 char) NOT NULL UNIQUE,
	-- 공지제목
	title varchar2(30 char),
	-- 공지내용
	content varchar2(4000),
	-- 첨부파일
	attach_file varchar2(50 char),
	-- 파일경로
	attach_path varchar2(100 char),
	-- 조회수
	rdcnt number,
	-- 등록일
	in_date varchar2(20 char),
	-- 등록자아이디
	in_user_id varchar2(15 char),
	-- 수정일
	up_date varchar2(20 char),
	-- 수정자아이디
	up_user_id varchar2(15 char),
	PRIMARY KEY (notice_no)
);


CREATE TABLE PAYMENT
(
	-- 사용자아이디
	user_id varchar2(15 char) NOT NULL UNIQUE,
	-- 이용권 번호
	ticket_no number NOT NULL,
	-- 결제일
	payday varchar2(2 char),
	-- 결제여부
	payment_flag varchar2(1 char),
	-- 갱신 예정일
	payment_renew varchar2(20 char),
	-- 등록일
	in_date varchar2(20 char),
	-- 등록자아이디
	in_user_id varchar2(15 char),
	-- 수정일
	up_date varchar2(20 char),
	-- 수정자아이디
	up_date_id varchar2(15 char),
	PRIMARY KEY (user_id, ticket_no)
);


CREATE TABLE qestn
(
	-- 질문번호
	qestn_no number NOT NULL UNIQUE,
	-- 사용자아이디
	user_id varchar2(15 char) NOT NULL UNIQUE,
	-- 질문제목
	title varchar2(30 char),
	-- 질문내용
	content varchar2(4000),
	-- 질문작성자
	writer varchar2(20 char),
	-- 질문답변
	answer varchar2(4000),
	-- 질문답변자
	answrr varchar2(20 char),
	-- 등록일
	in_date varchar2(20 char),
	-- 등록자아이디
	id_user_id varchar2(15 char),
	-- 수정일
	up_date varchar2(20 char),
	-- 수정자아이디
	up_user_id varchar2(15 char),
	PRIMARY KEY (qestn_no)
);


CREATE TABLE reco
(
	-- 사용자아이디
	user_id varchar2(15 char) NOT NULL UNIQUE,
	-- 영화번호
	movie_no number NOT NULL UNIQUE,
	-- 등록일
	in_date varchar2(20 char),
	-- 등록자아이디
	in_user_id varchar2(15 char),
	up_date varchar2(20 char),
	-- 수정자아이디
	up_user_id varchar2(15 char),
	PRIMARY KEY (user_id, movie_no)
);


CREATE TABLE ticket
(
	-- 이용권 번호
	ticket_no number NOT NULL,
	-- 요금명
	name varchar2(300),
	price number,
	-- 등록일
	-- 
	in_date varchar2(20 char),
	-- 등록자아이디
	in_user_id varchar2(15 char),
	-- 수정일
	up_date varchar2(20 char),
	-- 수정자아이디
	up_user_id varchar2(15 char),
	PRIMARY KEY (ticket_no)
);


CREATE TABLE users
(
	-- 사용자아이디
	user_id varchar2(15 char) NOT NULL UNIQUE,
	-- 이름
	user_nm varchar2(20 char),
	-- 비밀번호
	user_password varchar2(15 char),
	-- 전화번호
	user_telno varchar2(11 char),
	-- 이메일
	user_email varchar2(50 char),
	-- 관리자구분
	mngr_flag varchar2(1 char),
	-- 탈퇴여부
	-- 
	act_flag varchar2(1 char),
	-- 등록일
	in_date varchar2(20 char),
	-- 등록자아이디
	in_user_id varchar2(15 char),
	-- 수정일
	up_date varchar2(20 char),
	-- 수정자아이디
	up_user_id varchar2(15 char),
	PRIMARY KEY (user_id)
);



/* Create Foreign Keys */

ALTER TABLE comm
	ADD FOREIGN KEY (bss_no)
	REFERENCES bbs (bss_no)
;


ALTER TABLE movie
	ADD FOREIGN KEY (genre_code)
	REFERENCES genre (genre_code)
;


ALTER TABLE bkmk
	ADD FOREIGN KEY (movie_no)
	REFERENCES movie (movie_no)
;


ALTER TABLE evl
	ADD FOREIGN KEY (movie_no)
	REFERENCES movie (movie_no)
;


ALTER TABLE reco
	ADD FOREIGN KEY (movie_no)
	REFERENCES movie (movie_no)
;


ALTER TABLE movie
	ADD FOREIGN KEY (nation_code)
	REFERENCES nation (nation_code)
;


ALTER TABLE PAYMENT
	ADD FOREIGN KEY (ticket_no)
	REFERENCES ticket (ticket_no)
;


ALTER TABLE bbs
	ADD FOREIGN KEY (user_id)
	REFERENCES users (user_id)
;


ALTER TABLE bkmk
	ADD FOREIGN KEY (user_id)
	REFERENCES users (user_id)
;


ALTER TABLE comm
	ADD FOREIGN KEY (user_id)
	REFERENCES users (user_id)
;


ALTER TABLE evl
	ADD FOREIGN KEY (user_id)
	REFERENCES users (user_id)
;


ALTER TABLE faq
	ADD FOREIGN KEY (user_id)
	REFERENCES users (user_id)
;


ALTER TABLE notice
	ADD FOREIGN KEY (user_id)
	REFERENCES users (user_id)
;


ALTER TABLE PAYMENT
	ADD FOREIGN KEY (user_id)
	REFERENCES users (user_id)
;


ALTER TABLE qestn
	ADD FOREIGN KEY (user_id)
	REFERENCES users (user_id)
;


ALTER TABLE reco
	ADD FOREIGN KEY (user_id)
	REFERENCES users (user_id)
;



/* Comments */

COMMENT ON COLUMN bbs.bss_no IS '글번호';
COMMENT ON COLUMN bbs.user_id IS '사용자아이디';
COMMENT ON COLUMN bbs.titile IS '제목';
COMMENT ON COLUMN bbs.content IS '내용';
COMMENT ON COLUMN bbs.attach_file IS '첨부파일
';
COMMENT ON COLUMN bbs.attach_path IS '파일경로';
COMMENT ON COLUMN bbs.rdcnt IS '조회수';
COMMENT ON COLUMN bbs.writer IS '작성자';
COMMENT ON COLUMN bbs.in_date IS '등록일';
COMMENT ON COLUMN bbs.in_user_id IS '등록자아이디';
COMMENT ON COLUMN bbs.up_date IS '수정일자';
COMMENT ON COLUMN bbs.up_user_id IS '수정자아이디';
COMMENT ON COLUMN bkmk.user_id IS '사용자아이디';
COMMENT ON COLUMN bkmk.movie_no IS '영화번호';
COMMENT ON COLUMN bkmk.in_date IS '등록일';
COMMENT ON COLUMN bkmk.in_user_id IS '등록자아이디';
COMMENT ON COLUMN bkmk.up_date IS '수정일';
COMMENT ON COLUMN bkmk.up_user_id IS '수정자아이디';
COMMENT ON COLUMN comm.bss_no IS '글번호';
COMMENT ON COLUMN comm.comm_no IS '댓글번호';
COMMENT ON COLUMN comm.user_id IS '사용자아이디';
COMMENT ON COLUMN comm.content IS '댓글내용';
COMMENT ON COLUMN comm.likes IS '좋아요';
COMMENT ON COLUMN comm.dislike IS '싫어요';
COMMENT ON COLUMN comm.in_date IS '등록일';
COMMENT ON COLUMN comm.in_user_id IS '등록자아이디';
COMMENT ON COLUMN comm.up_date IS '수정일';
COMMENT ON COLUMN comm.up_user_id IS '수정자아이디';
COMMENT ON COLUMN evl.user_id IS '사용자아이디';
COMMENT ON COLUMN evl.movie_no IS '영화코드
';
COMMENT ON COLUMN evl.rate IS '평점';
COMMENT ON COLUMN evl.in_date IS '등록일';
COMMENT ON COLUMN evl.in_user_id IS '등록자아이디';
COMMENT ON COLUMN evl.up_user_id IS '수정자아이디';
COMMENT ON COLUMN faq.faq_no IS 'faq번호';
COMMENT ON COLUMN faq.user_id IS '사용자아이디';
COMMENT ON COLUMN faq.title IS 'faq제목';
COMMENT ON COLUMN faq.content IS 'faq내용';
COMMENT ON COLUMN faq.writer IS 'faq작성자';
COMMENT ON COLUMN faq.in_date IS '등록일';
COMMENT ON COLUMN faq.in_user_id IS '등록자아이디';
COMMENT ON COLUMN faq.up_date IS '수정일자';
COMMENT ON COLUMN genre.genre_code IS '장르코드';
COMMENT ON COLUMN genre.name IS '장르명';
COMMENT ON COLUMN genre.in_date IS '등록일';
COMMENT ON COLUMN genre.in_user_id IS '등록자아이디';
COMMENT ON COLUMN genre.up_date IS '수정일';
COMMENT ON COLUMN genre.up_user_id IS '수정자아이디';
COMMENT ON COLUMN movie.movie_no IS '영화번호';
COMMENT ON COLUMN movie.genre_code IS '장르코드';
COMMENT ON COLUMN movie.nation_code IS '국가코드';
COMMENT ON COLUMN movie.title IS '영화제목';
COMMENT ON COLUMN movie.director IS '감독';
COMMENT ON COLUMN movie.actor IS '배우';
COMMENT ON COLUMN movie.runtime IS '런타임';
COMMENT ON COLUMN movie.release_date IS '개봉일';
COMMENT ON COLUMN movie.poster IS '포스터';
COMMENT ON COLUMN movie.url IS '영상경로';
COMMENT ON COLUMN movie.stream_cnt IS '스트리밍 회수';
COMMENT ON COLUMN movie.in_date IS '등록일';
COMMENT ON COLUMN movie.in_user_id IS '등록자아이디';
COMMENT ON COLUMN movie.up_date IS '수정일';
COMMENT ON COLUMN movie.up_user_id IS '수정자아이디';
COMMENT ON COLUMN nation.nation_code IS '국가코드';
COMMENT ON COLUMN nation.name IS '국가명';
COMMENT ON COLUMN nation.in_date IS '등록일';
COMMENT ON COLUMN nation.in_user_id IS '등록자아이디';
COMMENT ON COLUMN nation.up_date IS '수정일';
COMMENT ON COLUMN nation.up_user_id IS '수정자아이디';
COMMENT ON COLUMN notice.notice_no IS '공지번호';
COMMENT ON COLUMN notice.user_id IS '사용자아이디';
COMMENT ON COLUMN notice.title IS '공지제목';
COMMENT ON COLUMN notice.content IS '공지내용';
COMMENT ON COLUMN notice.attach_file IS '첨부파일';
COMMENT ON COLUMN notice.attach_path IS '파일경로';
COMMENT ON COLUMN notice.rdcnt IS '조회수';
COMMENT ON COLUMN notice.in_date IS '등록일';
COMMENT ON COLUMN notice.in_user_id IS '등록자아이디';
COMMENT ON COLUMN notice.up_date IS '수정일';
COMMENT ON COLUMN notice.up_user_id IS '수정자아이디';
COMMENT ON COLUMN PAYMENT.user_id IS '사용자아이디';
COMMENT ON COLUMN PAYMENT.ticket_no IS '이용권 번호';
COMMENT ON COLUMN PAYMENT.payday IS '결제일';
COMMENT ON COLUMN PAYMENT.payment_flag IS '결제여부';
COMMENT ON COLUMN PAYMENT.payment_renew IS '갱신 예정일';
COMMENT ON COLUMN PAYMENT.in_date IS '등록일';
COMMENT ON COLUMN PAYMENT.in_user_id IS '등록자아이디';
COMMENT ON COLUMN PAYMENT.up_date IS '수정일';
COMMENT ON COLUMN PAYMENT.up_date_id IS '수정자아이디';
COMMENT ON COLUMN qestn.qestn_no IS '질문번호';
COMMENT ON COLUMN qestn.user_id IS '사용자아이디';
COMMENT ON COLUMN qestn.title IS '질문제목';
COMMENT ON COLUMN qestn.content IS '질문내용';
COMMENT ON COLUMN qestn.writer IS '질문작성자';
COMMENT ON COLUMN qestn.answer IS '질문답변';
COMMENT ON COLUMN qestn.answrr IS '질문답변자';
COMMENT ON COLUMN qestn.in_date IS '등록일';
COMMENT ON COLUMN qestn.id_user_id IS '등록자아이디';
COMMENT ON COLUMN qestn.up_date IS '수정일';
COMMENT ON COLUMN qestn.up_user_id IS '수정자아이디';
COMMENT ON COLUMN reco.user_id IS '사용자아이디';
COMMENT ON COLUMN reco.movie_no IS '영화번호';
COMMENT ON COLUMN reco.in_date IS '등록일';
COMMENT ON COLUMN reco.in_user_id IS '등록자아이디';
COMMENT ON COLUMN reco.up_user_id IS '수정자아이디';
COMMENT ON COLUMN ticket.ticket_no IS '이용권 번호';
COMMENT ON COLUMN ticket.name IS '요금명';
COMMENT ON COLUMN ticket.in_date IS '등록일
';
COMMENT ON COLUMN ticket.in_user_id IS '등록자아이디';
COMMENT ON COLUMN ticket.up_date IS '수정일';
COMMENT ON COLUMN ticket.up_user_id IS '수정자아이디';
COMMENT ON COLUMN users.user_id IS '사용자아이디';
COMMENT ON COLUMN users.user_nm IS '이름';
COMMENT ON COLUMN users.user_password IS '비밀번호';
COMMENT ON COLUMN users.user_telno IS '전화번호';
COMMENT ON COLUMN users.user_email IS '이메일';
COMMENT ON COLUMN users.mngr_flag IS '관리자구분';
COMMENT ON COLUMN users.act_flag IS '탈퇴여부
';
COMMENT ON COLUMN users.in_date IS '등록일';
COMMENT ON COLUMN users.in_user_id IS '등록자아이디';
COMMENT ON COLUMN users.up_date IS '수정일';
COMMENT ON COLUMN users.up_user_id IS '수정자아이디';



