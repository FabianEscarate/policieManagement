from fastapi import FastAPI
from src.Context.Http.routes.policies import policieRoutes
from src.Context.Repository.main import Engine

class Server():
    app = FastAPI()
    db = Engine()

    def run(self):
        # setup routes
        self.app.include_router(policieRoutes, prefix='/policies')

        # setup database
        self.db.createDatabase()

        return self.app