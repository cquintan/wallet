from sqlalchemy import create_engine
from sqlalchemy_utils.functions import database_exists
from . import models

## @brief
#  create a class DatabaseContext
class DatabaseContext():
    def __init__(self):     #create a function
        self.__database_file_name = "database.db";      #name the database
        self.database_engine = create_engine(f"sqlite:///{self.__database_file_name}")      #create the database kernel and define database locations
        
        if not database_exists(self.database_engine.url):       #database check
            models.Base.metadata.create_all(bind=self.database_engine)