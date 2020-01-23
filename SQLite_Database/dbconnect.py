import sqlite3
from sqlite3 import Error
from SQLite_Database import tablequery


class DbConnect:
    def __init__(self, db_file):
        """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
        self.conn = None
        try:
            self.conn = sqlite3.connect(db_file)
            print("Connection is established: Database Created!")
            self.cursor = self.conn.cursor()
            # self.table_def()
            self.cursor.executescript(tablequery.sql_create_table)
        except Error:
            print(Error)

    def save(self):
        """

        :return:
        :rtype:
        """
        # commit database operation
        self.conn.commit()

    # def create_table(self, create_table_sql):
    #     """ create a table from the create_table_sql statement
    #     :param create_table_sql: a CREATE TABLE statement
    #     :return:
    #     """
    #     try:
    #         self.cursor.execute(create_table_sql)
    #         self.save()
    #     except Error as e:
    #         print(e)

    # create tables
    # def table_def(self):
    #     """
    #
    #     :return:
    #     :rtype:
    #     """
    #     if self.conn is not None:
    #         # create bdos table
    #         self.create_table(tablequery.sql_create_bdos_table)
    #
    #         # create gpms table
    #         self.create_table(tablequery.sql_create_gpms_table)
    #
    #         # create projects table
    #         self.create_table(tablequery.sql_create_projects_table)
    #
    #         # create members table
    #         self.create_table(tablequery.sql_create_members_table)
    #
    #         # create tasks table
    #         self.create_table(tablequery.sql_create_tasks_table)
    #     else:
    #         print("Error! cannot create the database connection.")

    def validate_credentials(self, id, password, table_name):
        self.cursor.execute(f"SELECT * FROM '{table_name}'  WHERE id=? AND password = ?", (id, password,))
        result = self.cursor.fetchall()
        if result:
            return 'true'
        return 'false'

    def get_username(self, id, table_name):
        self.cursor.execute(f"SELECT name FROM '{table_name}' where id = ?", (id,))
        result = self.cursor.fetchall()
        for row in result:
            return row[0]

    def insert_gpm(self, user_details, table_name):
        self.cursor.execute(f"INSERT INTO '{table_name}' (name, password, district, state, pincode, bdo_id) "
                            f"VALUES ('{user_details['name']}','{user_details['password']}','{user_details['district']}','{user_details['state']}','{user_details['pincode']}', '{user_details['bdo_id']}');")
        self.save()

    def delete_data(self, id, table_name):
        self.cursor.execute(f"DELETE FROM '{table_name}'where id = '{id}';")
        self.save()

    def update_data(self, id, dict, table_name):
        for item in dict.items():
            if item[1] != '':
                sql_query = f"UPDATE '{table_name}' SET '{item[0]}' = '{item[1]}' WHERE id = '{id}'"
                self.cursor.execute(sql_query)
                self.conn.commit()

    def insert_project(self, user_details, table_name):
        self.cursor.execute(
            f"INSERT INTO '{table_name}' (name, category, area, state, labours, cost, start_date, end_date, bdo_id) "
            f"VALUES ('{user_details['name']}','{user_details['category']}','{user_details['area']}','{user_details['state']}','{user_details['labours']}', '{user_details['cost']}','{user_details['start_date']}','{user_details['end_date']}', '{user_details['bdo_id']}');")
        self.save()

    def insert_member(self, user_details, table_name):
        self.cursor.execute(
            f"INSERT INTO '{table_name}' (name, password, district, state, working_days, attendance, age, gender, address, gpm_id) "
            f"VALUES ('{user_details['name']}','{user_details['password']}','{user_details['district']}','{user_details['state']}','{user_details['working_days']}', '{user_details['attendance']}', '{user_details['age']}','{user_details['gender']}','{user_details['address']}','{user_details['gpm_id']}');")
        self.save()

    def validate_user(self, id, table_name):
        sql_query = f"SELECT * FROM '{table_name}' WHERE id == '{id}'"
        self.cursor.execute(sql_query)
        result = self.cursor.fetchall()
        if not result:
            return 'false'
        else:
            return 'true'

    def show_wage(self, id, table_name):
        sql_query = f"SELECT wage from '{table_name} WHERE member_id == '{id}'"
        self.cursor.execute(sql_query)
        result = self.cursor.fetchall()
        for row in result:
            return row[0]

    def complain(self, complain, member_id, table_name):
        self.cursor.execute(f"UPDATE '{table_name}' SET  complain=? WHERE member_id = ? ", (complain, member_id,))
        self.save()

    def job_card(self, id, table_name):
        self.cursor.execute(f"Select * from '{table_name}' Where id = '{id}'")
        check = self.cursor.fetchall()
        for row in check:
            if row[10] == 'true':
                print("Job card already issued!")
                print("{0} {1}".format(row[1], row[5]))
                print("=================================")
                print("{0} \t {1} \t {2}".format("Gender", "Address", "Place"))
                print("=================================")
                for record in check:
                    print("{0} \t {1} \t {2}".format(record[6], record[7], record[3], record[4]))
                    print(" ")
            else:
                for row in check:
                    print("{0} {1}".format(row[1], row[5]))
                    print("=================================")
                    print("{0} \t {1} \t {2}".format("Gender", "Address", "Place"))
                    print("=================================")
                    for record in check:
                        print("{0} \t {1} \t {2}".format(record[6], record[7], record[3], record[4]))
                        print(" ")
                self.cursor.execute(f"Update '{table_name}'  SET 'is_card_issued' = 'true' WHERE id = '{id}'")
                self.save()
                print("The job card is issued successfully!")

    def validate_access(self, pid, id, table_name):
        sql_query = f"SELECT id FROM {table_name} WHERE id = {id} AND bdo_id = {pid}"
        self.cursor.execute(sql_query)
        result = self.cursor.fetchall()
        if not result:
            return 'false'
        else:
            return 'true'

    def assign_project(self, member_id, project_id, table_name):
        sql_query = f"INSERT INTO {table_name} (member_id, project_id) VALUES (?,?))"
        self.cursor.execute(sql_query, (member_id, project_id,))
        self.save()
