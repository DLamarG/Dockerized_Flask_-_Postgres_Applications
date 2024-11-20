DO
$do$
BEGIN
   IF NOT EXISTS (SELECT FROM pg_database WHERE datname = 'students') THEN
      CREATE DATABASE students;
   END IF;
END
$do$;

\c students;

CREATE TABLE IF NOT EXISTS student (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INTEGER,
    grade CHAR(1)
);

INSERT INTO student (first_name, last_name, age, grade) 
SELECT * FROM (VALUES
    ('John', 'Doe', 20, 'A'),
    ('Jane', 'Smith', 22, 'B'),
    ('Alice', 'Johnson', 21, 'C')
) AS data(first_name, last_name, age, grade)
WHERE NOT EXISTS (
    SELECT 1 
    FROM student 
    WHERE student.first_name = data.first_name 
    AND student.last_name = data.last_name
    AND student.age = data.age 
    AND student.grade = data.grade
);

