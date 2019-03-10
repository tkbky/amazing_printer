from ap import ap

complex_dict = {
    'email': 'ghopper@gmail.com',
    'first_name': 'grace',
    'last_name': 'hopper',
    'address': {
        'line_1': '1 Hacker Way',
        'line_2': '#1-3-3-7',
        'postal_code': '54321',
        'city': 'L.A',
        'state': 'S.F',
        'country': 'United States of America'
    },
    'deeply': {
        'nested': {
            'dict': {
                'that': {
                    'you': {
                        'can': {
                            'never': {
                                'imagine': ['foo', 'bar', 'baz'],
                            }
                        }
                    }
                }
            }
        }
    }
}

simple_dict = {
    'foo': None,
    'bar': 'bar',
}

string = 'The quick brown fox jumps over the lazy dog'

simple_list_1 = ['foo', 'bar', 'baz']
simple_list_2 = [1, 2, 3]
complex_list = ['foo', 'bar', 1, 2, simple_dict, complex_dict]

class SimpleObject:
    def __init__(self):
        self.foo = 'foo'
        self.bar = ['foo', 'bar', 1, 2, { 'foo': 1, 'bar': 2 }]
        self.baz = { 'foo': 1, 'bar': 2, 'baz': ['foo', 'bar', 1, 2] }

simple_object = SimpleObject()

print("String")
ap(string)
print("Dict (Complex)")
ap(complex_dict)
print("Dict (Complex, Sort keys)")
ap(complex_dict, { 'sort_keys': True })
print("Dict (Simple)")
ap(simple_dict)
print("Dict (Simple, Sort keys)")
ap(simple_dict, options = { 'sort_keys': True })
print("List (Simple 1)")
ap(simple_list_1)
print("List (Simple 2)")
ap(simple_list_2)
print("List (Complex)")
ap(complex_list)
print("Object (Simple)")
ap(simple_object)
