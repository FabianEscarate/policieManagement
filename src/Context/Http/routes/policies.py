from fastapi import APIRouter, status, HTTPException, Response
from uuid import UUID
from src.Context.Http.schemas.policiesPayload import createPolicie, Policie
from src.App.Policies.addPolicie import addPolicie
from src.App.Policies.getPolicie import getPolicieById
from src.App.Policies.getPolicies import getPolicies

policieRoutes = APIRouter()


@policieRoutes.post("", status_code=status.HTTP_201_CREATED, response_model=Policie)
def postPolicie(policie: createPolicie):
    try:
        result = addPolicie().run(policie)
        return result
    except Exception as e:
        raise HTTPException(status_code=500)
    
@policieRoutes.get("/{id}", status_code=status.HTTP_200_OK)
def getPolicie(id: UUID):
    policie = getPolicieById().run(id)
    if not policie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="policie not found")
    return policie

@policieRoutes.get("",status_code=status.HTTP_200_OK)
def getAll():
    allPolicies = getPolicies().run()
    return allPolicies