from typing import List
from fastapi import APIRouter, status, HTTPException, Response
from uuid import UUID
from src.Context.Http.schemas.policiesPayload import createPolicie, Policie, policieStatus
from src.App.Policies.addPolicie import addPolicie
from src.App.Policies.getPolicie import getPolicieById
from src.App.Policies.getPolicies import getPolicies
from src.App.Policies.changeStatus import changeStatusPolicie

policieRoutes = APIRouter()

def validateInternalErrors(result):
    if not "code" in result:
        return False
    if result.code == 5001:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result.get("message"))
    if result.code == 5004:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=result.get("message"))
    
    return True


@policieRoutes.post("", status_code=status.HTTP_201_CREATED, response_model=Policie)
def postPolicie(policie: createPolicie):
    result = addPolicie().run(policie)
    print('routes ',result)
    if "code" in result:
        raise HTTPException(status_code=400, detail=result.get("message"))
    return result
    
@policieRoutes.get("/{id}", status_code=status.HTTP_200_OK)
def getPolicie(id: UUID):
    policie = getPolicieById().run(id)
    if not policie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="policie not found")
    return policie

@policieRoutes.get("",status_code=status.HTTP_200_OK, response_model=List[Policie])
def getAll():
    allPolicies = getPolicies().run()
    return allPolicies

@policieRoutes.put("/{id}/status")
def putChangeStatus(id:UUID, state: policieStatus | None = None):
    policie = changeStatusPolicie().run(id, state)