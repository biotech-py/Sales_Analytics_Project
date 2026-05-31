# %% [markdown]
# # Sales Analytics Project
# 
# ## 1. Data Loading and Initial Inspection
# 
# This project analyzes retail sales data to identify revenue trends, customer behavior, product performance, and business insights.

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %%
df = pd.read_csv("../DATA/Superstore.csv")

# %%
df.head()

# %%
df.shape

# %%
df.info()

# %%
df.describe()

# %%
df.isnull().sum()

# %% [markdown]
# ## 2. Data Understanding and Quality Assessment
# 
# ### Dataset Summary
# 
# The dataset contains 9,994 retail transactions and 21 variables related to orders, customers, products, sales, discounts, and profit.
# 
# ### Data Quality Findings
# 
# - No missing values were detected.
# - Sales and profit are continuous numerical variables.
# - The dataset contains customer, product, geographical, and transactional information.
# - The dataset is suitable for business analytics and performance evaluation.

# %% [markdown]
# ## 3. Revenue Analysis

# %%
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
avg_sales = df["Sales"].mean()
orders = df["Order ID"].nunique()

print(f"Total Revenue: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Average Sales per Transaction: ${avg_sales:,.2f}")
print(f"Unique Orders: {orders:,}")

# %% [markdown]
# ### Revenue Overview
# 
# The company generated a total revenue of $2.30 million and a total profit of $286.40 thousand.
# 
# The average sales value per transaction was approximately $229.86.
# 
# A total of 5,009 unique orders were recorded in the dataset.
# 
# These figures indicate strong business activity and provide a solid foundation for further analysis of products, customers, and regional performance.

# %% [markdown]
# ## 4. Revenue by Category Analysis

# %%
category_sales = df.groupby("Category")["Sales"].sum().sort_values()

category_sales

# %%
category_sales.plot(kind="bar")

plt.title("Revenue by Category")
plt.ylabel("Revenue")

plt.savefig("../OUTPUTS/revenue_by_category.png")

plt.show()

# %% [markdown]
# ### Revenue by Category
# 
# This analysis evaluates the contribution of each product category to overall revenue generation.
# 
# The comparison helps identify which categories drive the largest share of company sales.

# %%
(category_sales / category_sales.sum() * 100).round(2)

# %% [markdown]
# ### Revenue by Category Findings
# 
# Technology generated the highest revenue among all product categories, contributing approximately one-third of total company sales.
# 
# Furniture ranked second in revenue generation, while Office Supplies contributed the lowest revenue.
# 
# The relatively balanced revenue distribution suggests that the business does not rely heavily on a single category, although Technology appears to be the strongest revenue driver.

# %% [markdown]
# ## 5. Profit Analysis

# %%
category_profit = df.groupby("Category")["Profit"].sum().sort_values()

category_profit

# %%
category_profit.plot(kind="bar")

plt.title("Profit by Category")
plt.ylabel("Profit")

plt.savefig("../OUTPUTS/profit_by_category.png")

plt.show()

# %%
profit_margin = (
    df.groupby("Category")["Profit"].sum()
    /
    df.groupby("Category")["Sales"].sum()
) * 100

profit_margin.round(2)

# %% [markdown]
# ### Profit Analysis Findings
# 
# Technology generated the highest profit among all categories, contributing approximately $145,455 to overall company profitability.
# 
# Office Supplies ranked second with a profit of approximately $122,491, while Furniture generated only $18,452 despite contributing substantial revenue.
# 
# The large gap between Furniture revenue and profit suggests that this category operates with significantly lower margins compared to the other categories.

# %% [markdown]
# ### Profit Margin Findings
# 
# Technology achieved the highest profit margin at approximately 17.4%, closely followed by Office Supplies at 17.0%.
# 
# Furniture showed a very low profit margin of only 2.5%, indicating that a large portion of its revenue is consumed by operational costs, discounts, or lower markups.
# 
# Although Furniture contributes significantly to revenue, it is considerably less efficient in generating profit compared to Technology and Office Supplies.

# %% [markdown]
# ### Business Recommendation
# 
# Technology should remain a strategic focus area due to its strong performance in both revenue generation and profitability.
# 
# Office Supplies demonstrates healthy profitability and represents a stable source of business income.
# 
# Furniture requires further investigation to identify factors affecting profitability, such as excessive discounting, high procurement costs, or inefficient pricing strategies.

# %% [markdown]
# ## 6. Regional Sales Analysis

# %%
region_sales = df.groupby("Region")["Sales"].sum().sort_values()

region_sales

# %%
region_sales.plot(kind="bar")

plt.title("Revenue by Region")
plt.ylabel("Revenue")

plt.savefig("../OUTPUTS/revenue_by_region.png")

plt.show()

# %% [markdown]
# ### Regional Revenue Findings
# 
# The West region generated the highest revenue, contributing approximately $725,458 in sales.
# 
# The East region ranked second with total sales of approximately $678,781.
# 
# The Central region generated moderate revenue of approximately $501,240, while the South region recorded the lowest sales at approximately $391,722.
# 
# The substantial gap between the West and South regions indicates significant differences in market performance across geographical areas.

# %% [markdown]
# ### Business Insights
# 
# The West region appears to be the company's strongest market and should remain a key focus for future growth initiatives.
# 
# The East region also demonstrates strong performance and represents another major revenue contributor.
# 
# The South region presents an opportunity for business expansion, as its revenue is considerably lower than the other regions.
# 
# Further investigation into customer demand, product mix, and marketing effectiveness across regions may help explain these performance differences.

# %% [markdown]
# ## 7. Top Performing States

# %%
state_sales = (
    df.groupby("State")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

state_sales

# %%
state_sales.plot(kind="bar")

plt.title("Top 10 States by Revenue")
plt.ylabel("Revenue")

plt.savefig("../OUTPUTS/top_10_states_revenue.png")

plt.show()

# %% [markdown]
# ### Top States Revenue Findings
# 
# California generated the highest revenue, contributing approximately $457,688 in sales.
# 
# New York ranked second with approximately $310,877 in revenue, while Texas occupied the third position with approximately $170,188.
# 
# California's revenue is significantly higher than all other states, indicating that it is the company's most important market.
# 
# The top three states contribute a substantial share of total company revenue and should be considered strategic markets.

# %% [markdown]
# ### Business Insights
# 
# California should remain a primary focus area for customer retention and business expansion strategies.
# 
# New York demonstrates strong sales performance and represents another major revenue-generating market.
# 
# States with lower revenue among the top ten, such as Virginia and Michigan, may offer opportunities for targeted marketing campaigns and customer acquisition initiatives.
# 
# Understanding the factors driving California's exceptional performance could help replicate similar success in other states.

# %% [markdown]
# ## 8. Customer Analysis

# %%
top_customers = (
    df.groupby("Customer Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

top_customers

# %%
top_customers.plot(kind="bar")

plt.title("Top 10 Customers by Revenue")
plt.ylabel("Revenue")

plt.savefig("../OUTPUTS/top_customers_revenue.png")

plt.show()

# %%
top_customers.sum() / df["Sales"].sum() * 100

# %% [markdown]
# ### Top Customer Findings
# 
# Sean Miller was the highest revenue-generating customer, contributing approximately $25,043 in sales.
# 
# Tamara Chand ranked second with approximately $19,652 in revenue, followed by Raymond Buch with approximately $15,177.
# 
# The top ten customers collectively generated approximately 6.70% of total company revenue.
# 
# This indicates that company revenue is not heavily dependent on a small number of customers and is instead distributed across a broad customer base.

# %% [markdown]
# ### Customer Insights
# 
# The relatively low contribution of the top ten customers suggests a diversified customer portfolio, reducing revenue concentration risk.
# 
# Maintaining strong relationships with high-value customers remains important, as they contribute significantly more revenue than the average customer.
# 
# Customer retention programs targeting top-performing customers may further increase long-term revenue and profitability.

# %% [markdown]
# ## 9. Product Analysis

# %%
top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

top_products

# %%
top_products.plot(kind="bar")

plt.title("Top 10 Products by Revenue")
plt.ylabel("Revenue")

plt.savefig("../OUTPUTS/top_products_revenue.png")

plt.show()

# %%
top_products.sum() / df["Sales"].sum() * 100

# %% [markdown]
# ### Product Revenue Findings
# 
# The Canon imageCLASS 2200 Advanced Copier generated the highest revenue among all products, contributing approximately $61,600 in sales.
# 
# The second-highest revenue-generating product was the Fellowes PB500 Electric Punch Plastic Comb Binding Machine, generating approximately $27,453 in revenue.
# 
# The top ten products collectively contributed approximately 10.65% of total company revenue.
# 
# This indicates that a relatively small number of products generate a significant share of sales, highlighting the importance of monitoring top-performing products.

# %% [markdown]
# ### Product Insights
# 
# The Canon imageCLASS 2200 Advanced Copier significantly outperformed all other products, generating more than double the revenue of the second-ranked product.
# 
# The company's revenue appears to be partially concentrated among a small set of high-performing products.
# 
# Inventory management and marketing efforts should prioritize these top-performing products to maximize revenue generation.
# 
# Further analysis of profit margins for these products would help determine whether high sales are also translating into high profitability.

# %% [markdown]
# ## 10. Discount vs Profit Analysis

# %%
plt.figure(figsize=(8,5))

plt.scatter(df["Discount"], df["Profit"])

plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")

plt.savefig("../OUTPUTS/discount_vs_profit.png")

plt.show()

# %%
df[["Discount","Profit"]].corr()

# %% [markdown]
# ### Discount vs Profit Findings
# 
# The correlation between Discount and Profit is approximately -0.22, indicating a weak-to-moderate negative relationship.
# 
# The scatter plot shows that transactions with higher discounts are more likely to generate lower profits and, in some cases, substantial losses.
# 
# Most highly profitable transactions occur at low or zero discount levels, whereas heavily discounted transactions are frequently associated with reduced profitability.
# 
# These findings suggest that aggressive discounting may negatively impact overall business performance.

# %% [markdown]
# ### Business Insights
# 
# The company should carefully evaluate discount strategies to ensure that revenue growth does not come at the expense of profitability.
# 
# High-discount transactions should be monitored to identify products or customer segments that consistently generate losses.
# 
# A more targeted discounting approach may improve profit margins while maintaining competitive pricing.
# 
# Balancing customer acquisition incentives with profitability objectives is essential for long-term business success.

# %% [markdown]
# # 11. Key Business Recommendations

# %% [markdown]
# ## Key Business Recommendations
# 
# ### 1. Focus on High-Performing Regions
# 
# The West and East regions generate the highest revenue and should remain priority markets for expansion and customer retention initiatives.
# 
# ### 2. Strengthen Top Product Categories
# 
# Technology consistently demonstrates strong revenue and profitability performance and should remain a strategic focus area.
# 
# ### 3. Improve Furniture Profitability
# 
# Although Furniture contributes significant revenue, its profit margin is substantially lower than other categories. Pricing and discount strategies should be reviewed.
# 
# ### 4. Retain High-Value Customers
# 
# Top customers contribute a meaningful share of revenue. Targeted loyalty programs and customer engagement initiatives may improve retention.
# 
# ### 5. Optimize Discount Strategies
# 
# Higher discounts are associated with lower profits. Discount policies should be carefully evaluated to avoid unnecessary profit erosion.
# 
# ### 6. Expand Low-Performing Markets
# 
# The South region presents opportunities for revenue growth through targeted marketing and sales initiatives.

# %% [markdown]
# # 12. Project Conclusion

# %% [markdown]
# ## Conclusion
# 
# This project analyzed approximately 10,000 retail transactions to identify sales trends, profitability drivers, customer behavior patterns, and regional performance differences.
# 
# Key findings revealed that Technology is the most profitable category, the West region generates the highest revenue, and a small group of products contributes significantly to overall sales performance.
# 
# Customer revenue is relatively diversified, reducing dependency on a small number of buyers. However, discounting practices show a negative impact on profitability and should be carefully managed.
# 
# The analysis demonstrates how data analytics can support business decision-making by uncovering actionable insights related to revenue growth, profitability improvement, customer management, and market expansion.


