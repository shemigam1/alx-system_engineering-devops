-- create user
CREATE USER IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO 'replica_user'@'%';
GRANT SELECT ON `mysql`.`user` TO 'holberton_user'@'localhost';
