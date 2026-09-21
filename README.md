# Omni Inventory & Dynamic Pricing Engine

[![OpenGAP](https://img.shields.io/badge/OpenGAP-0.1.0-blue.svg)](agent.yaml)
[![Retail](https://img.shields.io/badge/Domain-Retail_E--Commerce_Pricing-teal.svg)](docs/retail_pricing_economics.md)
[![Economics](https://img.shields.io/badge/Model-Amoroso--Robinson_EOQ-blue.svg)](docs/retail_pricing_economics.md)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](requirements.txt)
[![CI](https://img.shields.io/badge/CI-Passing-brightgreen.svg)](.github/workflows/ci.yml)

An omnichannel retail inventory and dynamic pricing platform computing price elasticity markups, Wilson EOQ batches, and automated reorder points (ROP).

```
                    ┌─────────────────────────┐
                    │ SKU Cost & Demand Data  │
                    │ (Holding, Elasticity, D)│
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │ pricing/price_elasticity│
                    └────────────┬────────────┘
                                 │
                 ┌───────────────┴───────────────┐
                 ▼                               ▼
      ┌─────────────────────┐         ┌─────────────────────┐
      │ Optimal Price (P*)  │         │ Wilson EOQ & ROP    │
      │ P* = MC * (e/(1+e)) │         │  Batch Minimization │
      └──────────┬──────────┘         └──────────┬──────────┘
                 │                               │
                 └───────────────┬───────────────┘
                                 ▼
                    ┌─────────────────────────┐
                    │ Retail Execution Plan   │
                    │ (Target Price & Reorder)│
                    └─────────────────────────┘
```

## Features

- **Amoroso-Robinson Elasticity Pricing**: Dynamically calculates profit-maximizing price points.
- **Wilson EOQ Batch Sizing**: Minimizes the sum of inventory carrying and replenishment order costs.
- **SKU Catalog Grounding**: Includes benchmark consumer electronics SKU catalog.

## Directory Structure

```
omni-inventory-pricing/
├── agent.yaml                       # OpenGAP 0.1.0 Manifest
├── EXPLAINABILITY.md                # 7-checkpoint retail economics provenance
├── pricing/
│   └── price_elasticity_model.py    # Pricing and EOQ optimization engine
├── fixtures/
│   └── catalog/
│       └── sample_sku_catalog.json  # Benchmark retail product catalog
├── docs/
│   └── retail_pricing_economics.md  # Economic principles documentation
├── tests/
│   └── test_agent.py                # Pricing and inventory test suite
├── main.py                          # E-commerce CLI
└── requirements.txt
```

## Quick Start

```bash
# Run retail optimization tests
pytest tests/ -v

# Optimize sample SKU catalog
python main.py --demo
```
