from trino.exceptions import (  # noqa
    TrinoQueryError,
    TrinoUserError,
    TrinoExternalError,
    TrinoInternalError
)

# ref: https://github.com/trinodb/trino/blob/master/core/trino-spi/src/main/java/io/trino/spi/StandardErrorCode.java
NOT_FOUND = 'NOT_FOUND'
COLUMN_NOT_FOUND = 'COLUMN_NOT_FOUND'
TABLE_NOT_FOUND = 'TABLE_NOT_FOUND'
SCHEMA_NOT_FOUND = 'SCHEMA_NOT_FOUND'
CATALOG_NOT_FOUND = 'CATALOG_NOT_FOUND'
FUNCTION_NOT_FOUND= 'FUNCTION_NOT_FOUND'
NOT_SUPPORTED = 'NOT_SUPPORTED'

MISSING_TABLE = 'MISSING_TABLE'
MISSING_COLUMN_NAME = 'MISSING_COLUMN_NAME'
MISSING_SCHEMA_NAME = 'MISSING_SCHEMA_NAME'
MISSING_CATALOG_NAME = 'MISSING_CATALOG_NAME'
