from sqlalchemy import create_engine
from sqlalchemy_utils.functions import database_exists
from . import models

## @brief
#  create a class DatabaseContext
class DatabaseContext():
    # create a function
    def __init__(self):
        # name the database
        self.__database_file_name = "database.db";
        # create the database kernel and define database locations
        self.database_engine = create_engine(f"sqlite:///{self.__database_file_name}")

        # database check
        if not database_exists(self.database_engine.url):
            models.Base.metadata.create_all(bind=self.database_engine)