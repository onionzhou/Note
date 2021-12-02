CREATE SCHEMA "testdb";

create table "testdb"."student"
(
"id" INTEGER,
"name" CHAR(100)
)

SELECT "id", "name" FROM "TESTDB"."testdb"."student";

INSERT INTO "TESTDB"."testdb"."student"("id","name") VALUES(123,'qwe');
INSERT INTO "TESTDB"."testdb"."student"  VALUES(123,'qwde');
DELETE FROM "TESTDB"."testdb"."student" WHERE id=123;
UPDATE "TESTDB"."testdb"."student" SET "id" = 12223,"name" = 'onion';
---版本查询
select * from v$version;

DROP SCHEMA "TESTDB"."testdb" CASCADE;

create table "student"
(
"id" INTEGER,
"name" CHAR(100)
)
INSERT INTO "student"  VALUES(123,'qwde');

select * from "student";



达梦7
1.查询会话中程序占用会话数

select appname,count(*) from v$sessions group by  "V$SESSIONS".APPNAME;
2.查看用户下指定表占用空间

SELECT TABLE_USED_SPACE('username','tablename')*SF_GET_PAGE_SIZE()/1024/1024||'M'
3.查看用户下指定表实际使用的空间

SELECT TABLE_USED_PAGES('unsername','tablename')*SF_GET_PAGE_SIZE()/1024/1024||'M'

达梦6
1.查询cpu占用较长时间未释放的sql

select sql_text,app_name,login_name,cpu_time_call frome v$session where cpu_time_call > 1000;






