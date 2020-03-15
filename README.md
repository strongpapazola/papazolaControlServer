# papazolaControlServer
you can control server service or firewall(iptables rule) and can reboot your server

- Tested : ubuntu 18-04,16-04 !

- Step by step :
create user 'infra' and path /home/infra (sudo permision active)
extract papazolaControl.zip and move to /var/www (web base)
change /var/www/papazolaControl/application/config/config.php (SET URL from localhost)
change /var/www/papazolaControl/application/config/database.php (SET Auth Mysql)
change /var/www/papazolaControl/application/view/create.php (SET URL from localhost)
import database papazolaControl.sql
mkdir /home/infra/papazolaControlApps and mv papazolaControl.* to there
change path on papazolaControl.sh to papazolaControl.py
change auth mysql on papazolaControl.py
do 'apt install python3 python3-pip -y && python3 -m pip install mysql-connector'
