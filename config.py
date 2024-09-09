DATABASE_CONFIG = {
    'dbname': 'bimbo',
    'user': 'pygreen',
    'password': 'icugr8xx14',
    'host': 'localhost',
    'port': 5432,
}
config_string = ' '.join(f'{key}={value}' for key, value in DATABASE_CONFIG.items())