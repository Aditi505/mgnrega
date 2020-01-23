import os
import sys
import time
from sqlite3 import Error
from Models.Bdo import Bdo
from Models.Gpm import Gpm
from Models.Member import Member
from Models.User import User
from SQLite_Database.dbconnect import DbConnect


def display_panel_bdo(bdo_id, db):
    """
    Displays the panel to the user after login.

    Parameters:
    customer(Customer): customer object
    """
    os.system('clear')
    bdo = Bdo()
    # input choice
    while True:
        print('1 : Create, Update and Delete GPM')
        print('2 : Create, Update and Delete Project')
        print('3 : Approve GPM tasks')
        print('4 : Return to Login Page')
        choice = input('Enter a choice\n')
        if choice == '1':
            while True:
                print('1 : Create GPM')
                print('2 : Update GPM')
                print('3 : Delete GPM')
                print('4 : Return to BDO Main Page')
                option = input('Enter the option')
                if option == '1':
                    bdo.create_gpm(bdo_id, db)
                elif option == '2':
                    bdo.update_gpm(bdo_id, db)
                elif option == '3':
                    bdo.delete_gpm(bdo_id,db)
                elif option == '4':
                    display_panel_bdo(bdo_id, db)
                else:
                    break

        elif choice == '2':
            while True:
                print('1 : Create Project')
                print('2 : Update Project')
                print('3 : Delete Project')
                print('4 : Return to BDO Main Page')
                option = input('Enter the option')
                if option == '1':
                    bdo.create_project(bdo_id, db)
                elif option == '2':
                    bdo.update_project(bdo_id, db)
                elif option == '3':
                    bdo.delete_project(bdo_id, db)
                elif option == '4':
                    display_panel_bdo(bdo_id, db)
                else:
                    break

        elif choice == '3':
            while True:
                print('1 : Approve work assignment')
                print('2 : Approve wage ')
                print('3 : Return to BDO Main Page')
                option = input('Enter the option')
                if option == '1':
                    bdo.approve_work(db)
                elif option == '2':
                    bdo.approve_wage(db)
                elif option == '3':
                    display_panel_bdo(bdo_id, db)
        elif choice == '4':
            main_menu()
        else:
            break


def display_panel_gpm(gpm_id, db):
    """
    Displays the panel to the user after login.

    Parameters:
    customer(Customer): customer object
    """
    os.system('clear')
    gpm = Gpm()
    # input choice
    while True:
        print('1 : Create, Update and Delete Member')
        print('2 : Allot Work')
        print('3 : Issue Job Card')
        print('4 : Return to Login Page')
        choice = input('Enter a choice\n')
        if choice == '1':
            while True:
                print('1 : Create Member')
                print('2 : Update Member')
                print('3 : Delete Member')
                print('4 : Return to GPM Main Page')
                option = input('Enter the option')
                if option == '1':
                    gpm.create_member(gpm_id, db)
                elif option == '2':
                    gpm.update_member(gpm_id, db)
                elif option == '3':
                    gpm.delete_member(gpm_id,db)
                elif option == '4':
                    display_panel_gpm(gpm_id, db)
                else:
                    break
        elif choice == '2':
            gpm.allot_work(db)
        elif choice == '3':
            gpm.issue_job_card(db)
        elif choice == '4':
            main_menu()
        else:
            break


def display_panel_member(member_id, db):
    """
    Displays the panel to the user after login.

    Parameters:
    customer(Customer): customer object
    """
    os.system('clear')
    member = Member()
    # input choice
    while True:
        print("1. View Wage")
        print("2. File Complain")
        print('3 : Return to Login Page')
        choice = input('Enter a choice\n')
        if choice == '1':
            member.view_wage(member_id, db)
        elif choice == '2':
            member.file_complain(member_id, db)
        elif choice == '3':
            main_menu()


def main_menu():
    try:
        user = User()
        while True:
            # input choice
            print("1. BDO Login")
            print("2. GPM Login")
            print("3. Member Login")
            print("Press Any Other key to Exit......")
            choice = int(input("Enter choice: "))

            if choice == 1:
                os.system('clear')
                # redirect to login page
                user_access = user.bdo_login(db)
                if user_access[0] == 'true':
                    bdo_id = user_access[1]
                    # redirect to display_panel of bdo
                    display_panel_bdo(bdo_id, db)
                else:
                    print("Wrong Credentials, login again!")
                    main_menu()

            elif choice == 2:
                os.system('clear')
                # initialize customer instance
                user_access = user.gpm_login(db)
                if user_access[0] == 'true':
                    gpm_id = user_access[1]
                    # redirect to dashboard
                    display_panel_gpm(gpm_id, db)
                else:
                    print("Wrong Credentials, login again!")
                    main_menu()

            elif choice == 3:
                os.system('clear')
                # initialize customer instance
                user_access = user.member_login(db)
                if user_access[0] == 'true':
                    member_id = user_access[1]
                    # redirect to dashboard
                    display_panel_member(member_id, db)
                else:
                    print("Wrong Credentials, login again!")
                    main_menu()
            else:
                os.system('clear')
                print("Thank You for Using This Application")
                time.sleep(2)
                sys.exit()
    except Error as se:
        db.conn.rollback()
        print("Something went wrong: {}".format(se))
    except ValueError as ve:
        print("Invalid Choice, Please enter a valid number")
    except Exception as e:
        print("exception handled: {}".format(e))


# Main Program Starts here
if __name__ == "__main__":
    # get database handle
    db = DbConnect("mgnerga.db")
    main_menu()
