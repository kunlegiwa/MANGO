import utils as ut

#MANGO TEST DISTRIBUTION FUNCTION

def draw(key, size=None, **dist_params):
    '''Standalone function to draw from distribution'''
    ut.distributions_and_parameters['parameters'].update((k, v) for k, v in dist_params.items() if k in ut.allowed_distribution_params)
    return ut.distributions_and_parameters['distributions'].get(key, lambda d: print('Invalid distribution'))(size, dist_params)


