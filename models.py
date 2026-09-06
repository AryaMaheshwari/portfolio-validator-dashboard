
from pydantic import BaseModel, Field, computed_field
from typing import List

class Holding(BaseModel):
    ticker: str = Field(min_length=1, max_length=6)
    shares: float = Field(gt=0)
    purchase_price: float = Field(gt=0)
    current_price: float = Field(gt=0)

    @computed_field
    @property
    def current_value(self) -> float:
        return round(self.shares * self.current_price, 2)

    @computed_field
    @property
    def gain_loss(self) -> float:
        cost_basis = self.shares * self.purchase_price
        return round(self.current_value - cost_basis, 2)

    @computed_field
    @property
    def gain_loss_percent(self) -> float:
        cost_basis = self.shares * self.purchase_price
        if cost_basis == 0:
            return 0.0
        return round((self.gain_loss / cost_basis) * 100, 2)


class Portfolio(BaseModel):
    holdings: List[Holding] = []

    @computed_field
    @property
    def total_value(self) -> float:
        return round(sum(h.current_value for h in self.holdings), 2)

    def allocation_by_ticker(self) -> dict:
        if self.total_value == 0:
            return {}
        return {
            h.ticker: round((h.current_value / self.total_value) * 100, 2)
            for h in self.holdings
        }
    