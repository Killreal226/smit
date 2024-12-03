from typing import Annotated

from fastapi import APIRouter, Depends

from src.schemas import tariff
from src.broker.kafka import Kafka, get_broker
from src.controllers.manager import ServiceManager, get_service_manager


router = APIRouter(prefix="/v1/tariff", tags=["Tariff"])


@router.post("/get_cost")
async def get_cost(
    request: tariff.CostRequest,
    manager: Annotated[ServiceManager, Depends(get_service_manager)],
    broker: Annotated[Kafka, Depends(get_broker)]
) -> tariff.CostResponse:
    cost = await manager.tariff.get_cost(request)
    await broker.log_to_kafka("get_cost")
    return tariff.CostResponse(cargo_type=request.cargo_type, cost=cost)


@router.post("/add_tariff")
async def add_tariff(
    request: tariff.AddRequest,
    manager: Annotated[ServiceManager, Depends(get_service_manager)],
    broker: Annotated[Kafka, Depends(get_broker)]
) -> None:
    await manager.tariff.add_tariff(request)
    await broker.log_to_kafka("add_tariff")


@router.put("/update_tariff")
async def update_tariff(
    request: tariff.UpdateRequest,
    manager: Annotated[ServiceManager, Depends(get_service_manager)],
    broker: Annotated[Kafka, Depends(get_broker)]
) -> None:
    await manager.tariff.update_tariff(request)
    await broker.log_to_kafka("update_tariff")


@router.delete("/delete_tariff")
async def delete_tariff(
    request: tariff.DeleteRequest,
    manager: Annotated[ServiceManager, Depends(get_service_manager)],
    broker: Annotated[Kafka, Depends(get_broker)]
) -> None:
    await manager.tariff.delete_tariff(request)
    await broker.log_to_kafka("delete_tariff")
