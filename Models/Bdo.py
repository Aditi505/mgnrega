class Bdo:
    def __init__(self):
        pass

    def insert_gpm_values(self, id):
        print("Enter GPM Details")
        name = input("Name:")
        password = input("Password:")
        district = input("District:")
        state = input("State:")
        pincode = input("Pincode:")
        bdo_id = id
        user_details = {'password': password, 'name': name, 'district': district, 'state': state, 'pincode': pincode,
                        'bdo_id': bdo_id}
        return user_details

    def create_gpm(self, bdo_id, db):
        user_details = self.insert_gpm_values(bdo_id)
        db.insert_gpm(user_details, 'gpms')
        print("Gpm successfully added!")

    def update_gpm(self, bdo_id, db):
        gpm_id = input('Enter the gpm ID you want to update')
        user_exist = db.validate_user(gpm_id, 'gpms')
        if user_exist == 'false':
            print('GPM User not found')
            return
        user_access = db.validate_access(bdo_id, gpm_id, 'gpms')
        if user_access == 'false':
            print('Access Denied')
            return
        gpm_details = self.insert_gpm_values(bdo_id)
        db.update_data(gpm_id, gpm_details, 'gpms')
        print('Gpm successfully updated')

    def delete_gpm(self, bdo_id, db):
        gpm_id = int(input("Enter the Gpm Id you want to delete:"))
        user_exist = db.validate_user(gpm_id, 'gpms')
        if user_exist == 'false':
            print('GPM User not found')
            return
        user_access = db.validate_access(bdo_id, gpm_id, 'gpms')
        if user_access == 'false':
            print('Access Denied')
            return
        db.delete_data(id, 'gpms')
        print("Gpm successfully deleted!")

    def insert_project_values(self, id):
        print("Enter Project Details")
        name = input("Name:")
        area = input("Area:")
        state = input("State:")
        labours = input("No of workers required:")
        cost = input("Cost Estimated:")
        start_date = input("Start date:")
        end_date = input("End date:")
        bdo_id = id
        category = input("Enter the category out of 1. Road_Construction 2.Sewage_Treatment 3. Building_Construction")
        if category.lower() == "road_construction" or category.lower() == "sewage_treatment" or category.lower() == "building_construction":
            user_details = {'area': area, 'name': name, 'labours': labours, 'category': category.lower(), 'cost': cost,
                            'start_date': start_date, 'state': state, 'bdo_id': bdo_id, 'end_date': end_date}
            return user_details
        else:
            print("Wrong Category! Please choose a right category for the project")
            self.insert_project_values(id)

    def create_project(self, bdo_id, db):
        user_details = self.insert_project_values(bdo_id)
        db.insert_project(user_details, 'projects')
        print("Projects successfully added!")

    def update_project(self, bdo_id, db):
        project_id = input('Enter the project ID you want to update')
        user_exist = db.validate_user(project_id, 'projects')
        if user_exist == 'false':
            print('Project not found')
            return
        user_access = db.validate_access(bdo_id, project_id, 'projects')
        if user_access == 'false':
            print('Access Denied')
            return
        project_details = self.insert_project_values(bdo_id)
        db.update_data(project_id, project_details, 'projects')
        print('Project successfully updated')

    def delete_project(self, bdo_id, db):
        project_id = int(input("Enter the projectId you want to delete:"))
        user_exist = db.validate_user(id, 'projects') # TODO : project inplace of user
        if user_exist == 'false':
            print('Project not found')
            return
        user_access = db.validate_access(bdo_id, project_id, 'projects')
        if user_access == 'false':
            print('Access Denied')
            return
        db.delete_data(id, 'projects')
        print("Project successfully deleted!")

    def approve_work(self, db):
        db.pending_approval_list('assign')
        member_id = input('Enter the member id of the assign task you want to approve')
        db.approve_status(member_id, 'assign')

    def approve_wage(self, db):
        pass

    def pending_approval_list(self, db):
        pass

    def requested_approval_list(self, db):
        pass
