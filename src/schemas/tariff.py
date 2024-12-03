from datetime import datetime, date as date_

from pydantic import BaseModel, field_validator


class DateValidator(BaseModel):
    date: date_ | None = None

    __patterns__ = "%Y-%m-%d"

    @field_validator("date", mode="before")
    def validate_date(cls, v):
        if v is not None:
            if isinstance(v, str):
                try:
                    return datetime.strptime(v, cls.__patterns__).date()
                except ValueError:
                    raise ValueError(
                        f"Date does not match the pattern: {cls.__patterns__}"
                    )
        return v


class CostRequest(DateValidator):
    cargo_type: str
    value: float


class Tariff(DateValidator):
    cargo_type: str | None = None
    rate: float | None = None


class AddRequest(BaseModel):
    tariff: Tariff | list[Tariff]


class UpdateRequest(BaseModel):
    old_tariff: Tariff
    new_tariff: Tariff


class DeleteRequest(Tariff):
    pass


class CostResponse(BaseModel):
    cargo_type: str
    cost: float
