import dash_ifc
import dash
from dash import html
import dash_bootstrap_components as dbc

from ifcdashboard.fileutils import read_file

class IfcLayout:
    
    def __init__(self):
        self._layout = self.setup_layout()

    def apply_layout(self, app: dash.Dash) -> None:
        """
        Apply layout to app

        Args:
            app (dash.App): app object to apply layout to
        """
        app.layout = self._layout


    def setup_layout(self) -> dbc.Container:
        layout = dbc.Container([

            dbc.Row([
                dbc.Col(html.Div("Dash IFC viewer")),
                dbc.Col(html.Div("IFC viewer")),
            ]),
            dbc.Row([
                dbc.Col(html.Div("User inputs go here")),
                dbc.Col(dash_ifc.DashIfc("ifc_viewer", read_file("test.ifc"))),
            ])

        ])
        return layout
