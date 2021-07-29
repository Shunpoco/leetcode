CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    declare V int;
    set V = N - 1;
  RETURN (
      # Write your MySQL query statement below.
      select
        (select distinct salary from employee order by salary desc limit 1 offset V)
  );
END
