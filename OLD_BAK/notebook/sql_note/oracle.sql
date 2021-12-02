
--查看所有用户
select * from all_users;

--版本查看
select banner from sys.v_$version;

--查看当前连接数

select * from v$session where username is not null
--create  database
CREATE TABLESPACE testdb LOGGING DATAFILE 'testdb.dbf' SIZE 100M AUTOEXTEND ON NEXT 32M MAXSIZE 500M EXTENT MANAGEMENT LOCAL;

-- create table

create table student
(
    id varchar(12),
    name varchar(12)
)
tablespace testdb;

select * from student;

insert into student values(0, 'testname');

alter table student rename to students;

drop table students;

select name from v$database;

