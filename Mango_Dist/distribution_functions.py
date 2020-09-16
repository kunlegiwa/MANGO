import utils


#MANGO TEST DISTRIBUTION FUNCTION

def draw(key, size=None, **dist_params):
    '''Standalone function to draw from distribution'''
    utils.distributions_and_parameters['parameters'].update((k, v) for k, v in dist_params.items() if k in utils.allowed_distribution_params)
    return utils.distributions_and_parameters['distributions'].get(key, lambda d: print('Invalid distribution'))(size, dist_params)


