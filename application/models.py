from application import db


attribute_tags = db.Table('attribute_tags',
                          db.Column('attribute_id',
                                    db.Integer,
                                    db.ForeignKey('Attributes.id'),
                                    primary_key=True),
                          db.Column('tag_id',
                                    db.Integer,
                                    db.ForeignKey('Tags.id'),
                                    primary_key=True))


class Attributes(db.Model):
    __tablename__ = 'Attributes'
    id = db.Column(db.Integer, primary_key=True)
    attribute = db.Column(db.String(128), index=True, unique=False)
    value = db.Column(db.String(128), index=True, unique=False, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    tags = db.relationship('Tags', secondary=attribute_tags, lazy='subquery',
                           backref=db.backref('Attr', lazy=True))

    def __init__(self, attribute, value, weight):
        self.attribute = attribute
        self.value = value
        self.weight = weight

    def __repr__(self):
        return '<Attribute {} Value {} Weight {}>'.format(self.attribute, self.value, self.weight)

    def get_tag(self, tag_name):
        """
        Searches through the tags of the attribute for the values of tag_name.
        If a tag does not exist then it will return False.
        This is to allow tags to be defined with the true value and not require a false as well.
        :param tag_name: the tag name to look up
        :return: str, boolean
        """
        tag_values = []
        for tag in self.tags:
            if tag.tag_name == tag_name:
                tag_values.append(tag.tag_value)

        if len(tag_values) == 1:
            if tag_values[0].lower() == 'true':
                return True
            elif tag_values[0].lower() == 'false':
                return False
            else:
                return tag_values[0]
        elif len(tag_values) > 1:
            return tag_values
        else:
            return False

    def get_tag_dict(self):
        tag_dict = {}
        for tag in self.tags:
            if tag.tag_name in tag_dict.keys():
                tag_dict[tag.tag_name].append(tag.tag_value)
            else:
                tag_dict[tag.tag_name] = [tag.tag_value]
        return tag_dict


class Tags(db.Model):
    __tablename__ = 'Tags'
    id = db.Column(db.Integer, primary_key=True)
    tag_name = db.Column(db.String(128), nullable=False)
    tag_value = db.Column(db.String(256), nullable=False)

    def __init__(self, tag, value):
        self.tag_name = tag
        self.tag_value = value

    def __repr__(self):
        return '<tag {}: {}>'.format(self.tag_name, self.tag_value)


ability_tags = db.Table('ability_tags',
                        db.Column('ability_id',
                                  db.Integer,
                                  db.ForeignKey('Abilities.id'),
                                  primary_key=True),
                        db.Column('tag_id',
                                  db.Integer,
                                  db.ForeignKey('AbilityTags.id'),
                                  primary_key=True))


class Abilities(db.Model):
    __tablename__ = 'Abilities'
    id = db.Column(db.Integer, primary_key=True)
    ability = db.Column(db.String(128), index=True, unique=False)
    value = db.Column(db.String(128), index=True, unique=False, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    tags = db.relationship('AbilityTags', secondary=ability_tags, lazy='subquery',
                           backref=db.backref('Abbl', lazy=True))

    def __init__(self, ability, value, weight):
        self.ability = ability
        self.value = value
        self.weight = weight

    def __repr__(self):
        return '<Ability {} Value {} Weight {}>'.format(self.ability, self.value, self.weight)

    def get_tag(self, tag_name):
        """
        Searches through the tags of the attribute for the values of tag_name.
        If a tag does not exist then it will return False.
        This is to allow tags to be defined with the true value and not require a false as well.
        :param tag_name: the tag name to look up
        :return: str, boolean
        """
        tag_values = []
        for tag in self.tags:
            if tag.tag_name == tag_name:
                tag_values.append(tag.tag_value)

        if len(tag_values) == 1:
            if tag_values[0].lower() == 'true':
                return True
            elif tag_values[0].lower() == 'false':
                return False
            else:
                return tag_values[0]
        elif len(tag_values) > 1:
            return tag_values
        else:
            return False

    def get_tag_dict(self):
        tag_dict = {}
        for tag in self.tags:
            if tag.tag_name in tag_dict.keys():
                tag_dict[tag.tag_name].append(tag.tag_value)
            else:
                tag_dict[tag.tag_name] = [tag.tag_value]
        return tag_dict


class AbilityTags(db.Model):
    __tablename__ = 'AbilityTags'
    id = db.Column(db.Integer, primary_key=True)
    tag_name = db.Column(db.String(128), nullable=False)
    tag_value = db.Column(db.String(256), nullable=False)

    def __init__(self, tag, value):
        self.tag_name = tag
        self.tag_value = value

    def __repr__(self):
        return '<tag {}: {}>'.format(self.tag_name, self.tag_value)


