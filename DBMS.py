Create Table Student
(
Student_Id number(5),
Student_Name varchar(20),
Student_Branch varchar(20),
Year number(20),
Grades varchar(20), 
Mobile_Number char (20),
City_Name varchar(20),
Date_of_Birth date 
);

desc Student

drop table Student 

insert into Student(Student_Id, Student_Name, Student_Branch, Year, Grades, Mobile_Number, City_Name, Date_of_Birth) values(26390, 'Satyam Tripathi', 'CS', 2021, '8.8 CGPA', '8528095908', 'Mahoba(U.P.)', '07/24/2000')

select sysdate from dual;
