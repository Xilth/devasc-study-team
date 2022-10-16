import json
import yaml

with open('myfile.yaml', 'r') as yaml_file:
    ourYAML = yaml.safe_load(yaml_file)

print(ourYAML)

print("The access token is {}".format(ourYAML['access_token']))
print("The token expires in {}".format(ourYAML['expires_in'])+" seconds")

print("\n\n")
print(json.dumps(ourYAML, indent=4))