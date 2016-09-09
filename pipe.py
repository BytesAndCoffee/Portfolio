import inspect


class FrozenFunction:
    def __init__(self, func):
        self._func = func
        self.__name__ = func.__name__
        self._param = dict(inspect.signature(func).parameters)
        self.parameters = tuple(self._param)
        params = dict()
        for arg in self._param:
            if self._param[arg].default != inspect._empty:
                params[arg] = self._param[arg].default
            else: 
                params[arg] = None
        self.__dict__.update(params)
    
    def __call__(self, **args):
        params = {key: self.__dict__[key] for key in self.parameters}
        for param in params:
            if param in args:
                params[param] = args[param]
        return self._func(**params)

    def __setitem__(self, item, value):
        if item in self.__dict__:
            self.__dict__[item] = value
        else:
            raise AttributeError('Attribute not found')


class Pipeline:
    def __init__(self, funcs=None, val=None):
        self._val = val
        self._funcs = funcs if funcs else list()


    def __call__(self, func, args=None):
        self._funcs.append(FrozenFunction(func))
        # if args: self._args.update({func)
        return func

    @property
    def id(self):
        return str(self._val) + ' --> ' + ' | '.join(
                [func.__name__ for func in self._funcs]
                )

    def call(self, args=None):
        if args:
            for func in self._funcs:
                argdict = args.pop(0)
                if argdict:
                    for arg in argdict:
                        func[arg] = argdict[arg]
        for func in self._funcs:
            self._val = func(stdin=self._val)
        return self._val