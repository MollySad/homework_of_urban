import inspect

def introspection_info(obj):
    intro = {}

    intro['type'] = type(obj).__name__
    attr_list = []
    method_list = []
    for attr_name in dir(obj):
        attr = getattr(obj, attr_name)
        if callable(attr):
            method_list.append(attr_name)
        else:
            attr_list.append(attr_name)
    intro['attributes'] = attr_list
    intro['methods'] = method_list
    intro['module'] = inspect.getmodule(obj)

    return intro


number_info = introspection_info(42)
print(number_info)
