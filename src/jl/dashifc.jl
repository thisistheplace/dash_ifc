# AUTO GENERATED FILE - DO NOT EDIT

export dashifc

"""
    dashifc(;kwargs...)

A DashIfc component.

Keyword arguments:
- `id` (String; optional): The ID used to identify the container for the IFC viewer component.
- `url` (String; required): The url for where the IFC file is hosted.
"""
function dashifc(; kwargs...)
        available_props = Symbol[:id, :url]
        wild_props = Symbol[]
        return Component("dashifc", "DashIfc", "dash_ifc", available_props, wild_props; kwargs...)
end

