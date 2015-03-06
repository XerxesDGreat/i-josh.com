from types import *
import uuid
import datetime
class MyClass:
    attribute_details = {
        'my_uuid': {'type': uuid.UUID, 'required': True, 'read_only': False},
        'your_uuid': {'type': uuid.UUID, 'required': True, 'read_only': False},
        'uuid_a': {'type': uuid.UUID, 'required': False, 'read_only': True},
        'uuid_b': {'type': uuid.UUID, 'required': False, 'read_only': True},
        'created_datetime': {'type': datetime.datetime, 'required': True, 'read_only': True},
        'updated_datetime': {'type': datetime.datetime, 'required': False, 'read_only': False},
        'target_datetime': {'type': datetime.datetime, 'required': False, 'read_only': False},
        'name': {'type': StringType, 'required': False, 'read_only': True},
        'location': {'type': StringType, 'required': False, 'read_only': False},
        'num_actions_taken': {'type': IntType, 'required': False, 'read_only': False}
    }
    def __init__(self, **kwargs):
        self.__dict__['_in_init'] = True
        for field_name, details in self.attribute_details.iteritems():
            if details['required'] and field_name not in kwargs:
                raise KeyError('%s is required' % field_name)
            elif field_name in kwargs:
                self.__setattr__(field_name, kwargs[field_name])
        self.__dict__['_in_init'] = False
    def __setattr__(self, attr_name, value):
        attr_detail = self.attribute_details.get(attr_name, None)
        if not attr_detail:
            raise AttributeError('no attribute %s in object of type %s' % (attr_name, self.__class__.__name__))
        if attr_detail['read_only'] and not self.__dict__['_in_init']:
            raise AttributeError('%s is read-only' % attr_name)
        if type(value) is not attr_detail['type']:
            raise ValueError('%s expected to be a %s' % (attr_name, attr_detail['type'].__name__))
        self.__dict__['_%s' % attr_name] = value
    def __getattr__(self, attr_name):
        if attr_name not in self.attribute_details:
            raise AttributeError('no attribute "%s" in object of type %s' % (attr_name, self.__class__.__name__))
        return self.__dict__['_%s' % attr_name]