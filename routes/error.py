"""
Le module routes.error contient les routes
relatives à la gestion des erreurs http.

"""

from state import *


@app.errorhandler(404)
def page_not_found(e): # Complexité temporelle totale : O(1)
    """Gère les erreurs 404.

    Args:
        e (Exception): l'erreur

    Returns:
        Any: redirige vers la page de 404
    """
    # Redirige vers la page 404
    return render_template("./errors/404.html"), 404 # O(1)


@app.errorhandler(500)
def server_error_page(e): # Complexité temporelle totale : O(1)
    """Gère les erreurs 500.

    Args:
        e (Exception): l'erreur qui est survenue

    Returns:
        Any: redirige vers la page 500
    """
    # Redirige vers la page 500
    return render_template("./errors/500.html"), 500 # O(1)
