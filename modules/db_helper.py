import modules.config_module as config_module
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sqlalchemy


def _init_sqlalchemy_engine_object(db_section_name):
    """
    return sqlalchemy db enbine object

    >>> _init_sqlalchemy_engine_object()

    """
    print('init db engine')
    config = config_module.get_config_object('./config/db.config')
    connection_string = config.get(db_section_name, 'connection_string')
    db_host = config.get(db_section_name, 'db_host')
    db_port = config.get(db_section_name, 'db_port')
    db_name = config.get(db_section_name, 'db_name')
    db_user = config.get(db_section_name, 'db_user')
    db_password = config.get(db_section_name, 'db_password')
    connection_string = connection_string.format(db_host=db_host,
            db_port=db_port,
            db_name=db_name,
            db_user=db_user,
            db_password=db_password)
    engine = create_engine(connection_string, echo=True)
    return engine

def execute_sql_command(db_section_name, sql_command, engine):
    """
    execute sql command and return db result

    >>> execute_sql_command('select * from test_table')
    
    """
    # init session object
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    result = session.execute(sql_command)
    session.commit()
    return result

def execute_sqlite_command(db_section_name, sql_command, engine):
    """
    execute sql command and return db result

    >>> execute_sqlite_command('select * from test_table')
    
    """
    # init session object
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    result = session.execute(sql_command)
    return result

def get_session(engine):
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    return session

