create database testdb using codeset utf-8 territory CN

list tablespaces show detail

--版本查看

SELECT SERVICE_LEVEL FROM SYSIBMADM.ENV_INST_INFO

CREATE TABLE product_info (
  product_id varchar(32) NOT NULL,
  product_name varchar(64),
)

create table student(id int, name varchar(30));

rename table student to students;

select * from product_info;

insert into students values(0, 'testname1' );
insert into students values(0, 'testname3'  );

select * from students;

alter table students add birthday varchar(30)

update students set birthday="1995-01-01" where name="testname"