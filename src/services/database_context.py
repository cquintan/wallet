from sqlalchemy import create_engine
from sqlalchemy_utils.functions import database_exists
from . import models

class DatabaseContext():
    def __init__(self):
        self.__database_file_name = "database.db";
        self.database_engine = create_engine(f"sqlite:///{self.__database_file_name}")
        
        if not database_exists(self.database_engine.url):
            models.Base.metadata.create_all(bind=self.database_engine)