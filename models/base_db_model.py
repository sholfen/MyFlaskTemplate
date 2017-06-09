#!/usr/bin/python
# -*- coding: utf-8 -*-
import modules.db_helper as helper
import modules.config_module as config_module


class BaseDBModel(object):

    def __init__(self, db_section_name):
        self.db_section_name = db_section_name
        self.engine = helper._init_sqlalchemy_engine_object(db_section_name)

    def execute_sql_command(self, sql_command):
        result = helper.execute_sql_command(self.db_section_name, sql_command, self.engine)
        return result

    def execute_sqlite_command(self, sql_command):
        result = helper.execute_sqlite_command(self.db_section_name, sql_command, self.engine)
        return result

    def get_sql_command(self, sql_command_name):
        config = config_module.get_config_object('./config/sql_commands.config')
        return config.get(self.db_section_name, sql_command_name)

    def print_db_name(self):
        return self.db_section_name
