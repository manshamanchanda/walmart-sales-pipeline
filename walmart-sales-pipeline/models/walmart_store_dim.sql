
{{ config(materialized='incremental') }}

WITH source_data AS (
    SELECT
        store_id,
        dept_id,
        store_type,
        store_size,
        CURRENT_TIMESTAMP AS insert_date,
        CURRENT_TIMESTAMP AS update_date
    FROM {{ source('raw', 'store') }}
)

SELECT * FROM source_data
