import mysql.connector
import glob
import json
import csv
from io import StringIO
import itertools
import hashlib
import os
import cryptography
from cryptography.fernet import Fernet
from math import pow
import datetime

class database:

    def __init__(self, purge = False):

        # Grab information from the configuration file
        self.database       = 'db'
        self.host           = '127.0.0.1'
        self.user           = 'master'
        self.port           = 3306
        self.password       = 'master'
        self.tables         = ['institutions', 'positions', 'experiences', 'skills','feedback', 'users']
        
        self.encryption     =  {   'oneway': {'salt' : b'averysaltysailortookalongwalkoffashortbridge',
                                                 'n' : int(pow(2,5)),
                                                 'r' : 9,
                                                 'p' : 1
                                             },
                                'reversible': { 'key' : '7pK_fnSKIjZKuv_Gwc--sZEMKn2zc8VvD6zS96XcNHE='}
                                }
        #-----------------------------------------------------------------------------

    def query(self, query = "SELECT * FROM users", parameters = None):

        cnx = mysql.connector.connect(host     = self.host,
                                      user     = self.user,
                                      password = self.password,
                                      port     = self.port,
                                      database = self.database,
                                      charset  = 'latin1'
                                     )


        if parameters is not None:
            cur = cnx.cursor(dictionary=True)
            cur.execute(query, parameters)
        else:
            cur = cnx.cursor(dictionary=True)
            cur.execute(query)

        # Fetch one result
        row = cur.fetchall()
        cnx.commit()

        if "INSERT" in query:
            cur.execute("SELECT LAST_INSERT_ID()")
            row = cur.fetchall()
            cnx.commit()
        cur.close()
        cnx.close()
        return row

    def createTables(self, purge=False, data_path = 'back_end_flask/database/'):
        ''' FILL ME IN WITH CODE THAT CREATES YOUR DATABASE TABLES.'''

        #should be in order or creation - this matters if you are using forign keys.
         
        if purge:
            for table in self.tables[::-1]:
                self.query(f"""DROP TABLE IF EXISTS {table}""")
            
        # Execute all SQL queries in the /database/create_tables directory.
        for table in self.tables:
            
            #Create each table using the .sql file in /database/create_tables directory.
            with open(data_path + f"create_tables/{table}.sql") as read_file:
                create_statement = read_file.read()
            self.query(create_statement)

            # Import the initial data
            try:
                params = []
                with open(data_path + f"initial_data/{table}.csv") as read_file:
                    scsv = read_file.read()            
                for row in csv.reader(StringIO(scsv), delimiter=','):
                    params.append(row)
            
                # Insert the data
                cols = params[0]; params = params[1:] 
                self.insertRows(table = table,  columns = cols, parameters = params)

            #no initial data to insert - i.e. users and feedback
            except:
                
                pass

    def insertRows(self, table='table', columns=['x','y'], parameters=[['v11','v12'],['v21','v22']]):
        
        # Check if there are multiple rows present in the parameters
        has_multiple_rows = any(isinstance(el, list) for el in parameters)
        keys, values      = ','.join(columns), ','.join(['%s' for x in columns])
        
        # Construct the query we will execute to insert the row(s)
        query = f"""INSERT IGNORE INTO {table} ({keys}) VALUES """
        if has_multiple_rows:
            for p in parameters:
                query += f"""({values}),"""
            query     = query[:-1] 
            parameters = list(itertools.chain(*parameters))
        else:
            query += f"""({values}) """                      
        
        insert_id = self.query(query,parameters)[0]['LAST_INSERT_ID()']         
        return insert_id

    def about(self, nested=False):    
        query = """select concat(col.table_schema, '.', col.table_name) as 'table',
                          col.column_name                               as column_name,
                          col.column_key                                as is_key,
                          col.column_comment                            as column_comment,
                          kcu.referenced_column_name                    as fk_column_name,
                          kcu.referenced_table_name                     as fk_table_name
                    from information_schema.columns col
                    join information_schema.tables tab on col.table_schema = tab.table_schema and col.table_name = tab.table_name
                    left join information_schema.key_column_usage kcu on col.table_schema = kcu.table_schema
                                                                     and col.table_name = kcu.table_name
                                                                     and col.column_name = kcu.column_name
                                                                     and kcu.referenced_table_schema is not null
                    where col.table_schema not in('information_schema','sys', 'mysql', 'performance_schema')
                                              and tab.table_type = 'BASE TABLE'
                    order by col.table_schema, col.table_name, col.ordinal_position;"""
        results = self.query(query)
        if nested == False:
            return results

        table_info = {}
        for row in results:
            table_info[row['table']] = {} if table_info.get(row['table']) is None else table_info[row['table']]
            table_info[row['table']][row['column_name']] = {} if table_info.get(row['table']).get(row['column_name']) is None else table_info[row['table']][row['column_name']]
            table_info[row['table']][row['column_name']]['column_comment']     = row['column_comment']
            table_info[row['table']][row['column_name']]['fk_column_name']     = row['fk_column_name']
            table_info[row['table']][row['column_name']]['fk_table_name']      = row['fk_table_name']
            table_info[row['table']][row['column_name']]['is_key']             = row['is_key']
            table_info[row['table']][row['column_name']]['table']              = row['table']
        return table_info

    def createTables(self, purge=False, data_path = 'back_end_flask/database/'):
        ''' FILL ME IN WITH CODE THAT CREATES YOUR DATABASE TABLES.'''

        #should be in order or creation - this matters if you are using forign keys.
         
        if purge:
            for table in self.tables[::-1]:
                self.query(f"""DROP TABLE IF EXISTS {table}""")
            
        # Execute all SQL queries in the /database/create_tables directory.
        for table in self.tables:
            
            #Create each table using the .sql file in /database/create_tables directory.
            with open(data_path + f"create_tables/{table}.sql") as read_file:
                create_statement = read_file.read()
            self.query(create_statement)

            # Import the initial data
            try:
                params = []
                with open(data_path + f"initial_data/{table}.csv") as read_file:
                    scsv = read_file.read()            
                for row in csv.reader(StringIO(scsv), delimiter=','):
                    params.append(row)
            
                # Insert the data
                cols = params[0]; params = params[1:] 
                self.insertRows(table = table,  columns = cols, parameters = params)

            #no initial data to insert - i.e. users and feedback
            except:
                
                pass

    def insertRows(self, table='table', columns=['x','y'], parameters=[['v11','v12'],['v21','v22']]):
        
        # Check if there are multiple rows present in the parameters
        has_multiple_rows = any(isinstance(el, list) for el in parameters)
        keys, values      = ','.join(columns), ','.join(['%s' for x in columns])
        
        # Construct the query we will execute to insert the row(s)
        query = f"""INSERT IGNORE INTO {table} ({keys}) VALUES """
        if has_multiple_rows:
            for p in parameters:
                query += f"""({values}),"""
            query     = query[:-1] 
            parameters = list(itertools.chain(*parameters))
        else:
            query += f"""({values}) """                      
        
        insert_id = self.query(query,parameters)[0]['LAST_INSERT_ID()']         
        return insert_id

    

    # def createTables(self, purge=False, data_path = 'back_end_flask/database/'):
    #     '''
    #     Obtain our table creation statements from our sql files, directly use them to create the tables in the database
    #     if they do not exist.

    #     TODO: Implement Purge feature

    #     @param purge: Whether if we wish to wipe the database
    #     @param data_path: The data path to our sql tables

    #     '''

    #     with open(data_path + 'create_tables/institutions.sql', 'r') as afile:
    #         institutions_statement = afile.read()
    #         self.query(institutions_statement)

    #     with open(data_path + 'create_tables/positions.sql', 'r') as bfile:
    #         positions_statement = bfile.read()
    #         self.query(positions_statement)       

    #     with open(data_path + 'create_tables/experiences.sql', 'r') as cfile:
    #         experience_statement = cfile.read()
    #         self.query(experience_statement)


    #     with open(data_path + 'create_tables/skills.sql', 'r') as dfile:
    #         skills_statement = dfile.read()
    #         self.query(skills_statement)


    #     with open(data_path + 'create_tables/feedback.sql', 'r') as efile:
    #         feedback_statement = efile.read()
    #         self.query(feedback_statement)


    #     #Start inserting rows into the table with the helper funtion
    #     with open(data_path + "initial_data/institutions.csv") as institution_file:

    #         #Read the information from the csv
    #         information_reader = csv.reader(institution_file)
    #         #Extract the header and skip it
    #         header = next(information_reader)

    #         rows = []
    #         for row in information_reader:

    #             for elem in range(len(row)):

    #                 if row[elem] == "NULL":
    #                     row[elem] = None

    #             rows.append(row)


    #         self.insertRows(table="institutions", columns=header, parameters=rows)


    #     with open(data_path + "initial_data/positions.csv") as positions_file:

    #         #Read the information from the csv
    #         information_reader = csv.reader(positions_file)

    #         #Extract the header and skip it
    #         header = next(information_reader)

    #         rows = []
    #         for row in information_reader:

    #             for elem in range(len(row)):

    #                 if row[elem] == "NULL":
    #                     row[elem] = None

    #             rows.append(row)


    #         self.insertRows(table="positions", columns=header, parameters=rows)


    #     with open(data_path + "initial_data/experiences.csv") as experience_file:

    #         #Read the information from the csv
    #         information_reader = csv.reader(experience_file)
    #         #Extract the header and skip it
    #         header = next(information_reader)

    #         rows = []
    #         for row in information_reader:

    #             for elem in range(len(row)):

    #                 if row[elem] == "NULL":
    #                     row[elem] = None

    #             rows.append(row)


    #         self.insertRows(table="experiences", columns=header, parameters=rows)


    #     with open(data_path + "initial_data/skills.csv") as skill_file:

    #         #Read the information from the csv
    #         information_reader = csv.reader(skill_file)
    #         #Extract the header and skip it
    #         header = next(information_reader)

    #         rows = []
    #         for row in information_reader:

    #             for elem in range(len(row)):      

    #                 if row[elem] == "NULL":
    #                     row[elem] = None

    #             rows.append(row)

    #         self.insertRows(table="skills", columns=header, parameters=rows)


    # def insertRows(self, table='table', columns=['x','y'], parameters=[['v11','v12'],['v21','v22']]):
         
     
    #     #Now execute the insert queries
    #     for param in parameters:


    #         insert_query =  f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({', '.join(['%s']*len(param))})"
            

    #         try:

    #             self.query(insert_query,param)

    #         except Exception as e:
                
    #             pass
    
    #             # if table == "skills":

    #             #     print("SKILL ERROR",e)

    #             # elif table == "experiences":
    #             #     print("EXPERIENCE ERROR", e)

    #             # elif table == "positions":

    #             #     print("POSITIONS ERROR", e)

    #             # elif table == "institutions":

    #             #     print("INSTITUTIONS ERROR", e)

    #             # elif table == "feedback":

    #             #     print("FEEDBACK ERROR", e)

    #             # else:

    #             #     pass
            
        
    def getFeedbackData(self):

        select_query = "SELECT * FROM feedback"

        return self.query(select_query)


    def getResumeData(self):
        
        institutions_query = "SELECT * FROM institutions"

        institutions_query = self.query(institutions_query)

        institutions_dict = {}

        for institution in institutions_query:
            
            institutions_dict[institution["inst_id"]] = {
                "inst-id":institution["inst_id"],
                "type": institution["type"],
                "name": institution["name"],
                "department": institution["department"],
                "address": institution["address"],
                "city": institution["city"],
                "state":institution["state"],
                "zip":institution["zip"],
                "positions": {}
            }

            positions_query = f"SELECT * FROM positions WHERE positions.inst_id={institution['inst_id']}"

            positions_query = self.query(positions_query)

            #If we receive information on any positions in regard to the institution
            if positions_query != []:

                positions_dict = {}

                for position in positions_query:

                    positions_dict[position["position_id"]] = {
                        "end_date": position["end_date"],
                        "responsibilities": position["responsibilities"],
                        "start_date": position["start_date"],
                        "title": position["title"],
                        "experiences": {}
                    }


                    experiences_query = f"SELECT * FROM experiences WHERE experiences.position_id={position['position_id']}"

                    experiences_query = self.query(experiences_query)

                    #If we receive information on any positions in regard to the experiences
                    if experiences_query != []:

                        experiences_dict = {}

                        for experience in experiences_query:

                            experiences_dict[experience["experience_id"]] = {
                                "description": experience["description"],
                                "end_date": experience["end_date"],
                                "hyperlink": experience["hyperlink"],
                                "name": experience["name"],
                                "start_date": experience["start_date"],
                                "skills": {},
                            }

                        skills_query = f"SELECT * FROM skills WHERE skills.experience_id={experience['experience_id']}"

                        skills_query = self.query(skills_query)

                        #If we receive information on any positions in regard to the skills
                        if skills_query != []:

                            skills_dict = {}

                            for skill in skills_query:

                                skills_dict[skill["skill_id"]] = {
                                    "name": skill["name"],
                                    "skill_level": skill["skill_level"],
                                }


                            experiences_dict[experience["experience_id"]]["skills"] = skills_dict
                        
                        positions_dict[position["position_id"]]["experiences"] = experiences_dict

                    institutions_dict[institution["inst_id"]]["positions"] = positions_dict



        return json.dumps(institutions_dict, default=str)

#######################################################################################
# AUTHENTICATION RELATED
#######################################################################################
    def createUser(self, email='me@email.com', password='password', role='guest'):

        #We first need to check if the user exists already, we need to provide information regarding duplicates too

        email_query = "SELECT email FROM users WHERE email=%s"

        email_found = self.query(email_query, (email,))
    

        #If we find that a user already exists, we error out and tell them that we cannot fulfill their request
        if email_found != []:
            return json.dumps({"success": 0, "data": "Email already exists."})
        

        #encrypt password
        encrypted_password = self.onewayEncrypt(password)

        #Handle the default case that the user is not an owner - we will assume any other type of role other than owner will be a guest
        if role != "owner":
            
            self.insertRows('users',['email', 'password', 'role'], parameters=[[email,encrypted_password,'guest']])
        
        #We have an owner to the table
        else:

            self.insertRows('users',['email', 'password', 'role'], parameters=[[email,encrypted_password,'owner']])

        return json.dumps({'success': 1})

    def authenticate(self, email='me@email.com', password='password'):

        #See if the user exists in the database when logging in
        email_query = "SELECT email FROM users WHERE email=%s"

        email_found = self.query(email_query, (email,))

        #If we find that a user already exists, we error out and tell them that we cannot fulfill their request
        if email_found == []:
            return json.dumps({"success": 0, "data": "Email does not exist."})  
        

        #if we see that the user exists, we check to see if their password is correct
        password_query = "SELECT password FROM users WHERE email=%s"

        get_password, = self.query(password_query, (email,))

        #If password is wrong we return error message
        if get_password["password"] != self.onewayEncrypt(password):
            return json.dumps({"success": 0, "data": "Password does not match."}) 

        return json.dumps({'success': 1})

    def onewayEncrypt(self, string):
        encrypted_string = hashlib.scrypt(string.encode('utf-8'),
                                          salt = self.encryption['oneway']['salt'],
                                          n    = self.encryption['oneway']['n'],
                                          r    = self.encryption['oneway']['r'],
                                          p    = self.encryption['oneway']['p']
                                          ).hex()
        return encrypted_string


    def reversibleEncrypt(self, type, message):
        fernet = Fernet(self.encryption['reversible']['key'])
        
        if type == 'encrypt':
            message = fernet.encrypt(message.encode())
        elif type == 'decrypt':
            message = fernet.decrypt(message).decode()

        return message


