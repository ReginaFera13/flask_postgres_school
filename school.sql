DROP TABLE IF EXISTS students;
CREATE TABLE students (
  id           serial PRIMARY KEY,
  first_name   varchar(255) NOT NULL,
  last_name    varchar(255) NOT NULL,
  age          integer NOT NULL,
  subject      integer NOT NULL
);

DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
  id           serial PRIMARY KEY,
  first_name   varchar(255) NOT NULL,
  last_name    varchar(255) NOT NULL,
  age          integer NOT NULL,
  subject      integer NOT NULL
);

DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects (
  id           serial PRIMARY KEY,
  subject      varchar(255) NOT NULL
);


-- \COPY students FROM '/home/reginafera13/codeplatoon/flask_postgres_school/data/student.csv' DELIMITER ',' CSV HEADER;

-- \COPY teachers FROM '/home/reginafera13/codeplatoon/flask_postgres_school/data/teachers.csv' DELIMITER ',' CSV HEADER;

-- \COPY subjects FROM '/home/reginafera13/codeplatoon/flask_postgres_school/data/subjects.csv' DELIMITER ',' CSV HEADER;