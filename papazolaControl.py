import requests
from os import system
import subprocess
import mysql.connector

# Variable Area
domain = str(subprocess.Popen("hostname", shell=True,
                              stdout=subprocess.PIPE).stdout.read())

# Function Area
def mailservice(x):
    print(x)

# Database Function
try:
    db = mysql.connector.connect(
        host='localhost',
        user='root',
    	  passwd='your_password',
        database='papazolaControl'
    )
    cursor = db.cursor()
except Exception as e:
    mailservice(str(e))


def getall_datatable(table):
    sql = 'SELECT * FROM '+table
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def search_datatable(table, col, search):
    sql = 'SELECT * FROM '+table+' WHERE '+col+"='"+search+"'"
    cursor.execute(sql)
    result = cursor.fetchone()
    return result


def update_row(sql, val):
    try:
        cursor.execute(sql, val)
        db.commit()
    except Exception as e:
        mailservice(str(e))


# Get And Input to variable
portssh = str(search_datatable('info', 'type', 'PortSSH')[2])
master = str(search_datatable('info', 'type', 'Master')[2])

# Program Function
def launch():
    # reboot
    reboot_val = str(search_datatable('info', 'type', 'reboot')[2])
    if reboot_val == '2':
        sql = "UPDATE info SET value=%s WHERE type=%s"
        val = ('1', 'reboot')
        update_row(sql, val)
        system('reboot')

    # icmp
    icmp_val = str(search_datatable('network_rule', 'name', 'icmp')[2])
    icmp_exec = str(search_datatable('network_rule', 'name', 'icmp')[3])
    if icmp_val == '2':
        if icmp_exec == '1':
            sql = "UPDATE network_rule SET `execute_val`=%s WHERE `name`=%s"
            val = ("2", "icmp")
            update_row(sql, val)
            system("iptables -A INPUT -p icmp --source "+master+" -j ACCEPT")
            system("iptables -A INPUT -p icmp -j DROP")
    elif icmp_val == '1':
        if icmp_exec == '1':
            sql = "UPDATE network_rule SET `execute_val`=%s WHERE name=%s"
            val = ('2', 'icmp')
            update_row(sql, val)
            system("iptables -D INPUT -p icmp --source "+master+" -j ACCEPT")
            system("iptables -D INPUT -p icmp -j DROP")

    # ssh
    ssh_val = str(search_datatable('network_rule', 'name', 'ssh')[2])
    ssh_exec = str(search_datatable('network_rule', 'name', 'ssh')[3])
    if ssh_val == '2':
        if ssh_exec == '1':
            sql = "UPDATE network_rule SET execute_val=%s WHERE name=%s"
            val = ('2', 'ssh')
            update_row(sql, val)
            system("iptables -A INPUT -p tcp --dport " +portssh+" --source "+master+" -j ACCEPT")
            system("iptables -A INPUT -p tcp --dport "+portssh+" -j DROP")
    elif ssh_val == '1':
        if ssh_exec == '1':
            sql = "UPDATE network_rule SET execute_val=%s WHERE name=%s"
            val = ('2', 'ssh')
            update_row(sql, val)
            system("iptables -D INPUT -p tcp --dport " +portssh+" --source "+master+" -j ACCEPT")
            system("iptables -D INPUT -p tcp --dport "+portssh+" -j DROP")

    # Service
    # ssh
    ssh_svc = str(search_datatable('services', 'name', 'ssh')[2])
    ssh_x = str(search_datatable('services', 'name', 'ssh')[3])
    if ssh_svc == '1':
        if ssh_x == '1':
            system('service ssh stop')
            status = subprocess.Popen('service ssh status | grep Active:', shell=True, stdout=subprocess.PIPE).stdout.read()
            sql = "UPDATE services SET `execute`=%s,`information`=%s WHERE `name`=%s"
            val = ('2',str(status),'ssh')
            update_row(sql, val)
    if ssh_svc == '2':
        if ssh_x == '1':
            system('service ssh start')
            status = subprocess.Popen('service ssh status | grep Active:', shell=True, stdout=subprocess.PIPE).stdout.read()
            sql = "UPDATE services SET `execute`=%s,`information`=%s WHERE `name`=%s"
            val = ('2',str(status),'ssh')
            update_row(sql, val)

    # portsentry
    portsentry_svc = str(search_datatable('services', 'name', 'portsentry')[2])
    portsentry_x = str(search_datatable('services', 'name', 'portsentry')[3])
    if portsentry_svc == '1':
        if portsentry_x == '1':
            system('service portsentry stop')
            status = subprocess.Popen('service portsentry status | grep Active:', shell=True, stdout=subprocess.PIPE).stdout.read()
            sql = "UPDATE services SET `execute`=%s,`information`=%s WHERE `name`=%s"
            val = ('2',str(status),'portsentry')
            update_row(sql, val)
    if portsentry_svc == '2':
        if portsentry_x == '1':
            system('service portsentry start')
            status = subprocess.Popen('service portsentry status | grep Active:', shell=True, stdout=subprocess.PIPE).stdout.read()
            sql = "UPDATE services SET `execute`=%s,`information`=%s WHERE `name`=%s"
            val = ('2',str(status),'portsentry')
            update_row(sql, val)
'''
    # apache
    apache_svc = str(search_datatable('services', 'name', 'apache')[2])
    apache_x = str(search_datatable('services', 'name', 'apache')[3])
    if apache_svc == '1':
        if apache_x == '1':
            system('service apache2 stop')
            status = subprocess.Popen('service apache2 status | grep Active:', shell=True, stdout=subprocess.PIPE).stdout.read()
            sql = "UPDATE services SET `execute`=%s,`information`=%s WHERE `name`=%s"
            val = ('2',str(status),'apache')
            update_row(sql, val)
    if apache_svc == '2':
        if apache_x == '1':
            system('service apache2 start')
            status = subprocess.Popen('service apache2 status | grep Active:', shell=True, stdout=subprocess.PIPE).stdout.read()
            sql = "UPDATE services SET `execute`=%s,`information`=%s WHERE `name`=%s"
            val = ('2',str(status),'apache')
            update_row(sql, val)

    # mysql
    mysql_svc = str(search_datatable('services', 'name', 'mysql')[2])
    mysql_x = str(search_datatable('services', 'name', 'mysql')[3])
    if mysql_svc == '1':
        if mysql_x == '1':
            system('service mysql stop')
            status = subprocess.Popen('service mysql status | grep Active:', shell=True, stdout=subprocess.PIPE).stdout.read()
            sql = "UPDATE services SET `execute`=%s,`information`=%s WHERE `name`=%s"
            val = ('2',str(status),'mysql')
            update_row(sql, val)
    if mysql_svc == '2':
        if mysql_x == '1':
            system('service mysql start')
            status = subprocess.Popen('service mysql status | grep Active:', shell=True, stdout=subprocess.PIPE).stdout.read()
            sql = "UPDATE services SET `execute`=%s,`information`=%s WHERE `name`=%s"
            val = ('2',str(status),'mysql')
            update_row(sql, val)
'''
# Start Action
try:
    launch()
except Exception as e:
    mailservice(str(e))
