from re import S
from dash import no_update, callback_context
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc

import time

from .app import app, cache
from .charts import radar_chart, histogram
from .constants import IFC_TYPES
from .fileutils import parse_contents
from .ifc import IfcFile


def get_ifc_data(session_id, ifc_data=None, delete=False):
    """ https://dash.plotly.com/sharing-data-between-callbacks """
    @cache.memoize()
    def query_and_serialize_data(session_id):
        ifc_file = IfcFile(ifc_data)
        return ifc_file.to_json()

    if delete:
        cache.delete_memoized(query_and_serialize_data, session_id)

    return IfcFile.from_json(query_and_serialize_data(session_id))

@app.callback(Output('confirm-upload', 'message'),
            Output('confirm-upload', 'displayed'),
            Output("ifc_viewer", "ifc_file_contents"),
            Output('data-updated', 'children'),
            Input('upload-data', 'contents'),
            Input('session-id', 'data'),
            State('upload-data', 'filename'),
            prevent_initial_call=True)
def update_output(file_contents, session_id, filename):
    try:
        ifc_data = parse_contents(file_contents, filename)
        # reset data in cache
        _ = get_ifc_data(session_id, ifc_data, True)
        return "", False, ifc_data, ""
    except Exception as e:
        raise e
        return str(e), True, no_update, no_update

@app.callback(Output('radar', 'figure'),
    Output("dropdown", "label"),
    Input('session-id', 'data'),
    Input('data-updated', 'children'),
    [Input(key.replace(" ", "_"), "n_clicks") for key in ["All"] + IFC_TYPES],
    prevent_initial_call=True)
def update_figure(session_id, upload_success, *args):
    ctx = callback_context

    if not ctx.triggered:
        button_id = "All"
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]
    if button_id == "data-updated":
        button_id = "All"
    
    # load ifc data
    tstart = time.time()
    ifc_file = get_ifc_data(session_id)

    if button_id != "All" and "OverallHeight" in ifc_file.get_product(button_id).columns.values:
        # scatter plot
        fig = histogram(ifc_file.get_product(button_id), "OverallHeight")
        return fig, button_id
    else:
        # radar plot
        fig = radar_chart(ifc_file.product_count)
        return fig, "All"