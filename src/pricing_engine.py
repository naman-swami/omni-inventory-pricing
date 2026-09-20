"""
Omni Inventory & Pricing Engine
Calculates price elasticity of demand and optimal reorder points.
"""
import math
from typing import Dict, Any

class InventoryPricingEngine:
    def calculate_price_elasticity(self, original_price: float, new_price: float, original_demand: float, new_demand: float) -> float:
        if original_price <= 0 or original_demand <= 0:
            return 0.0
        pct_price = (new_price - original_price) / original_price
        pct_demand = (new_demand - original_demand) / original_demand
        if pct_price == 0:
            return 0.0
        return round(pct_demand / pct_price, 2)

    def calculate_reorder_point(self, lead_time_days: int, avg_daily_demand: float, demand_std_dev: float, z_score: float = 1.96) -> Dict[str, Any]:
        safety_stock = round(z_score * demand_std_dev * math.sqrt(lead_time_days), 1)
        lead_time_demand = round(lead_time_days * avg_daily_demand, 1)
        reorder_point = round(lead_time_demand + safety_stock, 1)
        return {
            "lead_time_demand": lead_time_demand,
            "safety_stock": safety_stock,
            "reorder_point": reorder_point,
            "service_level_confidence": "97.5%"
        }
