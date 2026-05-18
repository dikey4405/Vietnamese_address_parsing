from configparser import ConfigParser

def load_mssql_config(file_name='D:\\DS108\\source_code\\mssql.ini', section='mssql'):
    parser = ConfigParser()
    parser.read(file_name)

    config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} not found in the {file_name} file')
    
    return config

if __name__ == '__main__':
    pass
