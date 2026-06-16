from rest_framework.permissions import BasePermission, SAFE_METHODS


class ReadOnlyOrOAuth2WriteScope(BasePermission):
    """
    Permite consultar con GET sin autenticación.
    Exige token OAuth2 válido con scope 'write' para POST, PUT, PATCH y DELETE.
    """

    message = (
        "Para crear, actualizar o eliminar debes enviar un token OAuth2 "
        "válido con scope write."
    )

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        token = getattr(request, 'auth', None)
        user = getattr(request, 'user', None)

        if not token or not user or not user.is_authenticated:
            return False

        allow_scopes = getattr(token, 'allow_scopes', None)

        if callable(allow_scopes):
            return token.allow_scopes(['write'])

        scope = getattr(token, 'scope', '')
        return 'write' in str(scope).split()