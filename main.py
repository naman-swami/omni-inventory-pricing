import json
import argparse
from src.pricing_engine import InventoryPricingEngine

def main():
    parser = argparse.ArgumentParser(description="Omni Inventory Pricing CLI")
    parser.add_argument("--demo", action="store_true", help="Run simulated price elasticity & safety stock calculation")
    args = parser.parse_args()

    engine = InventoryPricingEngine()
    elasticity = engine.calculate_price_elasticity(original_price=100.0, new_price=110.0, original_demand=500, new_demand=420)
    reorder = engine.calculate_reorder_point(lead_time_days=7, avg_daily_demand=45.0, demand_std_dev=8.0)

    report = {
        "sku": "SKU-PREMIUM-JACKET",
        "price_elasticity": elasticity,
        "elasticity_nature": "ELASTIC" if abs(elasticity) > 1.0 else "INELASTIC",
        "inventory_reorder_profile": reorder
    }
    print("="*60)
    print(" OMNI INVENTORY PRICING & SAFETY STOCK AUDIT")
    print("="*60)
    print(json.dumps(report, indent=2))
    print("="*60)

if __name__ == "__main__":
    main()
