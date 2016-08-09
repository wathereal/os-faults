import abc


class Client(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_nodes(self):
        pass

    @abc.abstractmethod
    def get_services(self, name):
        pass