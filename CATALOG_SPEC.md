# Retail Product Catalog Specification & Inventory Economics

## 1. Catalog Data Architecture & Standards
Omni Inventory Pricing operates on enterprise retail catalog datasets conforming to:
- **GS1 Global Data Synchronization Network (GDSN)**
- **ISO/IEC 15459 (Unique identification of retail consumer items / UPC-A and EAN-13)**
- **ASC X12 EDI 888 (Item Maintenance) & EDI 879 (Pricing Information)**

---

## 2. Microeconomic Pricing Formulations

### A. Profit-Maximizing Optimal Price ($P^*$)
Based on the Amoroso-Robinson relation linking marginal revenue ($MR$) to own-price elasticity of demand ($\epsilon_d$):

$$MR = P \left( 1 + \frac{1}{\epsilon_d} \right)$$

Setting $MR = MC$ (Marginal Cost) yields the profit-maximizing price for elastic goods ($\epsilon_d < -1$):

$$P^* = MC \cdot \left( \frac{\epsilon_d}{1 + \epsilon_d} \right)$$

- *Markup Multiplier*: $m = \frac{\epsilon_d}{1 + \epsilon_d}$.
- For products with $\epsilon_d = -2.0$, optimal markup is $2.0\times MC$ ($100\%$ markup on cost).

### B. Cross-Price Elasticity of Demand ($\epsilon_{ij}$)
Measures demand substitution between product $i$ and related competitor or private-label product $j$:

$$\epsilon_{ij} = \frac{\% \Delta Q_i}{\% \Delta P_j}$$

- $\epsilon_{ij} > 0$: Substitute goods (a price hike in brand $j$ increases demand for store brand $i$).
- $\epsilon_{ij} < 0$: Complementary goods (a price hike in coffee decreases demand for coffee filters).

---

## 3. Wilson Economic Order Quantity (EOQ) & Inventory Carrying Costs
To minimize total annual inventory holding and ordering expenditures:

$$EOQ = \sqrt{\frac{2 \cdot D \cdot S}{H}}$$

Where:
- $D$: Annual demand volume ($	ext{units/year}$).
- $S$: Fixed administrative and logistics cost per purchase order ($\$/	ext{order}$).
- $H$: Unit inventory holding cost per year ($\$/	ext{unit/year}$), calculated as $H = i \cdot C$, where $i$ is the cost of capital plus warehouse shrinkage ($\sim 20-25\%$) and $C$ is unit purchase cost.

### Safety Stock ($SS$) Calculation:
$$SS = Z_{\alpha} \cdot \sigma_L$$
Where $Z_{\alpha}$ is the service level factor ($Z_{0.95} = 1.645$ for $95\%$ in-stock probability) and $\sigma_L$ is the standard deviation of lead-time demand.
