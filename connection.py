import os
from sqlalchemy import create_engine
import dotenv
dotenv.load_dotenv()


account_identifier = os.environ['SF_ACCOUNT_IDENTIFIER']
user = os.environ['SF_USER']
password = os.environ['SF_PASSWORD']
database= os.environ['SF_DATABASE']
schema = os.environ['SF_SCHEMA']
warehouse = os.environ['SF_WAREHOUSE']
role = os.environ['SF_ROLE']

engine = create_engine(
    'snowflake://{user}:{password}@{account_identifier}/'.format(
        user=user,
        password=password,
        account_identifier=account_identifier,
    )
)
try:
    connection = engine.connect()
    # results = connection.execute('select current_version()').fetchone()
    # print(results[0])
finally:
    connection.close()
    engine.dispose()