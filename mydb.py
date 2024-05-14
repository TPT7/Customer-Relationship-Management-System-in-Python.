import psycopg2
import psycopg2.extras

def connect_to_postgres():
    try:
        global conn
        conn = psycopg2.connect(host='localhost', database='crmdb', user='tpt', password='admin')
        
        conn.autocommit = True
        print('Successfully connected to database')
        
    except Exception as err:
        if err:
            print('Error connecting to database', err)
        
connect_to_postgres()




