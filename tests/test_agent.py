import os
import pytest
from pricing.price_elasticity_model import RetailAnalyticsEngine

def test_optimal_pricing_elastic():
    res = RetailAnalyticsEngine.calculate_optimal_price(cost=50.0, elasticity=-2.0)
    # P* = 50 * (-2 / (-2 + 1)) = 50 * 2 = 100.0
    assert res["optimal_price_usd"] == 100.0
    assert res["recommended_markup_pct"] == 100.0

def test_eoq_calculation():
    res = RetailAnalyticsEngine.calculate_eoq_and_rop(
        annual_demand=10000, order_cost=50.0, holding_cost=4.0, daily_demand=30, lead_time_days=10
    )
    # EOQ = sqrt(2 * 10000 * 50 / 4) = sqrt(250000) = 500
    assert res["economic_order_quantity_units"] == 500
    # ROP = 30 * 10 + 50 = 350
    assert res["reorder_point_units"] == 350
