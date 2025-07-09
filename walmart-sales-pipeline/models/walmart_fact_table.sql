
{{ config(materialized='incremental') }}

WITH source_data AS (
    SELECT
        date_id,
        store_id,
        dept_id,
        store_weekly_sales,
        fuel_price,
        store_temperature,
        unemployement,
        cpi,
        markdown1,
        markdown2,
        markdown3,
        markdown4,
        markdown5,
        CURRENT_TIMESTAMP AS insert_date,
        CURRENT_TIMESTAMP AS update_date,
        CURRENT_TIMESTAMP AS vrsn_start_date,
        NULL AS vrsn_end_date
    FROM {{ source('raw', 'sales') }}
)

SELECT * FROM source_data
