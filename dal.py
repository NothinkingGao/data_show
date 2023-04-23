from models import User, Group, UserGroup, UserSession
class UserDal(object):
    """User data access layer
    """

    def __init__(self, db):
        self.db = db

    def login(self, username, password):
        """Login user

        :param username: username
        :param password: password
        :return: user id
        """
        user = User.query.filter_by(username=username, password=password).first()
        if user is None:
            return None
        else:
            return user

    def logout(self, user_id):
        """Logout user

        :param user_id: user id
        :return: None
        """
        UserSession.query.filter_by(user_id=user_id).delete()

    def register(self, username, password):
        """Register user

        :param username: username
        :param password: password
        :return: user id
        """
        user = User(username=username, password=password)
        self.db.session.add(user)
        self.db.session.commit()
        return user

    def get_user(self, user_id):
        """Get user by id

        :param user_id: user id
        :return: user
        """
        return User.query.filter_by(id=user_id).first()

    def get_user_by_username(self, username):
        """Get user by username

        :param username: username
        :return: user
        """
        return User.query.filter_by(username=username).first()


    def get_users(self):
        """Get all users

        :return: list of users
        """
        return User.query.all()

    def get_users_by_group(self, group_id):
        """Get users by group

        :param group_id: group id
        :return: list of users
        """
        return User.query.join(UserGroup).filter(UserGroup.group_id == group_id).all()


class GroupDal(object):
    """Group data access layer
    """

    def __init__(self, db):
        self.db = db

    def get_group(self, group_id):
        """Get group by id

        :param group_id: group id
        :return: group
        """
        return Group.query.filter_by(id=group_id).first()

    def get_groups(self):
        """Get all groups

        :return: list of groups
        """
        return Group.query.all()

    def get_groups_by_user(self, user_id):
        """Get groups by user

        :param user_id: user id
        :return: list of groups
        """
        return Group.query.join(UserGroup).filter(UserGroup.user_id == user_id).all()

    def get_groups_by_user_and_group(self, user_id, group_id):
        """Get groups by user and group

        :param user_id: user id
        :param group_id: group id
        :return: list of groups
        """
        return Group.query.join(UserGroup).filter(UserGroup.user_id == user_id).filter(UserGroup.group_id == group_id).all()

    def get_groups_by_user_and_name(self, user_id, name):
        """Get groups by user and name

        :param user_id: user id
        :param name: group name
        :return: list of groups
        """
        return Group.query.join(UserGroup).filter(UserGroup.user_id == user_id).filter(Group.name == name).all()

    def get_groups_by_name(self, name):
        """Get groups by name

        :param name: group name
        :return: list of groups
        """
        return Group.query.filter_by(name=name).all()

    def add_group(self, name, user_id):
        """Add group

        :param name: group name
        :param user_id: user id
        :return: group id
        """
        group = Group(name=name)
        self.db.session.add(group)
        self.db.session.commit()
        user_group = UserGroup(user_id=user_id, group_id=group.id)
        self.db.session.add(user_group)
        self.db.session.commit()
        return group.id

    def delete_group(self, group_id):
        """Delete group

        :param group_id: group id
        :return: None
        """
        Group.query.filter_by(id=group_id).delete