# Omni Inventory Pricing & Demand Optimization

> **Retail Economics & Microeconomic Optimization Platform**  
> Operationalizing Amoroso-Robinson Price Elasticity and Wilson Economic Order Quantity (EOQ).

---

### Mathematical Pricing Formulations

#### 1. Profit-Maximizing Optimal Price ($P^*$)
Given constant marginal cost $MC$ and own-price elasticity of demand $\epsilon_d = \frac{\% \Delta Q}{\% \Delta P}$:

$$P^* = MC \cdot \left( \frac{\epsilon_d}{1 + \epsilon_d} \right) \quad \text{for } \epsilon_d < -1$$

#### 2. Wilson Economic Order Quantity ($EOQ$)
Minimizes total annual inventory ordering and holding costs:

$$EOQ = \sqrt{\frac{2 \cdot D \cdot S}{H}}$$

Where $D$ is annual demand (units), $S$ is fixed order cost ($/order), and $H$ is unit holding cost ($/unit/year).

---

### SKU Optimization Simulation

| SKU ID | Product Category | Current Price | Elasticity ($\epsilon_d$) | Marginal Cost | Optimal Price ($P^*$) | Order Batch ($EOQ$) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **SKU-491** | Organic Espresso | $14.99 | $-2.20$ | $6.50 | **$11.92** | 450 units |
| **SKU-812** | Ceramic Pour-Over | $29.99 | $-1.15$ | $12.00 | **$34.50** | 120 units |
| **SKU-105** | Paper Filters (Pack)| $5.99 | $-0.65$ | $1.20 | Inelastic | 1,200 units |

---

### Retail Analytics CLI

```bash
# Simulate catalog price and reorder optimizations
python retail_pricing.py --demo

# Run retail economics unit tests
pytest tests/ -v
```

Catalog schemas, inventory thresholds, and pricing governance standards are published in [CATALOG_SPEC.md](CATALOG_SPEC.md).
