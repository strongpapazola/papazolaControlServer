# papazolaControlServer
you can control server service or firewall(iptables rule) and can reboot your server

- Tested : ubuntu 18-04,16-04 !

- Step by step :
1. create user 'infra' and path /home/infra (sudo permision active)
2. extract papazolaControl.zip and move to /var/www (web base)
3. change /var/www/papazolaControl/application/config/config.php (SET URL from localhost)
4. change /var/www/papazolaControl/application/config/database.php (SET Auth Mysql)
5. change /var/www/papazolaControl/application/view/create.php (SET URL from localhost)
6. import database papazolaControl.sql
7. mkdir /home/infra/papazolaControlApps and mv papazolaControl.* to there
8. change path on papazolaControl.sh to papazolaControl.py
9. change auth mysql on papazolaControl.py
10. do 'apt install python3 python3-pip -y && python3 -m pip install mysql-connector'
