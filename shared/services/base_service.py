class BaseService:
    """
    Base service for writing business logic over repositories.
    """
    def __init__(self, repository):
        self.repository = repository
