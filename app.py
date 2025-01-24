import dash #type: ignore
from layout import create_layout
from callbacks import register_callbacks

app = dash.Dash(__name__)

create_layout(app)


register_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True)
