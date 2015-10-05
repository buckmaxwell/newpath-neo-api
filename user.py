from neomodel import (StringProperty, AliasProperty, RelationshipTo, Relationship, ZeroOrOne)
from neoapi import SerializableStructuredNode, SerializableStructuredRel, DateTimeProperty


class FriendRel(SerializableStructuredRel):
    __type__ = 'friend'  # => __type__ must be specified and the same as the default for type

    type = StringProperty(default='friend')
    met_at = StringProperty()


class User(SerializableStructuredNode):
    __type__ = 'users'  # => required, same as type default

    # INFO
    secret = ['password']

    # ATTRIBUTES
    type = StringProperty(default='users')                 # => required
    id = StringProperty(unique_index=True, required=True)  # => required
    email = AliasProperty(to='id')
    password = StringProperty(required=True)
    gender = StringProperty()

    # RELATIONSHIPS
    friends = Relationship('User', 'HAS_FRIEND', model=FriendRel)  # => for all relationships a model must be chosen
    mom = RelationshipTo('User', 'HAS_MOM', cardinality=ZeroOrOne, model=SerializableStructuredRel)


