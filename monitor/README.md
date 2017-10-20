### MySQL config

```
mysql> CREATE SCHEMA `lgb_access` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
mysql> CREATE USER 'lgbaccess'@'localhost' IDENTIFIED BY 'lgbaccess';
mysql> GRANT ALL PRIVILEGES ON lgb_access.* TO 'lgbaccess'@'localhost' WITH GRANT OPTION;
```
