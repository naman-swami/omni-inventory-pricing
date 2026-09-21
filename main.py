import argparse
import json
import os
from pricing.price_elasticity_model import RetailAnalyticsEngine

def main():
    parser = argparse.ArgumentParser(description="Omni Inventory Pricing CLI")
    parser.add_argument("--demo", action="store_true", help="Audit sample retail catalog")
    args = parser.parse_args()

    data_file = os.path.join(os.path.dirname(__file__), "fixtures", "catalog", "sample_sku_catalog.json")

    if args.demo:
        with open(data_file, "r") as f:
            items = json.load(f)
        print("=== OMNI RETAIL PRICING & INVENTORY AUDIT ===\n")
        for it in items:
            price_res = RetailAnalyticsEngine.calculate_optimal_price(it["cost_usd"], it["elasticity"])
            eoq_res = RetailAnalyticsEngine.calculate_eoq_and_rop(
                it["annual_demand_units"], it["order_cost_usd"], it["holding_cost_annual_usd"],
                it["daily_demand_units"], it["lead_time_days"]
            )
            print(f"SKU: {it['sku']} ({it['name']})")
            print(f"  Cost: ${it['cost_usd']} | Current Price: ${it['current_price_usd']} | Optimal Price: ${price_res['optimal_price_usd']}")
            print(f"  Recommended Markup: {price_res['recommended_markup_pct']}% (Elasticity: {it['elasticity']})")
            print(f"  Economic Order Quantity (EOQ): {eoq_res['economic_order_quantity_units']} units")
            print(f"  Reorder Point (ROP): {eoq_res['reorder_point_units']} units (Safety Stock: {eoq_res['safety_stock_units']})")
            print("-" * 50)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
