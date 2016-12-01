#!/usr/bin/env python
# encoding: utf-8
import threading


class LazyIntialization(object):
    """
    lazy实例化
    --------------
    通常会有一些代码会在 import 的时候去做一些实例化的事情，这种作法会有一些问题，
    使用这个库可以避免在导入的时候真正去执行或实例化它。

    比如，原来这种代码::

       >>> message_client = snow.Client(message_conf.host, message_conf.port, timeout=messsage_conf.timeout)

    可以改写为::

       >>> message_client = LazyIntialization(snow.Client, 'message_client', message_conf, 'host', 'port', timeout='timeout')


    """

    __singleton_lock = threading.Lock()
    _instances = {}

    def __init__(self, factory_cls, instance_name, conf, *args, **kwargs):
        self.__factory_cls = factory_cls
        self.__instance_name = instance_name
        self.__conf = conf
        self.__args = args
        self.__kwargs = kwargs

    @classmethod
    def get_instance(cls, factory_cls, instance_name, conf, *args, **kwargs):
        if instance_name in cls._instances:
            return cls._instances[instance_name]
        with cls.__singleton_lock:
            if instance_name not in cls._instances:
                if conf:
                    new_args = map(lambda x: getattr(conf, x), args)
                    new_kwargs = {}
                    for k, v in kwargs.items():
                        new_kwargs[k] = getattr(conf, v)
                else:
                    new_args = args
                    new_kwargs = kwargs
                cls._instances[instance_name] = factory_cls(*new_args, **new_kwargs)
            return cls._instances[instance_name]

    def __getattr__(self, name):
        instance = self.get_instance(self.__factory_cls,
                                     self.__instance_name,
                                     self.__conf,
                                     self.__args,
                                     self.__kwargs
                                     )
        return getattr(instance, name)
