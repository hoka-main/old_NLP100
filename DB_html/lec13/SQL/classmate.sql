SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";

CREATE TABLE `classmate` (
  `no` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `age` int(3) NOT NULL,
  PRIMARY KEY (`no`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;

insert into classmate(no,name,age)values(1,"正広","10");
insert into classmate(no,name,age)values(2,"拓也","10");
insert into classmate(no,name,age)values(3,"吾郎","9");
insert into classmate(no,name,age)values(4,"慎吾","7");
insert into classmate(no,name,age)values(5,"剛","9");

