class User:
    def __init__(self):
        pass

    def bdo_login(self, db):
        id = int(input('Enter the BDO userID'))
        password = input('Enter the Password')
        access = db.validate_credentials(id, password, 'bdos')
        if access == 'true':
            username = db.get_username(id, 'bdos')
            print("Welcome " + username)
            return ['true', id]
        else:
            return ['false']

    def gpm_login(self, db):
        id = int(input('Enter the GPM userID'))
        password = input('Enter the Password')
        access = db.validate_credentials(id, password, 'gpms')
        if access == 'true':
            username = db.get_username(id, 'gpms')
            print("Welcome " + username)
            return ['true', id]
        else:
            return ['false']

    def member_login(self, db):
        id = int(input('Enter the Member userID'))
        password = input('Enter the Password')
        access = db.validate_credentials(id, password, 'members')
        if access == 'true':
            username = db.get_username(id, 'members')
            print("Welcome " + username)
            return ['true', id]
        else:
            return ['false']
