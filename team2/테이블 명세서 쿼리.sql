--1. 테이블 명세서 쿼리
--번호,컬럼명,속성명,도메인,데이터타입,NULL여부,기본값,KEY
SELECT T.SEQ, T.COLUMN_ID, T.COMMENTS, 'N/A', T.DATA_TYPE, T.NULLABLE, T.DATA_DEFAULT, DECODE(T.PK,NULL,NULL,'P.K')||T.FK COL_KEY
FROM
(
SELECT
         COLUMN_ID AS SEQ
        ,( SELECT NVL(D.POSITION, '')
              FROM ALL_CONS_COLUMNS D
                 , all_constraints E
             WHERE D.OWNER           = UPPER('team2')
               AND D.OWNER           = A.OWNER
               AND D.TABLE_NAME      = A.TABLE_NAME
               AND D.COLUMN_NAME     = A.COLUMN_NAME
               AND D.OWNER           = E.OWNER
               AND D.TABLE_NAME      = E.TABLE_NAME
               AND D.CONSTRAINT_NAME = E.CONSTRAINT_NAME
               AND E.CONSTRAINT_TYPE = 'P') AS PK
        ,( SELECT CASE WHEN D.POSITION is null then ''
                       ELSE ' F.K'
                   END 
              FROM ALL_CONS_COLUMNS D
                 , all_constraints E
             WHERE D.OWNER           = UPPER('team2')
               AND D.OWNER           = A.OWNER
               AND D.TABLE_NAME      = A.TABLE_NAME
               AND D.COLUMN_NAME     = A.COLUMN_NAME
               AND D.OWNER           = E.OWNER
               AND D.TABLE_NAME      = E.TABLE_NAME
               AND D.CONSTRAINT_NAME = E.CONSTRAINT_NAME
               AND E.CONSTRAINT_TYPE = 'R') AS FK                  
         , A.COLUMN_NAME AS COLUMN_ID
         , C.COMMENTS
         , A.DATA_TYPE
         , A.DATA_LENGTH
         , A.NULLABLE
         , A.DATA_DEFAULT
      FROM ALL_TAB_COLUMNS  A
         , ALL_TAB_COMMENTS B
         , ALL_COL_COMMENTS C
        WHERE A.OWNER = UPPER('team2')
        AND B.OWNER = UPPER('team2')
        AND C.OWNER = UPPER('team2')
        AND A.OWNER = B.OWNER
        AND A.OWNER = C.OWNER
        AND A.TABLE_NAME  = B.TABLE_NAME
        AND A.TABLE_NAME  = C.TABLE_NAME
        AND A.COLUMN_NAME = C.COLUMN_NAME
        AND A.TABLE_NAME = UPPER('USER_INFO')
        ORDER BY 1
) T;


--2. 자료사전 쿼리
--표준속성명,표준영문명,타입,길이,설명,비고
SELECT T.COMMENTS, T.COLUMN_ID, T.DATA_TYPE, T.DATA_LENGTH, T.COMMENTS
FROM
(
SELECT
         COLUMN_ID AS SEQ
        ,( SELECT NVL(D.POSITION, '')
              FROM ALL_CONS_COLUMNS D
                 , all_constraints E
             WHERE D.OWNER           = UPPER('team2')
               AND D.OWNER           = A.OWNER
               AND D.TABLE_NAME      = A.TABLE_NAME
               AND D.COLUMN_NAME     = A.COLUMN_NAME
               AND D.OWNER           = E.OWNER
               AND D.TABLE_NAME      = E.TABLE_NAME
               AND D.CONSTRAINT_NAME = E.CONSTRAINT_NAME
               AND E.CONSTRAINT_TYPE = 'P') AS PK
        ,( SELECT CASE WHEN D.POSITION is null then ''
                       ELSE ' F.K'
                   END 
              FROM ALL_CONS_COLUMNS D
                 , all_constraints E
             WHERE D.OWNER           = UPPER('team2')
               AND D.OWNER           = A.OWNER
               AND D.TABLE_NAME      = A.TABLE_NAME
               AND D.COLUMN_NAME     = A.COLUMN_NAME
               AND D.OWNER           = E.OWNER
               AND D.TABLE_NAME      = E.TABLE_NAME
               AND D.CONSTRAINT_NAME = E.CONSTRAINT_NAME
               AND E.CONSTRAINT_TYPE = 'R') AS FK                  
         , A.COLUMN_NAME AS COLUMN_ID
         , C.COMMENTS
         , A.DATA_TYPE
         , A.DATA_LENGTH
         , A.NULLABLE
         , A.DATA_DEFAULT
      FROM ALL_TAB_COLUMNS  A
         , ALL_TAB_COMMENTS B
         , ALL_COL_COMMENTS C
        WHERE A.OWNER = UPPER('team2')
        AND B.OWNER = UPPER('team2')
        AND C.OWNER = UPPER('team2')
        AND A.OWNER = B.OWNER
        AND A.OWNER = C.OWNER
        AND A.TABLE_NAME  = B.TABLE_NAME
        AND A.TABLE_NAME  = C.TABLE_NAME
        AND A.COLUMN_NAME = C.COLUMN_NAME
) T;

--용어명,영문Full명,설명
SELECT T.COMMENTS, T.COLUMN_ID, T.COMMENTS
FROM
(
SELECT
         COLUMN_ID AS SEQ
        ,( SELECT NVL(D.POSITION, '')
              FROM ALL_CONS_COLUMNS D
                 , all_constraints E
             WHERE D.OWNER           = UPPER('team2')
               AND D.OWNER           = A.OWNER
               AND D.TABLE_NAME      = A.TABLE_NAME
               AND D.COLUMN_NAME     = A.COLUMN_NAME
               AND D.OWNER           = E.OWNER
               AND D.TABLE_NAME      = E.TABLE_NAME
               AND D.CONSTRAINT_NAME = E.CONSTRAINT_NAME
               AND E.CONSTRAINT_TYPE = 'P') AS PK
        ,( SELECT CASE WHEN D.POSITION is null then ''
                       ELSE ' F.K'
                   END 
              FROM ALL_CONS_COLUMNS D
                 , all_constraints E
             WHERE D.OWNER           = UPPER('team2')
               AND D.OWNER           = A.OWNER
               AND D.TABLE_NAME      = A.TABLE_NAME
               AND D.COLUMN_NAME     = A.COLUMN_NAME
               AND D.OWNER           = E.OWNER
               AND D.TABLE_NAME      = E.TABLE_NAME
               AND D.CONSTRAINT_NAME = E.CONSTRAINT_NAME
               AND E.CONSTRAINT_TYPE = 'R') AS FK                  
         , A.COLUMN_NAME AS COLUMN_ID
         , C.COMMENTS
         , A.DATA_TYPE
         , A.DATA_LENGTH
         , A.NULLABLE
         , A.DATA_DEFAULT
      FROM ALL_TAB_COLUMNS  A
         , ALL_TAB_COMMENTS B
         , ALL_COL_COMMENTS C
        WHERE A.OWNER = UPPER('team2')
        AND B.OWNER = UPPER('team2')
        AND C.OWNER = UPPER('team2')
        AND A.OWNER = B.OWNER
        AND A.OWNER = C.OWNER
        AND A.TABLE_NAME  = B.TABLE_NAME
        AND A.TABLE_NAME  = C.TABLE_NAME
        AND A.COLUMN_NAME = C.COLUMN_NAME
        ORDER BY A.TABLE_NAME, C.COLUMN_NAME
) T;