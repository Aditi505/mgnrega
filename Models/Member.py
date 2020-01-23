class Member:
    def __init__(self):
        pass

    def view_wage(self, member_id, db):
        wage = db.show_wage(member_id, 'tasks')
        print("Your wage is:" + wage)

    def file_complain(self, member_id, db):
        complain = input("Enter your complain:")
        db.complain(complain, member_id, 'tasks')
        print("Complain filed successfully!")
