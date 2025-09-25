SHOW TOPICS;

SET 'auto.offset.reset' = 'earliest';

-- all data
CREATE STREAM marketing_stream (
  name STRING,
  address STRING,
  email STRING,
  country STRING
) WITH (
  KAFKA_TOPIC = 'marketing',
  VALUE_FORMAT = 'JSON'
);

SELECT 
    * 
FROM 
    marketing_stream
EMIT 
    CHANGES;

SELECT 
    count(*) 
FROM 
    marketing_stream
GROUP BY 
    'dummy' 
EMIT 
    CHANGES;

