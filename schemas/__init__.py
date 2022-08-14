import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from db import (
    User as userDBModel,
    Post as postDBModel,
    session
)

class UserSchema(SQLAlchemyObjectType):
    class Meta:
        model = userDBModel
        interfaces = (relay.Node, )

class PostSchema(SQLAlchemyObjectType):
    class Meta:
        model = postDBModel
        interfaces = (relay.Node, )
        
class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_users = SQLAlchemyConnectionField(UserSchema.connection)
    all_posts = SQLAlchemyConnectionField(PostSchema.connection)
    

schema = graphene.Schema(query=Query)