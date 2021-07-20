---10.0.80.2
---Microsoft SQL Server 2017 (RTM-CU9-GDR) (KB4293805) - 14.0.3035.2 (X64)   Jul  6 2018 18:24:36   Copyright (C) 2017 Microsoft Corporation  Express Edition (64-bit) on Linux (CentOS Linux 7 (Core))
---版本查看
SELECT @@VERSION

create database testdb;

--数据库查看
SELECT name, database_id, create_date
FROM sys.databases ;

use testdb1;
create table student(id int, name varchar(30));

EXEC sp_rename 'student', 'students';

alter table students add birthday varchar(200) null;

insert into students values(0, 'testname1',  '1990-01-01');
insert into students values(0, 'testname1',  '1990-01-01');

update students set birthday='1995-01-01' where name='testname';


begin transaction
insert into students values(0, 'testname2',  '1990-01-01');
rollback transaction

begin transaction;
insert into students values(0, 'testname2',  '1990-01-01');
insert into students values(0, 'testname3',  '1990-01-01');
commit transaction

--查看表结构
sp_help students;

delete from students where name='testname';

--存储过程
CREATE PROCEDURE PR_Sum2
    @a int,
    @b int
AS
BEGIN
    Return @a+@b
END

----执行存储
declare @mysum2 int
execute @mysum2= PR_Sum2 1,2
print @mysum2

drop DATABASE testdb1;


CREATE LOGIN Jack WITH PASSWORD = '1qaz@WSX'
go

create login testuser with password='abcd1234@', default_database=testdb1

create user testuser for login testuser with default_schema=dbo