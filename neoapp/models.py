from neomodel import StructuredNode, Relationship, StringProperty, IntegerProperty, UniqueIdProperty, RelationshipTo, StructuredRel, RelationshipFrom, FloatProperty

class Team(StructuredNode):
    name = StringProperty(unique_index=True, required=True)

class Player(StructuredNode):
    name = StringProperty(required=True, index=True)
    age = IntegerProperty(required=True, index=True)
    height = FloatProperty(required=True, index=True)
    number = IntegerProperty(required=True, index=True)
    weight = IntegerProperty(required=True, index=True)

    team = RelationshipTo(Team, 'PLAYS_FOR')

    rivales = RelationshipTo(Team, 'PLAYED_AGAINST')

    teammates = Relationship('Player', 'TEAMMATES')


class Coach(StructuredNode):
    name = StringProperty(required=True, index=True)
    age = IntegerProperty(required=True, index=True)

    coaches = RelationshipTo(Player, 'COACHES')

    team = RelationshipTo(Team, 'COACHES_FOR')


