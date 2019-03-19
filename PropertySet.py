class PropertySet(object):
    _mutable = True

    def __init__(self, name, properties):
        if not all([type(p) == str for p in properties]):
            raise ValueError('Properties must all be strings.')

        self._mutable = True
        self._name = str(name)
        self._props = frozenset(properties)
        self._mutable = False

    def __getattr__(self, prop):
        if prop in ['_name', '_props', '_mutable']:
            return super(PropertySet, self).__getattribute__(prop)
        elif prop in self._props:
            return prop
        else:
            msg = "{0} object '{1}' has no attribute '{2}'"
            raise AttributeError(msg.format(type(self).__name__, self._name, prop))

    def __setattr__(self, prop, value):
        if self._mutable:
            super(PropertySet, self).__setattr__(prop, value)
        else:
            msg = "Cannot set attribute '{0}' because {1} object '{2}' is immutable"
            raise AttributeError(msg.format(prop, type(self).__name__, self._name))

    def __delattr__(self, prop):
        if self._mutable:
            super(PropertSet, self).__delattr__(prop, value)
        else:
            msg = "Cannot delete attribute '{0}' because {1} object '{2}' is immutable"
            AttributeError(msg.format(prop, type(self).__name__, self._name))

    def __iter__(self):
        def gen():
            for el in self._props:
                yield el

        return gen()

    def __repr__(self):
        elems = ', '.join(self)
        out = '{0} {{ {1} }}'.format(self._name, elems)
        return out

    def __eq__(self, other):
        return (
            self.__class__ == other.__class__
                and self._name == other._name
                and self._props == other._props
        )
