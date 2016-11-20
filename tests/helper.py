# Helper methods for tests

def deep_equals(val1, val2):
    if val1 == val2:
        # Try naive compare first
        return True
    if type(val1) == dict:
        if type(val2) != dict:
            return False
        return dict_deep_equals(val1, val2)
    elif type(val1) == list:
        if type(val2) != list:
            return False
        return list_deep_equals(val1, val2)
    return False

def list_deep_equals(expected, test):
    if len(expected) != len(test):
        return False
    for v1, v2 in zip(sorted(expected), sorted(test)):
        return deep_equals(v1, v2)
    return True

def dict_deep_equals(expected, test):
    if len(expected.keys()) != len(test.keys()):
        return False
    for key, value in expected.iteritems():
        if key not in test:
            return False
        return deep_equals(value, test[key])
    return True
