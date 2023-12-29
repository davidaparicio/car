class Config:
    """
    Base configuration class with common settings.
    """

    DEBUG = False
    TESTING = False


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
