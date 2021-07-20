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
