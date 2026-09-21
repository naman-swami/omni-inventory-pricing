"""
Retail Price Elasticity & Economic Order Quantity (EOQ) Engine
Calculates optimal revenue-maximizing pricing and Wilson EOQ reorder thresholds.
"""
import math
from typing import Dict, Any

class RetailAnalyticsEngine:
    @staticmethod
    def calculate_optimal_price(cost: float, elasticity: float) -> Dict[str, Any]:
        # Amoroso-Robinson optimal pricing formula: P* = Cost * (e / (e + 1))
        # Note: elasticity is negative for standard goods (e.g. -1.8)
        if elasticity >= -1.0:
            optimal_price = cost * 1.5 # Inelastic fallback markup
            markup = 0.50
        else:
            markup_multiplier = elasticity / (elasticity + 1.0)
            optimal_price = round(cost * markup_multiplier, 2)
            markup = round((optimal_price - cost) / cost, 2)

        return {
            "cost_usd": cost,
            "price_elasticity": elasticity,
            "optimal_price_usd": optimal_price,
            "recommended_markup_pct": round(markup * 100, 1)
        }

    @staticmethod
    def calculate_eoq_and_rop(
        annual_demand: int,
        order_cost: float,
        holding_cost: float,
        daily_demand: float,
        lead_time_days: int,
        safety_stock: int = 50
    ) -> Dict[str, Any]:
        # Wilson EOQ = sqrt(2 * D * S / H)
        eoq = math.isqrt(int((2 * annual_demand * order_cost) / max(0.1, holding_cost)))
        # Reorder Point (ROP) = d * L + SS
        rop = int(daily_demand * lead_time_days) + safety_stock

        return {
            "economic_order_quantity_units": eoq,
            "reorder_point_units": rop,
            "safety_stock_units": safety_stock
        }
