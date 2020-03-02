import mysql.connector
import time

def convert_time(time_):
	return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time_))

def get_name_threads():
	list_threads=[]
	cnx = mysql.connector.connect(user='myforum', password='****', host='192.168.158.206', database='myforum')
	cursor = cnx.cursor()
	cursor.execute("SELECT id,usr,sbj,time_create FROM threads")
	for (id, usr,sbj,time_create) in cursor:
		list_threads.append((id,usr,sbj,convert_time(int(time_create))))
	cnx.commit()
	cursor.close()
	cnx.close()
	return list_threads

def read_cmt(thread_id):
	list_cmts=[]
	cnx = mysql.connector.connect(user='myforum', password='****', host='192.168.158.206', database='myforum')
	cursor = cnx.cursor()
	cursor.execute("SELECT cmt_id,usr,cmt,time_create FROM comments WHERE thread_id=%s" %thread_id)
	for (cmt_id, usr,cmt,time_create) in cursor:
		list_cmts.append(( usr,cmt,convert_time(int(time_create))))
	cnx.commit()
	cursor.close()
	cnx.close()
	return list_cmts

def write_cmt(thread_id,usr,cmt):
	time_now = int(time.time())
	cnx = mysql.connector.connect(user='myforum', password='****', host='192.168.158.206', database='myforum')
	cursor = cnx.cursor()

	cursor.execute("INSERT INTO comments (cmt,usr,time_create,thread_id) VALUES ('%s','%s','%s','%s')"%(cmt, usr, time_now, thread_id))
	cmt_id = cursor.lastrowid
	cnx.commit()
	cursor.close()
	cnx.close()

def get_thread(id):
	cnx = mysql.connector.connect(user='myforum', password='****', host='192.168.158.206', database='myforum')
	cursor = cnx.cursor()
	cursor.execute("SELECT usr,sbj,msg,time_create FROM threads WHERE id='%s'" %id)
	result = cursor.fetchone()
	cnx.commit()
	cursor.close()
	cnx.close()
	return result

def write_new(usr, sbj, msg):
	time_now = int(time.time())
	cnx = mysql.connector.connect(user='myforum', password='****',host='192.168.158.206',database='myforum')
	cursor = cnx.cursor()
	add_new_thread=("INSERT INTO threads (usr,sbj,msg,time_create) VALUES (%s,%s,%s,%s)")
	cursor.execute(add_new_thread, (usr, sbj, msg, time_now))
	id = cursor.lastrowid
	cnx.commit()
	cursor.close()
	cnx.close()

def live_chat_send(usr, chat_ct):
	cnx = mysql.connector.connect(user='myforum', password='****', host='192.168.158.206', database='myforum')
	cursor = cnx.cursor()
	add_new_chat = ("INSERT INTO livechat (usr, chat) VALUES (%s,%s)")
	cursor.execute(add_new_chat, (usr, chat_ct))
	chat_id = cursor.lastrowid
	cnx.commit()
	cursor.close()
	cnx.close()

def create_user(usr,passwd):
	cnx = mysql.connector.connect(user='myforum', password='****',host='192.168.158.206',database='myforum')
	cursor = cnx.cursor()
	add_user=("INSERT INTO users (user,passwd) VALUES (%s,%s)")
	cursor.execute(add_user, (usr,passwd))
	usr_id = cursor.lastrowid
	cnx.commit()
	cursor.close()
	cnx.close()

def get_chat():
	list_chat=[]
	cnx = mysql.connector.connect(user='myforum', password='****', host='192.168.158.206', database='myforum')
	cursor = cnx.cursor()
	cursor.execute("SELECT usr,chat FROM (SELECT * FROM livechat ORDER BY chat_id DESC LIMIT 50) sub ORDER BY chat_id ASC")
	for (usr,chat) in cursor:
		list_chat.append((usr,chat))
	cnx.commit()
	cursor.close()
	cnx.close()
	return list_chat

def check_login(usr,passwd):
	try:
		cnx = mysql.connector.connect(user='myforum', password='****', host='192.168.158.206', database='myforum')
		cursor = cnx.cursor()
		cursor.execute("SELECT user FROM users WHERE user='%s' AND passwd='%s'" % (usr, passwd))
		result= cursor.fetchone()[0]
		cnx.commit()
		cursor.close()
		cnx.close()
		return True
	except:
		return False

def check_username_existing(usr):
	try:
		cnx = mysql.connector.connect(user='myforum', password='****', host='192.168.158.206', database='myforum')
		cursor = cnx.cursor()
		cursor.execute("SELECT user FROM users WHERE user='%s'"%usr)
		cursor.fetchone()[0]
		cnx.commit()
		cursor.close()
		cnx.close()
		return True
	except:
		return False

if __name__ == '__main__':
	#create_user('admin','admin')
	#print check_login('hoang','hoang')
	#print get_thread(1)
	print time.time()
	#print convert_time(time.time())
