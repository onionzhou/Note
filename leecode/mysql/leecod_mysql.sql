
'''
183. Customers Who Never Order easy
 某网站包含两个表，Customers 表和 Orders 表。编写一个 SQL 查询，找出所有从不订购任何东西的客户。

Customers 表：

+----+-------+
| Id | Name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
Orders 表：

+----+------------+
| Id | CustomerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
例如给定上述表格，你的查询应返回：

+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/customers-who-never-order
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

select c.Name as 'Customers' from Customers as c where c.Id not in(
    select CustomerID from Orders
)

select c.Name as 'Customers' from Customers as c
left join Orders as o on c.id = o.CustomerId
where o.id is null


'''
184. 部门工资最高的员工
Employee 表包含所有员工信息，每个员工有其对应的 Id, salary 和 department Id。

+----+-------+--------+--------------+
| Id | Name  | Salary | DepartmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Henry | 80000  | 2            |
| 3  | Sam   | 60000  | 2            |
| 4  | Max   | 90000  | 1            |
+----+-------+--------+--------------+
Department 表包含公司所有部门的信息。

+----+----------+
| Id | Name     |
+----+----------+
| 1  | IT       |
| 2  | Sales    |
+----+----------+
编写一个 SQL 查询，找出每个部门工资最高的员工。例如，根据上述给定的表格，Max 在 IT 部门有最高工资，Henry 在 Sales 部门有最高工资。

+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Max      | 90000  |
| Sales      | Henry    | 80000  |
+------------+----------+--------+

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/department-highest-salary
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
思路就是在Employee表中以DepartmentId分组找出所有部门的最大工资，然后再在连接的临时表中查询等于最大工资的员工！
 '''
select
      Department.Name as 'Department' ,
      Employee.Name as 'Employee',
      Employee.Salary
from
      Employee
join  Department
on    Employee.DepartmentId =Department.Id
and (Employee.DepartmentId,Employee.Salary )
in (select DepartmentId , max(Salary) from Employee  group by DepartmentId);


select
    d.Name as Department,
    e.Name as Employee,
    e.Salary
from
    Employee e,Department d
where
    e.DepartmentId=d.id
    and
    (e.Salary,e.DepartmentId) in (select max(Salary),DepartmentId from Employee group by DepartmentId);