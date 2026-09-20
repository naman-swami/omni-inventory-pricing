import pytest
from src.pricing_engine import InventoryPricingEngine

def test_elasticity_computation():
    engine = InventoryPricingEngine()
    # 10% price hike led to 16% demand drop -> -1.6
    e = engine.calculate_price_elasticity(100.0, 110.0, 500, 420)
    assert e == -1.6

def test_reorder_point_positive():
    engine = InventoryPricingEngine()
    r = engine.calculate_reorder_point(lead_time_days=7, avg_daily_demand=30.0, demand_std_dev=5.0)
    assert r["reorder_point"] > r["lead_time_demand"]
