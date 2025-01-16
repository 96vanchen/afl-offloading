import numpy as np
import inspect
import functools


def store_args(method):
    """Stores provided method args as instance attributes.
    """
    argspec = inspect.getfullargspec(method)
    defaults = {}
    if argspec.defaults is not None:
        defaults = dict(
            zip(argspec.args[-len(argspec.defaults):], argspec.defaults))
    if argspec.kwonlydefaults is not None:
        defaults.update(argspec.kwonlydefaults)
    arg_names = argspec.args[1:]

    @functools.wraps(method)
    def wrapper(*positional_args, **keyword_args):
        self = positional_args[0]
        # Get default arg values
        args = defaults.copy()
        # Add provided arg values
        for name, value in zip(arg_names, positional_args[1:]):
            args[name] = value
        args.update(keyword_args)
        self.__dict__.update(args)
        return method(*positional_args, **keyword_args)

    return wrapper


def make_env(args):
    import map
    map_mec = map.Map()
    args.n_agents = map_mec.M
    args.obs_shape = 3 + (map_mec.N + map_mec.BS) * 2
    args.action_shape = map_mec.N + map_mec.BS + 1
    args.high_action = 1
    args.low_action = -1

    return map_mec, args
