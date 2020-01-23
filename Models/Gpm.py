class Gpm:
    def __init__(self):
        pass

    def insert_member_values(self, id):
        print("Enter GPM Details")
        name = input("Name:")
        password = input("Password:")
        district = input("District:")
        state = input("State:")
        working_days = input("Working Days:")
        attendance = input("Attendance:")
        age = input("Age:")
        gender = input("Gender:")
        address = input("Address:")
        gpm_id = id
        user_details = {'password': password, 'name': name, 'district': district, 'state': state,
                        'working_days': working_days, 'attendance': attendance, 'age': age, 'gender': gender,
                        'address': address,
                        'gpm_id': gpm_id}
        return user_details

    def create_member(self, gpm_id, db):
        user_details = self.insert_member_values(gpm_id)
        db.insert_member(user_details, 'members')
        print("Member successfully added!")

    def update_member(self, gpm_id, db):
        member_id = input('Enter the member ID you want to update')
        user_exist = db.validate_user(member_id, 'members')
        if user_exist == 'false':
            print('Member not found')
            return
        user_access = db.validate_access(gpm_id, member_id, 'members')
        if user_access == 'false':
            print('Access Denied')
            return
        member_details = self.insert_member_values(gpm_id)
        db.update_data(member_id, member_details, 'members')
        print('Member successfully updated')

    def delete_member(self, gpm_id, db):
        member_id = int(input("Enter the member Id you want to delete:"))
        user_exist = db.validate_user(member_id, 'members')
        if user_exist == 'false':
            print('Member not found')
            return
        user_access = db.validate_access(gpm_id, member_id, 'members')
        if user_access == 'false':
            print('Access Denied')
            return
        db.delete_data(id, 'members')
        print("Member successfully deleted!")

    def issue_job_card(self, gpm_id, db):
        member_id = int(input("Enter the member Id you want issue job card for:"))
        user_exist = db.validate_user(member_id, 'members')
        if user_exist == 'false':
            print('Member not found')
            return
        user_access = db.validate_access(gpm_id, member_id, 'members')
        if user_access == 'false':
            print('Access Denied')
            return
        db.job_card(id, 'members')

    def allot_work(self, gpm_id, db):
        member_id = int(input('Enter the Member Id'))
        member_exist = db.validate_user(member_id, 'members')
        if member_exist == 'false':
            print('Member does not exist')
            return
        user_access = db.access_user(gpm_id, member_id, 'members')
        if user_access == 'false':
            print('Member Access Denied')
            return
        project_id = int(input('Enter the project you want this member to assign to :'))
        project_exist = db.validate_user(project_id, 'projects')
        if project_exist == 'false':
            print('Project does not exist')
            return
        db.assign_project(member_id, project_id, 'tasks')

