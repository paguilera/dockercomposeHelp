# class for different generating a single service
class Service():

    # subclass build
    class Build():
        # initializer
        def __init__(self):
            self.value = False

        # add context
        def context(self, location):
            self.value = True
            self.build = {'context':location}

        # add dockerfile
        def dockerfile(self, input):
            if(isinstance(input, str)):
                self.build['dockerfile'] = input
                return True
            else:
                raise Exception('{} -- is not a string'.format(input))

        # remove dockerfile
        def remove_dockerfile(self):
            if('dockerfile' not in self.build):
                raise Exception('build.dockerfile does not exist. Nothing to remove.')
            else:
                del self.build['shm_size']
                return True

        # add args
        def args(self, input):
            if(isinstance(input, list)):
                self.build['args'] = input
                return True
            else:
                raise Exception('{}\nis not a list'.format(input))

        # remove args
        def remove_args(self):
            if('args' not in self.build):
                raise Exception('build.args does not exist. Nothing to remove.')
            del self.build['args']
            return True

        # add cache_from
        def cache_from(self, input):
            if(isinstance(input, list)):
                self.build['cache_from'] = input
                return True
            else:
                raise Exception('{}\nis not a list'.format(input))

        # remove cache_from
        def remove_cache_from(self):
            if('cache_from' not in self.build):
                raise Exception('build.cache_from does not exist. Nothing to remove.')
            del self.build['cache_from']
            return True

        # add labels
        def labels(self, input):
            if(isinstance(input, list) or isinstance(input, dict)):
                self.build['labels'] = input
                return True
            else:
                raise Exception('{}\nis not a list or dict'.format(input))

        # remove labels
        def remove_labels(self):
            if('labels' not in self.build):
                raise Exception('build.labels does not exist. Nothing to remove.')
            del self.build['labels']
            return True

        # add wshm_size
        def shm_size(self, input):
            if(isinstance(input, int) or isinstance(input, str)):
                self.build['shm_size'] = input
                return True
            else:
                raise Exception('{} -- is not an integer'.format(input))

        # remove shm_size
        def remove_shm_size(self):
            if('shm_size' not in self.build):
                raise Exception('build.shm_size does not exist. Nothing to remove.')
            else:
                del self.build['shm_size']
                return True

        # add target
        def target(self, input):
            if(isinstance(input, str)):
                self.build['target'] = input
                return True
            else:
                raise Exception('{} -- is not a string'.format(input))

        # print service.build
        def print_build(self):
            print(self.build)

        #return self as dictionary
        def get_dict(self):
            return(dict(self.build))

    #initializer
    def __init__(self, name):
        self.name = name
        self.service = {name:{}}
        self.build = self.Build()
        self.service[self.name]['build'] = self.build

    # add cap
    def cap_add(self, input):
        if(isinstance(input, list)):
            self.service['cap_add'] = input
            return True
        else:
            raise Exception('{}\nis not a list'.format(input))

    # cap drop
    def cap_drop(self, input):
        if(isinstance(input, list)):
            self.service['cap_drop'] = input
            return True
        else:
            raise Exception('{}\nis not a list'.format(input))
    
    # add cgroup_parent
    def cgroup_parent(self, input):
        if(isinstance(input, str)):
            self.service['cgroup_parent'] = input
            return True
        else:
            raise Exception('{} -- is not a string'.format(input))
    
    # add command
    def command(self, input):
        if((isinstance(input, str)) or (isinstance(input, list))):
            self.service['command'] = input

    #prints service dictionary
    def print_service(self):
        # remove build if a context was never added.
        # this is a workaround for removing build in
        # case it is never used
        if(self.build.value == False):
            del self.service[self.name]['build']
        else:
            self.service[self.name]['build'] = self.build = self.build.get_dict()
        print(self.service)

