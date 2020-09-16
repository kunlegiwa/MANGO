from Mango_Dist import utils as ut
#import utils as ut
import pandas as pd



class Distribution(object):
    '''A distribution class'''

    def __init__(self, **dist_args):
        """
        Initialise distribution.
        """
        # define default attributes
        self.default_attr = dict(distribution='exponential', scale=5, size=None)
        self.distribution_params = set(ut.allowed_distribution_params)
        self.allowed_attr = set(list(self.default_attr.keys()))
        self.default_attr.update(dist_args)
        self.__dict__.update((k, v) for k, v in self.default_attr.items()
                             if k in (self.allowed_attr | self.distribution_params))
        self.distribution_params = {k: self.__dict__.get(k, False) for k in self.distribution_params}
        self.drawn = False


    def draw(self):
        '''Draw from distribution without unpacking parameters'''
        if self.size and self.size > 1:
            self.drawn = ut.distributions_and_parameters['distributions'].get(self.distribution, lambda d: print('Invalid distribution')
                )(self.size, self.distribution_params).tolist()
            return self.drawn
        else:
            self.drawn = ut.distributions_and_parameters['distributions'].get(self.distribution, lambda d: print('Invalid distribution')
                )(self.size, self.distribution_params)
            return self.drawn

    
    def summarise(self):
        if self.drawn:
            df = pd.DataFrame(self.drawn, columns =['Draw'])
            return df.describe()
        return 'No draw'

    def __repr__(self):
        return 'Distribution'

