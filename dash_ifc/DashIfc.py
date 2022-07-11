# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashIfc(Component):
    """A DashIfc component.


Keyword arguments:

- id (string; optional):
    The ID used to identify the container for the IFC viewer
    component.

- url (string; required):
    The url for where the IFC file is hosted."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_ifc'
    _type = 'DashIfc'
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, url=Component.REQUIRED, **kwargs):
        self._prop_names = ['id', 'url']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'url']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in ['url']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(DashIfc, self).__init__(**args)
