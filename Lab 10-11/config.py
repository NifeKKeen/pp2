from configparser import ConfigParser


def load_config(filename, section):
  parser = ConfigParser()
  parser.read(filename)

  config = {}
  if parser.has_section(section):
    params = parser.items(section)
    for param in params:
      config[param[0]] = param[1]
  else:
    raise Exception(f"Section {section} was not found in {filename} file")
  
  return config
