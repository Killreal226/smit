from src.db.dao import TariffDAO
from src.broker.kafka import Kafka
from src.schemas.tariff import \
    UpdateRequest, CostRequest, DeleteRequest, AddRequest


class TariffController:
    def __init__(self):
        self._dao = TariffDAO
        self._broker = Kafka

    async def get_cost(self, request: CostRequest) -> float:
        if request.date:
            record = await self._dao.select_one_filter(
                cargo_type=request.cargo_type, date=request.date
            )
        else:
            record = await self._dao.select_latest_tariff(
                cargo_type=request.cargo_type
            )
        if record:
            return record.rate * request.value
        return 0

    async def update_tariff(self, request: UpdateRequest) -> None:
        await self._dao.update_filter(
            update_values=request.new_tariff.model_dump(),
            **request.old_tariff.model_dump()
        )

    async def delete_tariff(self, request: DeleteRequest) -> None:
        await self._dao.delete_filter(**request.model_dump())

    async def add_tariff(self, request: AddRequest) -> None:
        if isinstance(request.tariff, list):
            tariffes = [item.model_dump() for item in request.tariff]
            await self._dao.add_many(*tariffes)
        else:
            await self._dao.add_one(**request.tariff.model_dump())
        await self._broker.log_to_kafka()
