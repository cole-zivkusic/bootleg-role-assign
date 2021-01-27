# Helper functions for tracking role stats

import json

'''
Keeps track of how many roles are applied by the bot
param count : an integer to be added to the total
'''


def roles_assigned(count):
    with open("roles_assigned.json", 'r') as lf:
        data = json.load(lf)
    lf.close()

    with open("roles_assigned.json", 'w') as lf:
        data["roles_assigned"] += count
        json.dump(data, lf)
    lf.close()


'''
return : the total number of roles applied by the bot
'''


def total_roles_assigned():
    with open("roles_assigned.json", 'r') as lf:
        data = json.load(lf)
    lf.close()

    return data["roles_assigned"]
