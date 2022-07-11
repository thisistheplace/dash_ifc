import dash
import dash_bootstrap_components as dbc

from .layout import IfcLayout

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
IfcLayout().apply_layout(app)