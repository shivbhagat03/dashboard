import dash #type: ignore
from layout import create_layout
from callbacks import register_callbacks

# Initialize the Dash app
app = dash.Dash(__name__)

# Create the layout
create_layout(app)

# Register callbacks
register_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True)