from numpy import random
from collections import defaultdict


class Distribution(object):
    '''A distribution class from which other distribution classes will inherit'''

    def __repr__(self):
        return 'Distribution'

    def sample(self, t=None, ind=None):
        pass

    def _sample(self, t=None, ind=None):
        """
        Performs vaildity checks before sampling.
        """
        s = self.sample(t=t, ind=ind)
        if (isinstance(s, float) or isinstance(s, int)) and s >= 0:
            return s
        else:
            raise ValueError('Invalid time sampled.')

    

def sample(dist, size, **dist_params):
    '''Sample distribution'''
    distributions_and_parameters = defaultdict(dict)
    allowed_distribution_params = ['a', 'b', 'n', 'p', 'df', 'alpha', 'scale', 'dfnum', 'dfden', 'shape', 'p', 'df', 'alpha', 'scale']
    distributions_and_parameters['parameters'].update((k, v) for k, v in dist_params.items() if k in allowed_distribution_params)

    try:
        return getattr(random, dist)(size=5, scale=3)
    except ValueError as e:
        exit(e)

