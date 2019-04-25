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
    def make_compose(self, input=None):
        """
        create compose file in this directory
        @type string
        @param path to compose output location
        """
        if(input==None):
            input=self.path
        with open(input+'/docker-compose.yaml', 'w') as this_file:
            yaml.dump(self.compose, this_file, Dumper=MyDumper, default_flow_style=False)

if __name__ == "__main__":
    my_compose = Compose()
    service_reddit = Service('reddit')
    service_reddit.deploy.restart_policy.window('Yes')
    service_reddit.deploy.replicas(6)
    service_reddit.deploy.placement_constraints(['node.role == manager', 'engine.labels.operatingsystem == ubuntu 14.04'])
    my_compose.add_service(service_reddit)
    print(my_compose.compose)
    my_compose.make_compose()