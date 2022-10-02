# Configure app.toml
# > snow login
# > snow configure
# Test locally
# > python app.py
# Create and deploy in snowflake:
# > snowcli procedure package
# > snowcli procedure create --environment dev
# > snowcli procedure call -f 'helloProcedure()'
import sys
from snowflake.snowpark import Session


def hello(session: Session) -> str:
    return 'Hello World!'


# For local debugging. Be aware you may need to type-convert arguments if you add input parameters
if __name__ == '__main__':
    from local_connection import get_dev_config
    print(get_dev_config('dev'))
    session = Session.builder.configs(get_dev_config('dev')).create()
    if len(sys.argv) > 1:
        print(hello(session, *sys.argv[1:]))  # type: ignore
    else:
        print(hello(session))  # type: ignore
    session.close()