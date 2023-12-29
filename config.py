class Config:
    """
    Base configuration class with common settings.
    """

    DEBUG = False
    TESTING = False
    SECRET_KEY = "elbEJ80libKieSGezAFD9Mvsf69XzQkv8oE9vB9K"  # nosec - ✅ example
    # https://bandit.readthedocs.io/en/latest/config.html#exclusions


class DevelopmentConfig(Config):
    """
    Configuration for Development environment.
    """

    DEBUG = True
    # Other development-specific settings


class TestingConfig(Config):
    """
    Configuration for Testing environment.
    """

    TESTING = True
    # Other test-specific settings


class ProductionConfig(Config):
    """
    Configuration for Production environment.
    """

    # Production-specific settings like database URI
