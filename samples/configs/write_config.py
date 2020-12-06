from configparser import ConfigParser

# Initialize the Parser.
config = ConfigParser()

# Add the Section.
config.add_section('graph_api')

# Set the Values.
config.set('graph_api', 'client_id', '976cc237-b711-47f9-980c-4f12b6fb5d96')
config.set('graph_api', 'client_secret', '6zdc326a39s4KWg9SjMV~Rci2~wO-U.vYn')
config.set('graph_api', 'redirect_uri', 'https://localhost/todo_login')

# Write the file.
with open(file='samples/configs/config.ini', mode='w+') as f:
    config.write(f)
