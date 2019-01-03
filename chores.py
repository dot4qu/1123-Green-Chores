import sqlite3
from datetime import datetime, timedelta
from sqlite3 import Error
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from pdb import set_trace as bp

db = '/home/pi/1123-Green-Chores/chores.db'
chores_table = "Chores"
people_table = "People"
name_column = "Name"
email_column = 'Email'
choreid_column = "ChoreID"
id_column = "ID"
from_addr = '1123greenchores@gmail.com'
email_pass = os.environ['CHORES_PW']

def rotate_chores(person_choreid_tuples):
	length = len(person_choreid_tuples)

	for i in range(length):
		new_tuple = (person_choreid_tuples[i][0], (person_choreid_tuples[i][1] % length) + 1)
		person_choreid_tuples[i] = new_tuple

	return person_choreid_tuples

def get_responsibility_names(connection):
	cursor = connection.cursor()
	cursor.execute('SELECT {0}.{1}, {2}.{3} FROM {4} JOIN {5} on {6}={7}.{8};'\
	.format(people_table, name_column, chores_table, name_column, people_table, chores_table, choreid_column, chores_table, id_column))
	return cursor.fetchall();

def get_responsibility_ids(connection):
	cursor = connection.cursor()
	cursor.execute('SELECT {0}.{1}, {2}.{3} FROM {4} JOIN {5} on {6}={7}.{8};'\
		.format(people_table, name_column, chores_table, id_column,  people_table, chores_table, choreid_column, chores_table, id_column))
	return cursor.fetchall()

def update_responsibilities(connection, person_choreid_tuples):
	cursor = connection.cursor()
	new_chore_str = ''
	# update_string = 'UPDATE {0} SET {1}=(SELECT {2} FROM {3} WHERE {4}.{5}=\'{6}\') WHERE {7}=\'{8}\''
	update_string = 'UPDATE {0} SET {1}={2} WHERE {3}=\'{4}\''

	print('\n')
	for pair in person_choreid_tuples:
		print('Executing query: {0}'\
			.format(update_string\
				.format(people_table, choreid_column, pair[1], name_column, pair[0])))

		cursor.execute(update_string\
			.format(people_table, choreid_column, pair[1], name_column, pair[0]))

	print('\n')
	connection.commit()

def prettyprint_responsibilities(opening_string, person_chore_tuples):
	output_str = '{0}\n\n'.format(opening_string)
	print('{0}'.format(opening_string))
	for i in range(len(person_chore_tuples)):
		output_str = output_str + '{0} --- {1}\n'\
			.format(person_chore_tuples[i][0], person_chore_tuples[i][1]);

		print ('{0} --- {1}'\
			.format(person_chore_tuples[i][0], person_chore_tuples[i][1]))

	return output_str

if __name__ == '__main__':
	now = datetime.now()

	connection = sqlite3.connect(db)

	# need person/chorename dict for logging and email, need person/choreid for accurate chore rotation
	person_chore_tuples = get_responsibility_names(connection)
	person_choreid_tuples = get_responsibility_ids(connection)

	smtp = SMTP('smtp.gmail.com', 587)
	smtp.ehlo()
	smtp.starttls()
	smtp.ehlo()
	smtp.login(from_addr, email_pass)
	
	prettyprint_responsibilities('Last week\'s chores!', person_chore_tuples)

	# rotate simply mod the incremented tuple values within list
	person_choreid_tuples = rotate_chores(person_choreid_tuples)

	# update and commit all new chore ids for each person
	update_responsibilities(connection, person_choreid_tuples)

	# requery newly updated rows to get new chores
	person_chore_tuples = get_responsibility_names(connection)

	chores_str = prettyprint_responsibilities('This week\'s chores!', person_chore_tuples)

	email_sql = 'SELECT {0} FROM {1};'
	email_tuple_list = connection.cursor().execute(email_sql.format(email_column, people_table)).fetchall()
	email_list = [pair[0] for pair in email_tuple_list]

	# build multipart mimetype with data and sends it
	comma_char = ','
	message = MIMEMultipart()
	message['From'] = from_addr
	message['To'] = comma_char.join(pair[0] for pair in email_tuple_list)
	message['Subject'] = 'Chores for the upcoming week: {0} through {1}'\
		.format(now.strftime('%m/%d'), (now + timedelta(days=7)).strftime('%m/%d'))
	message.attach(MIMEText(chores_str))

	smtp.sendmail(from_addr,\
		email_list,\
		str(message))
	smtp.quit()






