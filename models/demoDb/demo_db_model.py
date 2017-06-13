import sys
import logging

from sqlalchemy import Column, MetaData, Table, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import or_, and_, desc, func
from sqlalchemy.sql import label

import modules.config_module as config_module
from models.base_db_model import BaseDBModel

Base = declarative_base()

class Album(Base):

    __tablename__ = 'Album'

    def __init__(self):
        super(Album, self).__init__()

    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer)


class DemoDBModel(BaseDBModel):

    def __init__(self, *args, **kwargs):
        kwargs['db_section_name'] = 'Demo_db'
        super(DemoDBModel, self).__init__(*args, **kwargs)

    def list_album_title(self):
        sql_command = self.get_sql_command('list_album_title')
        return self.execute_sqlite_command(sql_command)

    def list_all_employee(self):
        sql_command = self.get_sql_command('list_all_employee')
        return self.execute_sqlite_command(sql_command)

    def list_all_album(self):
        rows = self.get_session().query(Album.AlbumId,
                Album.Title,
                Album.ArtistId)

        result = []
        for item in rows:
            result.append({
                    'AlbumId': item.AlbumId,
                    'Title': item.Title,
                    'ArtistId': item.ArtistId
            })

        return result
