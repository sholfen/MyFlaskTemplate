import sys
import logging
import modules.config_module as config_module
from models.base_db_model import BaseDBModel


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