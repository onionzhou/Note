
select version();

create database testdb;

create table student(id int, name varchar(30));

----修改表名
alter table student rename to students

---修改表字段

alter table students add column birthday text;

insert into students values(0, 'testname',  '1990-01-01');

insert into students values(0, 'testname1',  '1990-01-01');

select * from students;

update students set birthday='1995-01-01' where name='testname';

select * from students;

begin;
insert into students values(0, 'testname2',  '1990-01-01');
rollback;


begin;
insert into students values(0, 'testname3',  '1990-01-01');
insert into students values(0, 'testname4',  '1990-01-01');
commit;

delete from students where name='testname';

drop table students;

drop DATABASE testdb;

create user test with password '123456';
alter user test password '1234561';
GRANT ALL PRIVILEGES ON DATABASE testdb TO test;

revoke ALL  ON DATABASE testdb from test;
DROP USER test

select * from pg_user;


# 存储过程  表结构