CREATE TABLE employee (
`no` int(11) NOT NULL AUTO_INCREMENT,
`emp_id` CHAR(6) NOT NULL,
`name` VARCHAR(10) NOT NULL,
`gender` CHAR(1) NOT NULL,
`birthday` DATE NOT NULL,
`salary` INT,
PRIMARY KEY (`no`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;


INSERT INTO employee VALUES ('1','E00001', '山田太郎', '男', '1995-01-01', 190000);
INSERT INTO employee VALUES ('2','E00002', '佐藤次郎', '男', '1990-05-03', 250000);
INSERT INTO employee VALUES ('3','E00003', '鈴木花子', '女', '1990-02-11', 250000);
INSERT INTO employee VALUES ('4','E00004', '田中三郎', '男', '1975-11-03', 400000);
INSERT INTO employee VALUES ('5','E00005', '高橋良子', '女', '1985-11-23', 300000);
INSERT INTO employee VALUES ('6','E00006', '鈴木良枝', '女', '1970-05-03', 450000);
INSERT INTO employee VALUES ('7','E00007', '佐藤健次', '男', '1980-05-05', 350000);

