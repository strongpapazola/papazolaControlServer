from os import system as sy
import sys

def banner():
 print('Usage : python3 '+str(sys.argv[0])+' [--install/--remove]')

def checksql():
 pass_sql = input('Input Password Root SQL : ')
 import mysql.connector
 try:
  db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=str(pass_sql),
  )
  if db.is_connected():
   print("Berhasil terhubung ke database")
  return pass_sql
 except:
  print("Gagal terhubung ke database")
  sys.exit()

def remove():
 pass_sql = checksql()
 inp = input('Input Path Web [ex: "/var/www/"] : ')
 if not inp:
  inp = '/var/www/'

 sy('rm -r /opt/papazolaControlServerApps')
 sy('rm -r %spapazolaControlServer' % (inp,))
 sy("mysql -u root -p%s -e 'drop database papazolaControl;'" % (pass_sql,))

 import subprocess
 a = subprocess.Popen('ps aux | grep /opt/papazolaControlServerApps/', shell=True, stdout=subprocess.PIPE).stdout
 a = str(a.read())
 a = a.split("'")
 a = a[1]
 a = a.split(' ')
 b = []
 for c in a:
  if c:
   b.append(c)
 b = b[1]
 print('killing PID : '+str(b))
 sy('kill -9 '+str(b))



def install():
 nameapps = 'papazolaControlServer'
 scapps = 'papazolaControlServerApps'

 sy('clear')
 print('Script Must Run Root')
 input('[Enter]')
 sy('clear')
 print('Script Required apache2 & mysql/mariadb Installed')
 input('[Enter]')
 sy('clear')

 pass_sql = checksql()
 pathweb = input('Input Path Web [ex: "/var/www/"] : ')
 urlweb = input('Input URL method [ex: "http"] : ')
 namesvr = input('Input Domain Server [ex: "localhost"] : ')
 portssh = input('Input port ssh server [ex: "22"] : ')
 if not pathweb:
  pathweb = '/var/www/'
 if not portssh:
  portssh = '22'
 if not urlweb:
  urlweb = 'http'
 if not namesvr:
  namesvr = 'localhost'

 def update_row(sql, val):
  try:
   cursor.execute(sql, val)
   db.commit()
  except Exception as e:
   print(str(e))

 print('Installing Python And Package')
 sy('sleep 1')
 sy('apt install apache2 python3 python3-pip git -y')
 sy('python3 -m pip install mysql-connector requests')

 print('System Update Launch...!!!')
 sy('sleep 1')
 sy('rm -r %s' % (nameapps,))
 sy('git clone https://github.com/strongpapazola/%s' % (nameapps,))
 sy('mv %s /opt/' % (nameapps,))

 print('Copy The sh & py File Trigger...!!!')
 sy('sleep 1')
 sy('mkdir -p /opt/%s' % (scapps,))
 sy('mv /opt/%s/papazolaControl.py /opt/%s' % (nameapps,scapps,))
 sy('mv /opt/%s/papazolaControl.sql /opt/%s' % (nameapps,scapps,))

 print('Moving Dir To [%s]...!!!' % (pathweb,))
 sy('sleep 1')
 sy('rm -r '+pathweb+'papazolaControlServer')
 sy('unzip /opt/'+nameapps+'/papazolaControl.zip')
 sy('mv papazolaControl '+pathweb+nameapps)
 sy('rm -r /opt/'+nameapps)

 print('Set Password Your SQL on (PHP and Python)...!!!')
 sy('sleep 1')
 sy("sed -i 's/your_password/"+pass_sql+"/g' "+pathweb+nameapps+"/application/config/database.php")
 sy("sed -i 's/your_password/"+pass_sql+"/g' /opt/"+scapps+'/papazolaControl.py')

 print('Change URL On Config ...!')
 sy('sleep 1')
 sy("sed -i \"26c\$config['base_url'] = '"+urlweb+"://"+namesvr+"/papazolaControlServer';\" "+pathweb+nameapps+"/application/config/config.php")

 a = '''

Copy This Script :
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

 print('Import Database "mysql -u root -p"')
 sy('sleep 1')
 sy("mysql -u root -p%s -e 'CREATE DATABASE papazolaControl;'" % (pass_sql,))
 sy('mysql -u root -p%s papazolaControl < /opt/%s/papazolaControl.sql' % (pass_sql,scapps,))

 import mysql.connector
 db = mysql.connector.connect(
   host="localhost",
   user="root",
   passwd=str(pass_sql),
   database="papazolaControl"
 )
 cursor = db.cursor()

 sql = "UPDATE info SET value=%s WHERE type=%s"
 val = (str(namesvr), 'Name')
 update_row(sql, val)
 val = (str(portssh), 'PortSSH')
 update_row(sql, val)

 print('==============================================================')
 print('For check value on database for execute command...!')
 print('please run : "/opt/papazolaControlServerApps/papazolaControl.sh"')
 print('==============================================================')
 print('Add Another user : open url "'+urlweb+'://'+namesvr+'/'+nameapps+'/index.php/auth/register/aiypwzqp040902"')
 print('open url "'+urlweb+'://'+namesvr+'/'+nameapps+'/", User : admin, Pass : admin')

try:
 if sys.argv[1] == '--install':
  install()
 elif sys.argv[1] == '--remove':
  remove()
 else:
  banner()
except:
 banner()


