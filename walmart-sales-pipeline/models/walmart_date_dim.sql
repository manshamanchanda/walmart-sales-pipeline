
{{ config(materialized='incremental') }}

WITH source_data AS (
    SELECT
        date_id,
        store_date,
        isholiday,
        CURRENT_TIMESTAMP AS insert_date,
        CURRENT_TIMESTAMP AS update_date
    FROM {{ source('raw', 'date') }}
)

SELECT * FROM source_data
