from sqlmodel import SQLModel,create_engine, Session, select
from src.config.setting import settings

class Engine():
    engine = create_engine(settings.get("url_database"), echo=True)

    def createDatabase(self):
        SQLModel.metadata.create_all(self.engine);

    def getSession(self):
        with Session(self.engine) as session:
            yield session