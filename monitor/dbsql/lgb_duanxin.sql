CREATE SCHEMA `lgbaccess` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
CREATE USER 'lgbaccess'@'localhost' IDENTIFIED BY 'lgbaccess';
GRANT ALL PRIVILEGES ON lgb_access.* TO 'lgbaccess'@'localhost' WITH GRANT OPTION;

use lgb_access;

CREATE TABLE `lgb_access`.`information` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `statusCode` INT NOT NULL,
  `statusInformation` VARCHAR(20) NOT NULL,
  `nowTime` TIMESTAMP NOT NULL,
  PRIMARY KEY (`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `lgb_access`.`config` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `running` INT NOT NULL COMMENT '是否运行\n0：否\n1：是',
  PRIMARY KEY (`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT = '配置表';

INSERT INTO `lgb_access`.`config` (`running`) VALUES ('1');
