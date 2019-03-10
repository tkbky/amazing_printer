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
                                'imagine': [],
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

print("String")
ap(string)
print("Dict (Complex)")
ap(complex_dict)
print("Dict (Complex, Sort keys)")
ap(complex_dict, { 'sort_keys': True })
print("Dict (Simple)")
ap(simple_dict)
print("Dict (Simple, Sort keys)")
ap(simple_dict, { 'sort_keys': True })
