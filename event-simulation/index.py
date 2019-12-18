import random
import simpy

class Constants:
    RANDOM_SEED = 14
    NUM_SERVERS = 2        # Number of servers
    EXECUTION_TIME = 2     # Minutes it takes to run a task
    TASK_INTERVAL = 3      # Create a new task every ~3 minutes
    SIMULATION_TIME = 20   # Simulation time in minutes

class CloudPlatform(object):
    """College's cloud platform has a limited number of server (NUM_SERVERS) to
    process tasks. Tasks have to request one of the servers. When they got one, they
    can get run and wait for it to finish (which takes 'EXECUTION_TIME' minutes).

    """
    def __init__(self, env, num_servers, exec_time):
        self.env = env
        self.machine = simpy.Resource(env, num_servers)
        self.exec_time = exec_time

    def execute(self, task_name):
        """Takes a task and executes it.
        """
        yield self.env.timeout(Constants.EXECUTION_TIME)

def create_task(env, name, cw):
    """Creates a task with a given name and requests a server to execute it.
    """
    print("new task '%s' at %.2f." % (name, env.now))
    with cw.machine.request() as request:
        yield request
        print("Starts executing '%s' at %.2f" % (name, env.now))
        yield env.process(cw.execute(name))
        print("Finished %s at %.2f" % (name, env.now))


def setup(env, num_server, exec_time, task_interval):
    """Creates a cloud platform object and keeps creating tasks approx. every 
    'TASK_INTERVAL' minutes.
    """
    # creates the cloud platform
    platform = CloudPlatform(env, num_server, exec_time)

    # create 10 initial tasks
    for i in range(10):
        env.process(create_task(env, 'Task %d' % i, platform))

    # creates more tasks while the simulation is running
    while True:
        yield env.timeout(random.randint(task_interval - 2, task_interval + 2))
        i += 1
        env.process(create_task(env, 'Task %d' % i, platform))


# setup and start the simulation
print('Cloud Platform')
random.seed(Constants.RANDOM_SEED)

# creates an environment
env = simpy.Environment()
config = setup(env, Constants.NUM_SERVERS, Constants.EXECUTION_TIME, Constants.TASK_INTERVAL)
env.process(config)

# starts simulation
env.run(until=Constants.SIMULATION_TIME)
