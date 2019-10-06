import flask
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.graph_objs as gobs

external_stylesheets = ['https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css']


external_scripts = ['https://code.jquery.com/jquery-3.2.1.slim.min.js',
                    'https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js',
                    'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js']

# Server definition

server = flask.Flask(__name__)
app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets,
                external_scripts=external_scripts,
                server=server)

# HEADER
# ======

header = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Page 1", href="#")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("Page 2", href="#"),
                dbc.DropdownMenuItem("Page 3", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="{{cookiecutter.project_name}}",
    brand_href="#",
    color="primary",
    dark=True
)


# COMPONENTS
# ==========

# Your components go here.


# INTERACTION
# ===========

# Your interaction goes here.


# APP LAYOUT
# ==========

app.layout = html.Div([
    header
])

if __name__ == '__main__':
    app.run_server(debug=True)