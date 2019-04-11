
# class for different generating a single service
class Services():
    #initializer
    def __init__(self, name):
        self.name = name
        self.service = {name:{}}

    #add build to compose
    def add_build(self, location):
        self.build = {}
        self.service[self.name]['build'] = self.build
        self.build['context'] = location
        return True

    def remove_build(self):
        if('build' not in self.service):
            raise Exception('{}.build does not exist. Nothing to remove.'.format(self.name))
        del self.service[self.name]['build']
        return True

    #add args to build
    def add_build_args(self, list_input):
        if(isinstance(list_input, list)):
            self.build['args'] = list_input
            return True
        else:
            raise Exception('{}\nis not a list'.format(list_input))

    #remove arguments from build
    def remove_build_args(self):
        if('args' not in self.build):
            raise Exception('{}.build.args does not exist. Nothing to remove.'.format(self.name))
        del self.build['args']
        return True

    #add cache_from to build
    def add_build_cache_from(self, list_input):
        if(isinstance(list_input, list)):
            self.build['cache_from'] = list_input
            return True
        else:
            raise Exception('{}\nis not a list'.format(list_input))

    #remove cache_from from build
    def remove_build_cache_from(self):
        if('cache_from' not in self.build):
            raise Exception('{}.build.cache_from does not exist. Nothing to remove.'.format(self.name))
        del self.build['cache_from']
        return True


    #prints service dictionary
    def print_service(self):
        print(self.service)

if __name__ == "__main__":
    x = Services("test")
    #x.remove_build()
    x.add_build("www.docker-hub.com/DC-wrapper")
    #x.remove_build_args()
    x.add_build_args(["arg0", "arg1", "arg2"])
    #x.remove_build_cache_from()
    x.add_build_cache_from(["buildno", "gitcommithash"])
    #x.remove_build_cache_from()

    x.print_service()