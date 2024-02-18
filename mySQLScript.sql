create
database questionBank;
show
databases;
create table questionBank.questions
(
    id          int primary key auto_increment,
    subjectName varchar(255),
    question    varchar(255),
    answer      varchar(255),
    chapterName varchar(255)
);

