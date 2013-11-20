CREATE TABLE User (
    User_ID INT(11) NOT NULL AUTO_INCREMENT,
    User_Fname VARCHAR(255) NULL ,
    User_Lname VARCHAR(255) NULL ,
    User_Username VARCHAR(255) NULL ,
    User_Password VARCHAR(255) NULL ,
    User_Email VARCHAR(255) NULL ,
    PRIMARY KEY (User_ID)
) ENGINE=InnoDB charset=utf8
