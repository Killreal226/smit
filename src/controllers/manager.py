from src.controllers.tariff import TariffController


class ServiceManager(object):
    tariff: TariffController

    def __init__(self):
        self.tariff = TariffController()


async def get_service_manager() -> ServiceManager:
    return ServiceManager()
