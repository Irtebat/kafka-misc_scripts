import os

def getAdminConfig() -> dict: 
    """ Return the admin config """ 
     
    import configparser
    import socket
    
    # Create a ConfigParser object
    config = configparser.ConfigParser()

    # Read the properties file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    admin_config_filepath = os.path.join(script_dir, 'admin-config.ini')
    config.read(admin_config_filepath)

    # Load the configuration into a dictionary
    admin_config = {
        'bootstrap.servers': config.get('default', 'bootstrap.servers'),
        'security.protocol': config.get('default', 'security.protocol'),
        'sasl.mechanism': config.get('default', 'sasl.mechanism'),
        'sasl.username': config.get('default', 'sasl.username'),
        'sasl.password': config.get('default', 'sasl.password'),
        'client.id': socket.gethostname(),
    }
    
    return admin_config
