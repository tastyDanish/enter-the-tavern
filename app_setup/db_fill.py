import pandas as pd
from application.models import Attributes, Tags, Abilities, AbilityTags
from application import db
import json


def import_attrs():
    df = pd.read_csv('db_import_attributes.csv')

    for index, row in df.iterrows():
        attr = Attributes(attribute=row['attribute'],
                          value=row['value'],
                          weight=row['weight'])
        if type(row['tags']) is str:
            tags_list = json.loads(row['tags'])
            for tag, value in tags_list.items():
                if type(value) is list:
                    for v in value:
                        final_tag = Tags.query.filter_by(tag_name=tag, tag_value=v).first()
                        if final_tag is not None:
                            attr.tags.append(final_tag)
                        else:
                            print('New attr tag found {}: {}'.format(tag, v))
                            new_tag = Tags(tag=tag, value=v)
                            db.session.add(new_tag)
                            db.session.commit()
                            new_tag = Tags.query.filter_by(tag_name=tag, tag_value=v).first()
                            attr.tags.append(new_tag)
                else:
                    final_tag = Tags.query.filter_by(tag_name=tag, tag_value=value).first()
                    if final_tag is not None:
                        attr.tags.append(final_tag)
                    else:
                        print('New attr tag found {}: {}'.format(tag, value))
                        new_tag = Tags(tag=tag, value=value)
                        db.session.add(new_tag)
                        db.session.commit()
                        new_tag = Tags.query.filter_by(tag_name=tag, tag_value=value).first()
                        attr.tags.append(new_tag)

        print('Adding Attribute {} to DB'.format(attr))
        db.session.add(attr)
        db.session.commit()


def import_abils():
    df = pd.read_csv('db_import_abilities.csv')

    for index, row in df.iterrows():
        abil = Abilities(ability=row['ability'], value=row['value'], weight=row['weight'])
        if type(row['tags']) is str:
            tags_list = json.loads(row['tags'])
            for tag, value in tags_list.items():
                if type(value) is list:
                    for v in value:
                        final_tag = AbilityTags.query.filter_by(tag_name=tag, tag_value=v).first()
                        if final_tag is not None:
                            abil.tags.append(final_tag)
                        else:
                            print('New abil tag found {}: {}'.format(tag, v))
                            new_tag = AbilityTags(tag=tag, value=v)
                            db.session.add(new_tag)
                            db.session.commit()
                            new_tag = AbilityTags.query.filter_by(tag_name=tag, tag_value=v).first()
                            abil.tags.append(new_tag)
                else:
                    final_tag = AbilityTags.query.filter_by(tag_name=tag, tag_value=value).first()
                    if final_tag is not None:
                        abil.tags.append(final_tag)
                    else:
                        print('New abil tag found {}: {}'.format(tag, value))
                        new_tag = AbilityTags(tag=tag, value=value)
                        db.session.add(new_tag)
                        db.session.commit()
                        new_tag = AbilityTags.query.filter_by(tag_name=tag, tag_value=value).first()
                        abil.tags.append(new_tag)

        print('Adding Ability: {} to DB'.format(abil))
        db.session.add(abil)
        db.session.commit()


if __name__ == '__main__':
    import_attrs()
    import_abils()
