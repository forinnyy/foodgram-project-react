from rest_framework import permissions


class SafeMethodOrAuthUserPermission(permissions.BasePermission):
    """Доступ пользователям при безопастном запросе
    или аутенфицированным."""

    pass


class AdminOrReadOnly(SafeMethodOrAuthUserPermission):
    """Доступ к объекту только с правами не ниже администратора."""

    pass


class OwnerOrReadOnly(SafeMethodOrAuthUserPermission):
    """Доступ к объекту только его создателю или администратору."""

    pass
