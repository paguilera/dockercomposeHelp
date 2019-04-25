from service import Service
import yaml
import os

# MODIFIES THE YAML DUMP FUNCTION, BETTER INDENTATION
class MyDumper(yaml.Dumper):

    def increase_indent(self, flow=False, indentless=False):
        return super(MyDumper, self).increase_indent(flow, False)

class Compose():
    """
    Services manages every service within a compose.
    """
    def __init__(self):
        self.compose = {'version': "3.7", 'services':{}}
        self.path = os.getcwd()

    # add service to compose
    def add_service(self, input):
        """
        Add a service into compose
        @type   service
        @param  service object
        """
        self.compose['services'].update(input.spit())

    # make compose file
    def make_compose(self, path=None):
        """
        create compose file in this directory
        @type string
        @param path to compose output location
        """
        if(path==None):
            path=self.path
        with open(path+'/docker-compose.yaml', 'w') as this_file:
            yaml.dump(self.compose, this_file, Dumper=MyDumper, default_flow_style=False)

if __name__ == "__main__":
    my_compose = Compose() #create a compose instance
    service_db = Service('db') #create and define service instance
    service_db.image('mysql:latest')
    service_db.command('--default-authentication-plugin=mysql_native_password')
    service_db.restart('always')
    service_db.environment({'MYSQL_ROOT_PASSWORD': 'example'})
    service_db.ports(['8080:8080'])

    my_compose.add_service(service_db) #add service to compose
    my_compose.make_compose() #output compose