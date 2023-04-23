from __future__ import unicode_literals
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __init__(self, name, email, password, created_at, updated_at):
        self.name = name
        self.email = email
        self.password = password
        self.created_at = created_at
        self.updated_at = updated_at
    
    def __repr__(self):
        return "<User(name='%s', email='%s', password='%s', created_at='%s', updated_at='%s')>" % (
            self.name, self.email, self.password, self.created_at, self.updated_at)
    
    def __str__(self):
        return "User(name='%s', email='%s', password='%s', created_at='%s', updated_at='%s')" % (
            self.name, self.email, self.password, self.created_at, self.updated_at)
    
    def __unicode__(self):
        return "User(name='%s', email='%s', password='%s', created_at='%s', updated_at='%s')" % (
            self.name, self.email, self.password, self.created_at, self.updated_at)

class UserGroup(Base):
    __tablename__ = "user_groups"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    group_id = Column(Integer, ForeignKey("groups.id"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __init__(self, user_id, group_id, created_at, updated_at):
        self.user_id = user_id
        self.group_id = group_id
        self.created_at = created_at
        self.updated_at = updated_at
    
    def __repr__(self):
        return "<UserGroup(user_id='%s', group_id='%s', created_at='%s', updated_at='%s')>" % (
            self.user_id, self.group_id, self.created_at, self.updated_at)
    
    def __str__(self):
        return "UserGroup(user_id='%s', group_id='%s', created_at='%s', updated_at='%s')" % (
            self.user_id, self.group_id, self.created_at, self.updated_at)
    
    def __unicode__(self):
        return "UserGroup(user_id='%s', group_id='%s', created_at='%s', updated_at='%s')" % (
            self.user_id, self.group_id, self.created_at, self.updated_at)
