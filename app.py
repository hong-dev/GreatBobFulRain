import config

from flask         import Flask
from flask_graphql import GraphQLView
from flask_cors    import CORS
from sqlalchemy    import create_engine

from api           import schema, get_services

def create_app():

    app = Flask(__name__)
    app.config['DEBUG'] = True
    CORS(app)

    db       = create_engine(config.DB_CONNECTION_URL)
    services = get_services(db)

    class ContextedView(GraphQLView):
        context_value = None

        def get_context(self):
            return services

    app.add_url_rule(
        '/graphql',
        view_func = ContextedView.as_view(
            'graphql',
            schema        = schema,
            graphiql      = True,
            context_value = {"services" : services}
        )
    )

    return app
