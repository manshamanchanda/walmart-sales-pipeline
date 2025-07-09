
## Walmart BI Project Overview

This project builds a dimensional data model for Walmart sales, implements SCD1 and SCD2 logics in DBT, and produces Tableau-ready datasets.

**Main Tables:**
- `walmart_store_dim`: SCD1
- `walmart_date_dim`: SCD1
- `walmart_fact_table`: SCD2 (versioned data)

**Outputs:**
- Dimension and Fact tables in Snowflake
- Python visualizations and Tableau dashboards
