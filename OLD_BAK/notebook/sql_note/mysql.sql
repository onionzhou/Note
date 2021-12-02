
create database testdb;

show databases;

use testdb;

create table student(id int, name varchar(30));

rename table student to students;

alter table students add birthday datetime;

insert into students values(0, "testname",  "1990-01-01");
insert into students values(0, "testname1",  "1990-01-01");

select * from students;

update students set birthday="1995-01-01" where name="testname";

select * from students;


#----事务操作-------

begin;
insert into students values(0, "testname2",  "1990-01-01");
rollback;

select * from students;

begin;
insert into students values(0, "testname3",  "1990-01-01");
insert into students values(0, "testname4",  "1990-01-01");
commit;

select * from students;

desc table students;

delete from students where name="testname";





#--------存储过程----------

 delimiter $$
CREATE PROCEDURE search_students()
  BEGIN
    select * from students;
  END$$

 delimiter ;;


drop DATABASE testdb;

CREATE USER 'user1'@'%' IDENTIFIED BY '123456';

SET PASSWORD FOR 'user1'@'%' = PASSWORD('1234567');

GRANT ALL ON *.* TO 'user1'@'%' identified by '1234567';

SHOW GRANTS FOR 'user1'@'%';

flush privileges;

REVOKE SELECT ON *.* FROM 'user1'@'%';

DROP USER 'user1'