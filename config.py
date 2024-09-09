DATABASE_CONFIG = {
    'dbname': '',
    'user': '',
    'password': '',
    'host': '',
    'port': 5432,
}
config_string = ' '.join(f'{key}={value}' for key, value in DATABASE_CONFIG.items())