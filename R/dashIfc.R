# AUTO GENERATED FILE - DO NOT EDIT

#' @export
dashIfc <- function(id=NULL, url=NULL) {
    
    props <- list(id=id, url=url)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DashIfc',
        namespace = 'dash_ifc',
        propNames = c('id', 'url'),
        package = 'dashIfc'
        )

    structure(component, class = c('dash_component', 'list'))
}
