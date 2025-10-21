from repositories.factories import create_users_repository


def get_user_repository(route_handler_func):
    def wrapper(*args, **kwargs):
        user_repo = create_users_repository()
        return route_handler_func(user_repo, *args, **kwargs)
    return wrapper


def get_repository(repo_name):
    def decorator(route_handler_func):
        def wrapper(*args, **kwargs):
            if repo_name == 'user':
                repo = create_users_repository()
                return route_handler_func(repo, *args, **kwargs)
            raise ValueError('repository does not exist')
        return wrapper
    return decorator