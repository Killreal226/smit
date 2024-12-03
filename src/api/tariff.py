from typing import Annotated

from fastapi import APIRouter, Depends

from src.schemas import tariff
from src.controllers.manager import ServiceManager, get_service_manager


router = APIRouter(prefix="/v1/tariff", tags=["Tariff"])


@router.post("/get_cost")
async def get_cost(
    request: tariff.CostRequest,
    manager: Annotated[ServiceManager, Depends(get_service_manager)]
) -> tariff.CostResponse:
    cost = await manager.tariff.get_cost(request)
    return tariff.CostResponse(cargo_type=request.cargo_type, cost=cost)


@router.post("/add_tariff")
async def add_tariff(
    request: tariff.AddRequest,
    manager: Annotated[ServiceManager, Depends(get_service_manager)]
) -> None:
    await manager.tariff.add_tariff(request)


@router.put("/update_tariff")
async def update_tariff(
    request: tariff.UpdateRequest,
    manager: Annotated[ServiceManager, Depends(get_service_manager)]
) -> None:
    await manager.tariff.update_tariff(request)


@router.delete("/delete_tariff")
async def delete_tariff(
    request: tariff.DeleteRequest,
    manager: Annotated[ServiceManager, Depends(get_service_manager)]
) -> None:
    await manager.tariff.delete_tariff(request)
