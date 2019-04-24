# class for different generating a single service
class Service():

    # subclass build
    class Build():
        # initializer
        def __init__(self):
            self.build = {}

        # add context
        def context(self, input):
            if(isinstance(input, str)):
                self.build['context'] = input
                return True
            else:
                raise Exception('INVALID INPUT:{}\nis not a string'.format(input))

        # add dockerfile
        def dockerfile(self, input):
            if(isinstance(input, str)):
                self.build['dockerfile'] = input
                return True
            else:
                raise Exception('INVALID INPUT:{}\nis not a string'.format(input))

        # add args
        def args(self, input):
            if(isinstance(input, list)):
                self.build['args'] = input
                return True
            else:
                raise Exception('INVALID INPUT:{}\nis not a list'.format(input))

        # add cache_from
        def cache_from(self, input):
            if(isinstance(input, list)):
                self.build['cache_from'] = input
                return True
            else:
                raise Exception('INVALID INPUT:{}\nis not a list'.format(input))

        # add labels
        def labels(self, input):
            if(isinstance(input, list) or isinstance(input, dict)):
                self.build['labels'] = input
                return True
            else:
                raise Exception('INVALID INPUT:{}\nis not a list or dict'.format(input))

        # add wshm_size
        def shm_size(self, input):
            if(isinstance(input, int) or isinstance(input, str)):
                self.build['shm_size'] = input
                return True
            else:
                raise Exception('INVALID INPUT:{}\nis not an integer'.format(input))

        # add target
        def target(self, input):
            if(isinstance(input, str)):
                self.build['target'] = input
                return True
            else:
                raise Exception('INVALID INPUT:{}\nis not a string'.format(input))

        #return self as dictionary
        def get_dict(self):
            if('context' in self.build):
                return(dict(self.build))
            else:
                raise Exception('ERROR: build.context was not assigned')

    class Deploy():
        #initializer
        def __init__(self):
            self.deploy = {}

        #add context
        def endpoint_mode(self, input):
            if(isinstance(input, str)):
                self.deploy['endpoint_mode'] = input
                return True
            else:
                raise Exception('INVALID INPUT:{}\nis not a string'.format(input))

        #add labels
        def labels(self, input):
            if(isinstance(input, list) or isinstance(input, dict)):
                self.deploy['labels'] = input
                return True
            else:
                raise Exception('INVALID INPUT:{}\nis not a list or dict'.format(input))
        
        #add placement, constraints
        def placement_constraints(self, input):
            if(isinstance(input, list)):
                self.deploy['placement']['constraints'] = input
            else:
                raise Exception('INVALID INPUT:{}\nis not a list'.format(input))

        #add placement preference
        def placement_preference(self, input):
            if(isinstance(input, list)):
                self.deploy['placement']['preference'] = input
            else:
                raise Exception('INVALID INPUT:{}\nis not a list'.format(input))

        #add replicas
        def replicas(self, input):
            if(isinstance(input, str)):
                self.deploy['placement']['constraints'] = input
            else:
                raise Exception('INVALID INPUT:{}\nis not a list'.format(input))

        #add resources limit cpu
        def resources_limits_cpu(self, input):
            if(isinstance(input, str)):
                self.deploy['resources']['limits']['cpus'] = input
            else:
                raise Exception('INVALID INPUT:{}\nis not a string'.format(input))

        #add resources limit memory
        def resources_limits_memory(self, input):
            if(isinstance(input, str)):
                self.deploy['resources']['limits']['memory'] = input
            else:
                raise Exception('INVALID INPUT:{}\nis not a string'.format(input))

        #add resources reservations cpu
        def resources_reservations_cpu(self, input):
            if(isinstance(input, str)):
                self.deploy['resources']['limits']['cpus'] = input
            else:
                raise Exception('INVALID INPUT:{}\nis not a string'.format(input))

        #add resources reservations memory
        def resources_reservations_memory(self, input):
            if(isinstance(input, str)):
                self.deploy['resources']['limits']['memory'] = input
            else:
                raise Exception('INVALID INPUT:{}\nis not a string'.format(input))
        
        #add restart policy condition
        def restart_policy_condition(self, input):
            """
            Add restart policy condition
            @type input: string
            @param input: One of 'none', 'on-failure' or 'any'
            """
            if(isinstance(input, str)):
                if(input in ['none', 'on-failure', 'any']):
                    self.deploy['restart_policy']['condition'] = input
                else:
                    raise Exception("INVALID INPUT:{}\nis not One of 'none', 'on-failure' or 'any'".format(input))
            else:
                raise Exception('INVALID INPUT:{}\nis not a string'.format(input))

        #add restart policy delay
        def restart_policy_delay(self, input):
            """
            add delay to restart policy
            @type:  string
            @param: How long to wait between restart attempts
            """
            if(isinstance(input, str)):
                self.deploy['restart_policy']['deploy'] = input
            else:
                raise Exception('INVALID INPUT:{}\nis not a string'.format(input))

        #add restart policy delay
        def restart_policy_max_attempts(self, input):
            """
            add max attempts to restart policy
            @type:  integer
            @param: How many times to attempt to restart a container before giving up
            """
            if(isinstance(input, str)):
                self.deploy['restart_policy']['max_attempts'] = input
            else:
                raise Exception('INVALID INPUT:{}\nis not an integer'.format(input))

        #add restart policy delay
        def restart_policy_window(self, input):
            """
            add window to restart policy
            @type:  integer
            @param: How long to wait before deciding if a restart has succeeded
            """
            if(isinstance(input, str)):
                self.deploy['restart_policy']['window'] = input
            else:
                raise Exception('INVALID INPUT:{}\nis not a string'.format(input))

        #def restart policy rollback_config
        def restart_policy_rollback_config(self, input):
            raise NotImplementedError

        #def restart policy update_config
        def restart_policy_update_config(self, input):
            raise NotImplementedError

        #return self as dictionary
        def get_dict(self):
            if(bool(self.deploy)):
                return(dict(self.deploy))
            else:
                raise Exception('INVALID INPUT:{}\nis not a list or dict'.format(input))

    #initializer
    def __init__(self, name):
        self.name = name
        self.service = {name:{}}
        self.build = self.Build()
        self.deploy = self.Deploy()
        self.service[self.name]['build'] = self.build
        self.service[self.name]['deploy'] = self.deploy

    # add cap
    def cap_add(self, input):
        if(isinstance(input, list)):
            self.service[self.name]['cap_add'] = input
            return True
        else:
            raise Exception('INVALID INPUT:{}\nis not a list'.format(input))

    # cap drop
    def cap_drop(self, input):
        if(isinstance(input, list)):
            self.service[self.name]['cap_drop'] = input
            return True
        else:
            raise Exception('INVALID INPUT:{}\nis not a list'.format(input))
    
    # add cgroup_parent
    def cgroup_parent(self, input):
        if(isinstance(input, str)):
            self.service[self.name]['cgroup_parent'] = input
            return True
        else:
            raise Exception('{} -- is not a string'.format(input))
    
    # add command
    def command(self, input):
        if((isinstance(input, str)) or (isinstance(input, list))):
            self.service[self.name]['command'] = input
        else:
            raise Exception('INVALID INPUT:{}\nis not a string or list'.format(input))

    # add a dictionary with wanted configs
    def configs_add(self, input):
        if(isinstance(input, dict)):
            self.service[self.name]['configs'] = input
            return True
        else:
            raise Exception('INVALID INPUT:{}\nis not a dictionary'.format(input))

    # removes configs dictionary
    def configs_remove(self):
        if('configs' not in self.service[self.name]):
            raise Exception('service.configs does not exist. Nothing to remove.')
        else:
            del self.service[self.name]['configs']

    # add container_name
    def container_name(self, input):
        if(isinstance(input, str)):
            self.service[self.name]["container_name"] = input
        else:
            raise Exception('INVALID INPUT:{}\nis not a string'.format(input))

    # add credential_spec using file
    def credential_spec_file(self, input):
        if(isinstance(input, str)):
            self.service[self.name]["credential_spec"] = {"file":input}
            if('registry' in self.service[self.name]['credential_spec']):
                del self.service[self.name]['credential_spec']['registry']
        else:
            raise Exception('INVALID INPUT:{}\nis not a string'.format(input))
    
    # add credential_spec using registry
    def credential_spec_registry(self, input):
        if(isinstance(input, str)):
            self.service[self.name]['credential_spec'] = {"registry":input}
            if('file' in self.service[self.name]['credential_spec']):
                del self.service[self.name]['credential_spec']['file']
        else:
            raise Exception('INVALID INPUT:{}\nis not a string'.format(input))

    # add service dependenies
    def depends_on(self, input):
        if(isinstance(input, list)):
            self.service[self.name]["depends_on"] = input
        else:
            raise Exception('INVALID INPUT:{}\nis not a list'.format(input))
    
    #spit out compose dictionary
    def spit(self):
        if(bool(self.build.get_dict())):
            self.service[self.name]['build'] = self.build.get_dict()
        else:
            del self.service[self.name]['build']
        if(bool(self.deploy.get_dict())):
            self.service[self.name]['deploy'] = self.deploy.get_dict()
        else:
            del self.service[self.name]['deploy']
        print(self.service)
