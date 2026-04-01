CREATE VIEW view1 AS
SELECT emp_name, location
FROM employee
WHERE job_domain="marketing";

SELECT * FROM view1;

CREATE OR REPLACE VIEW view1 AS
SELECT emp_name, location
FROM employee
WHERE job_domain="sales";

SELECT * FROM view1;

CREATE VIEW view2 AS
select employee.emp_id, emp_name, job_domain, salary
from employee
inner join income
on employee.emp_id=income.emp_id;

SELECT * FROM view2;

DROP VIEW view2;

