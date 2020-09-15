from itertools import cycle
import random
from random import expovariate, uniform, triangular, gammavariate, lognormvariate, weibullvariate, choice, choices, shuffle, gauss


def seed(z):
    random.seed(z)

allowed_distributions = ['exponential', 'unrounded_uniform', 'rounded_uniform', 'normal', 'average', 'fixed', 'triangular', 
                                  'lognormal', 'gamma', 'empirical', 'sequential', 'probability_profile', 'no_arrivals']
distributions = {}

def distribution(d):
    distributions[d.__name__] = d


@distribution
def exponential(params):
    try:
        if not params['average'] or params['average'] <= 0:
            raise ValueError('Invalid average time')
        return int(expovariate(1 / params['average']))
    except ValueError:
        exit('Invalid average time')


@distribution
def unrounded_uniform(params):
    try:
        if not params['lower_bound'] or not params['upper_bound']:
            raise ValueError('Invalid lower_bound or upper_bound')
        if params['lower_bound'] < 0.0 or params['upper_bound'] < 0.0:
            raise ValueError('Distribution must sample positive numbers only')
        if not params['lower_bound'] < params['upper_bound']:
            raise ValueError('lower_bound must be smaller than upper_bound')
        return round(uniform(float(params['lower_bound']), float(params['upper_bound'])), 2)
    except ValueError:
        exit('Could not get unrounded uniform sample time')


@distribution
def rounded_uniform(params):
    try:
        if not params['lower_bound'] or not params['upper_bound']:
            raise ValueError('Invalid lower_bound or upper_bound')
        if params['lower_bound'] < 0 or params['upper_bound'] < 0:
            raise ValueError('Distribution must sample positive numbers only')
        if not params['lower_bound'] < params['upper_bound']:
            raise ValueError('lower_bound must be smaller than upper_bound')
        return random.randint(int(params['lower_bound']), int(params['upper_bound']))
    except ValueError:
        exit('Could not get rounded uniform sample time')


@distribution
def normal(params):
    '''resample if negative'''
    try:
        if not params['average'] or not params['standard_deviation']:
            raise ValueError('Invalid average or standard_deviation')

        normal_sample = gauss(params['average'], params['standard_deviation'])
        while normal_sample <= 0.0:
            normal_sample = gauss(params['average'], params['standard_deviation'])
        return int(normal_sample)
    except ValueError:
        exit('Could not get normally distributed sample time')


@distribution
def average(params):
    '''Normal distribution with large sd of 25% of the mean'''
    try:
        if not params['average']:
            raise ValueError('Invalid average')

        normal_sample = gauss(params['average'], (0.25 * params['average']))
        while normal_sample <= 0.0:
            normal_sample = gauss(params['average'], (0.25 * params['average']))
        return int(normal_sample)
    except ValueError:
        exit('Could not get normally distributed sample time')


@distribution
def fixed(params):
    if isinstance(params['fixed_value'], str) or params['fixed_value'] < 0:
        raise ValueError('Invalid fixed_value')
    return params['fixed_value']


@distribution
def triangular(params):
    try:
        if not params['lower'] or not params['upper'] or not params['mode']:
            raise ValueError('Invalid lower, upper or mode')
        if params['lower'] < 0.0 or params['upper'] < 0.0 or params['mode'] < 0.0:
            raise ValueError('Triangular distribution must sample positive numbers only.')
        if not params['lower'] <= params['mode'] <= params['upper']:
            raise ValueError('Triangular distribution lower bound must be <= mode must be <= upper bound.')
        return int(random.triangular(params['lower'], params['upper'], params['mode']))
    except ValueError:
        exit('Could not get triangular distribution')


@distribution
def lognormal(params):
    '''resample if negative'''
    try:
        if not params['average'] or not params['standard_deviation']:
            raise ValueError('Invalid average or standard_deviation')
        return int(lognormvariate(params['average'], params['standard_deviation']))
    except ValueError:
        exit('Could not get lognormal distribution')


@distribution
def gamma(params):
    try:
        if not params['alpha'] or not params['beta']:
            raise ValueError('Invalid average or standard_deviation')
        return int(gammavariate(params['alpha'], params['beta']))
    except ValueError:
        exit('Could not get gamma distribution')

@distribution
def erlang(params):
    try:
        if not params['average'] or not params['k']:
            raise ValueError('Invalid average or standard_deviation')
        if not isinstance(params['k'], int):
            raise ValueError('K must be an integer')
        return int(gammavariate(params['average'], params['k']))
    except ValueError:
        exit('Could not get erlang distribution')

@distribution
def empirical(params):
    """Takes `distribution_list` the observations from which to sample"""
    try:
        if not params['distribution_list'] or not isinstance(params['distribution_list'], list):
            raise ValueError('Invalid distribution list, must be non empty list')
        if any(o < 0 for o in params['distribution_list']):
            raise ValueError('Empirical distribution must sample positive numbers only.')
        return choice(params['distribution_list'])
    except ValueError:
        exit('Could not get empirical distribution')


@distribution
def sequential(params):
    """Takes `distribution_list` the sequence to cycle through"""
    try:
        if not params['distribution_list'] or not isinstance(params['distribution_list'], list):
            raise ValueError('Invalid distribution list, must be non empty list')
        if any(o < 0 for o in params['distribution_list']):
            raise ValueError('Sequential distribution must sample positive numbers only.')
        return next(cycle(params['distribution_list']))
    except ValueError:
        exit('Could not get sequential distribution')


@distribution
def probability_profile(params):
    """Takes `distribution_list` the values to sample
    and weights_list, the associated probabilities """
    try:
        if not params['distribution_list'] or not params['weights_list'] or not isinstance(params['distribution_list'], list) or not isinstance(params['weights_list'], list):
            raise ValueError('Invalid distribution_list or weights_list must be non empty list') 
        if len(params['distribution_list']) != len(params['weights_list']):
            raise ValueError('Lengths must be equal')
        if any(o < 1 for o in params['distribution_list']):
            raise ValueError('Probability profile distribution must sample numbers greater than 0')
        if any(p < 0 or p > 1.0 for p in params['weights_list']):
            raise ValueError('Probability profile distribution must have valid probabilities.')
        #if int(sum(params['weights_list'])) != 1:
        #    raise ValueError('Probability profile distribution probabilities must sum to 1.0.')
        return choices(params['distribution_list'], params['weights_list'])[0]
    except ValueError:
        exit('Could not get probability profile distribution')

@distribution
def no_arrivals(params):
    """A placeholder distribution if there are no arrivals."""
    return float('Inf')


def sample(key, dist_params):
    return distributions.get(key, lambda d: print('Invalid distribution'))(dist_params)


# test1 = {'distribution_list': [1, 2, 3, 4, 5, 6], 
#          'weights_list': [0.05, 0.1, 0.25, 0.2, 0.3, 0.1], 
#          'average': 10, 
#          'standard_deviation': 2.5, 
#          'lower_bound': 3, 
#          'upper_bound': 6, 
#          'fixed_value': 7, 
#          'lower': 10, 
#          'upper': 20, 
#          'mode': 15, 
#          'alpha': 2, 
#          'beta': 5, 
#          }

# print('exponential: {}'.format(sample('exponential', test1)))
# print('unrounded_uniform: {}'.format(sample('unrounded_uniform', test1)))
# print('rounded_uniform: {}'.format(sample('rounded_uniform', test1)))
# print('normal: {}'.format(sample('normal', test1)))
# print('average: {}'.format(sample('average', test1)))
# print('fixed: {}'.format(sample('fixed', test1)))
# print('triangular: {}'.format(sample('triangular', test1)))
# print('lognormal: {}'.format(sample('lognormal', test1)))
# print('gamma: {}'.format(sample('gamma', test1)))
# print('erlang: {}'.format(sample('erlang', test1)))
# print('empirical: {}'.format(sample('empirical', test1)))
# print('sequential: {}'.format(sample('sequential', test1)))
# print('probability_profile: {}'.format(sample('probability_profile', test1)))
# print('no_arrivals: {}'.format(sample('no_arrivals', test1)))


