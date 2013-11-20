CREATE TABLE Tasks (
    Task_ID INT(11) NOT NULL AUTO_INCREMENT,
	User_ID INT(11) NOT NULL ,
    Task_DateAdded DATE NULL ,
    Task_DateDue DATE NULL ,
    Task_Subject VARCHAR(255) NULL ,
    PRIMARY KEY (Task_ID)
) ENGINE=InnoDB charset=utf8