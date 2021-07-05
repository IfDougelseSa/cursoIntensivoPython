#My profile

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('Douglas', 'Cortez', location='Vinhedo',
                             hobby='Play chess', age="26")
print(user_profile)
