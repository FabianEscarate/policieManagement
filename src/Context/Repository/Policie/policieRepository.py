from src.Context.Http.schemas.policiesPayload import createPolicie
from src.Context.Repository.Policie.model import Policie as modelPolicie
from src.Context.Repository.main import Engine, select

class policieRepository():

    Engine = Engine()

    def addPolicie(self, policie: createPolicie):
        policieToAdd = modelPolicie.model_validate(policie)
        with self.Engine.getSession().__next__() as sess:
            sess.add(policieToAdd)
            sess.commit()
            sess.refresh(policieToAdd)
            return policieToAdd
        

    def getPolicieById(self, idPolicie: str):
        with self.Engine.getSession().__next__() as session:
            return session.get(modelPolicie, idPolicie)
        
    def getManyPolicies(self):
        with self.Engine.getSession().__next__() as session:
            policies = session.exec(select(modelPolicie)).all()
            return policies
        
    def updatePolicie(self,idPolicie: str, policie: modelPolicie):
        with self.Engine.getSession().__next__() as session:
            dbPolicie = session.get(modelPolicie, idPolicie)
            policieUpdate = policie.model_dump(exclude_unset=True)
            dbPolicie.sqlmodel_update(policieUpdate)
            session.add(dbPolicie)
            session.commit()
            session.refresh(dbPolicie)
            return dbPolicie
