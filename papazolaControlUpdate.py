from os import system as sy
import sys

def banner():
 print('Usage : python3 <this_script> [--install/--remove]')

def remove():
 sy('rm -r /opt/papazola*')
 sy('rm -r /var/www/papazola*')
 sy("mysql -u root -p -e 'drop database papazolaControl;'")

def install():
 nameapps = 'papazolaControlServer'
 scapps = 'papazolaControlServerApps'

 sy('clear')
 print('Script Must Run Root')
 input('[Enter]')
 sy('clear')
 print('Go to main directory by type : [cd ~/]')
 input('[Enter]')
 sy('clear')

 print('Installing Python And Package')
 input('[Enter]')
 sy('apt install python3 python3-pip git -y')
 sy('python3 -m pip install mysql-connector requests')
 input('[Enter]')
 sy('clear')
 
 print('System Update Launch...!!!')
 sy('sleep 1')
 sy('git clone https://github.com/strongpapazola/'+nameapps)
 sy('mv '+nameapps+' /opt/')
 input('[Enter]')
 sy('clear')
 
 print('Copy The sh & py File Trigger...!!!')
 sy('sleep 1')
 sy('mkdir -p /opt/'+scapps)
 sy('mv /opt/'+nameapps+'/papazolaControl.py /opt/'+scapps)
 sy('mv /opt/'+nameapps+'/papazolaControl.sql /opt/'+scapps)
 input('[Enter]')
 sy('clear')
 
 pathweb = input('Input Path Web [ex: "/var/www/"] : ')
 print('Moving Dir To ['+pathweb+']...!!!')
 sy('sleep 1')
 sy('rm -r '+pathweb+'papazolaControlServer')
 sy('unzip /opt/'+nameapps+'/papazolaControl.zip')
 sy('mv papazolaControl '+pathweb+nameapps)
 sy('rm -r /opt/'+nameapps)
 input('[Enter]')
 sy('clear')
 
 print('Set Password Your SQL on (PHP and Python)...!!!')
 input('[Enter]')
 sy('clear')
 sy("nano "+pathweb+nameapps+"/application/config/database.php")
 sy('nano /opt/'+scapps+'/papazolaControl.py')
 input('[Enter]')
 sy('clear')
 
 print('Change URL On Config ...!')
 input('[Enter]')
 sy('clear')
 sy("nano "+pathweb+nameapps+"/application/config/config.php")
 input('[Enter]')
 sy('clear')
 
 a = '''
 Input This Script like this :
 ==================
 #!/bin/bash
 /opt/papazolaControlServerApps/papazolaControl.sh
 exit 0
 ==================
 on /etc/rc.local
 '''
 print(a)
 input('[Enter]')
 sy('echo "watch --interval 60 python3 /opt/'+scapps+'/papazolaControl.py &> /dev/null &" > /opt/'+scapps+'/papazolaControl.sh')
 sy('chmod +x /opt/'+scapps+'/papazolaControl.sh')
 sy('nano /etc/rc.local')
 sy('chmod +x /etc/rc.local')
 input('[Enter]')
 sy('clear')
 
 print('Import Database "mysql -u root -p"')
 input('[Enter]')
 sy("mysql -u root -p -e 'CREATE DATABASE papazolaControl;'")
 input('[Enter]')
 sy('clear')
 
 def importdb():
  importdb = input('import Database papazolaControl ?? [y/n]')
  if importdb == 'y':
   sy('mysql -u root -p papazolaControl < /opt/'+scapps+'/papazolaControl.sql')
  else:
   importdb()
 
 importdb()
 
 print('open url "{url_your_server}/'+nameapps+'"')

try:
 if sys.argv[1] == '--install':
  install()
 elif sys.argv[1] == '--remove':
  remove()
 else:
  banner()
except:
 banner()


