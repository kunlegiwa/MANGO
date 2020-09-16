from numpy import random
from collections import defaultdict



def sample(key, size=None, **dist_params):
    '''Sample distribution'''
    distributions_and_parameters = defaultdict(dict)
    allowed_distribution_params = ['a', 'b', 'n', 'p', 'df', 'alpha', 'scale', 'dfnum', 'dfden', 'shape', 'loc', 'mean', 'mu', 'kappa', 
                                   'low', 'high', 'left', 'mode', 'high', 'dtype', 'out', 'method', 'lam', 'nonc', 'cov', 'check_valid', 
                                   'tol', 'colors', 'nsample', 'ngood', 'nbad', 'pvals', 'sigma']
    distributions_and_parameters['parameters'].update((k, v) for k, v in dist_params.items() if k in allowed_distribution_params)

    def distribution(d):
        distributions_and_parameters['distributions'][d.__name__] = d

    @distribution
    def beta(params):
        try:
            return random.beta(params['a'], params['b'], size)
        except ValueError as e:
            exit(e)

    @distribution
    def binomial(params):
        try:
            return random.binomial(params['n'], params['p'], size)
        except ValueError as e:
            exit(e)

    @distribution
    def chisquare(params):
        try:
            return random.chisquare(params['df'], size)
        except ValueError as e:
            exit(e)

    @distribution
    def dirichlet(params):
        try:
            return random.dirichlet(params['alpha'], size)
        except ValueError as e:
            exit(e)

    @distribution
    def exponential(params):
        try:
            return random.exponential(params['scale'], size)
        except ValueError as e:
            exit(e)

    @distribution
    def f(params):
        try:
            return random.f(params['dfnum'], params['dfden'], size)
        except ValueError as e:
            exit(e)

    @distribution
    def gamma(params):
        try:
            return random.gamma(params['shape'], params['scale'], size)
        except ValueError as e:
            exit(e)

    @distribution
    def geometric(params):
        try:
            return random.geometric(params['p'], size)
        except ValueError as e:
            exit(e)

    @distribution
    def gumbel(params):
        try:
            return random.gumbel(params['loc'], params['scale'], size)
        except ValueError as e:
            exit(e)

    @distribution
    def hypergeometric(params):
        try:
            return random.hypergeometric(params['ngood'], params['nbad'], params['nsample'], size)
        except ValueError as e:
            exit(e)

    @distribution
    def laplace(params):
        try:
            return random.laplace(params['loc'], params['scale'], size)
        except ValueError as e:
            exit(e)

    @distribution
    def logistic(params):
        try:
            return random.logistic(params['loc'], params['scale'], size)
        except ValueError as e:
            exit(e)

    @distribution
    def lognormal(params):
        try:
            return random.lognormal(params['mean'], params['sigma'], size)
        except ValueError as e:
            exit(e)

    @distribution
    def logseries(params):
        try:
            return random.logseries(params['p'], size)
        except ValueError as e:
            exit(e)

    @distribution
    def multinomial(params):
        try:
            return random.multinomial(params['n'], params['pvals'], size)
        except ValueError as e:
            exit(e)

    @distribution
    def multivariate_hypergeometric(params):
        try:
            return random.multivariate_hypergeometric(params['colors'], params['nsample'], size, params['method'])
        except ValueError as e:
            exit(e)

    @distribution
    def multivariate_normal(params):
        try:
            return random.multivariate_normal(params['mean'], params['cov'], size,  params['check_valid'], params['tol'])
        except ValueError as e:
            exit(e)

    @distribution
    def negative_binomial(params):
        try:
            return random.negative_binomial(params['n'], params['p'], size)
        except ValueError as e:
            exit(e)

    @distribution
    def noncentral_chisquare(params):
        try:
            return random.noncentral_chisquare(params['df'], params['nonc'], size)
        except ValueError as e:
            exit(e)

    @distribution
    def noncentral_f(params):
        try:
            return random.noncentral_f(params['dfnum'], params['dfden'], params['nonc'], size)
        except ValueError as e:
            exit(e)

    @distribution
    def normal(params):
        try:
            return random.normal(params['loc'], params['scale'], size)
        except ValueError as e:
            exit(e)

    @distribution
    def pareto(params):
        try:
            return random.pareto(params['a'], size)
        except ValueError as e:
            exit(e)

    @distribution
    def poisson(params):
        try:
            return random.poisson(params['lam'], size)
        except ValueError as e:
            exit(e)

    @distribution
    def power(params):
        try:
            return random.power(params['a'], size)
        except ValueError as e:
            exit(e)

    @distribution
    def rayleigh(params):
        try:
            return random.rayleigh(params['scale'], size)
        except ValueError as e:
            exit(e)

    @distribution
    def standard_cauchy(params):
        try:
            return random.standard_cauchy(size)
        except ValueError as e:
            exit(e)

    @distribution
    def standard_exponential(params):
        try:
            return random.standard_exponential(size, params['dtype'], params['method'], params['out'])
        except ValueError as e:
            exit(e)

    @distribution
    def standard_gamma(params):
        try:
            return random.standard_gamma(size, params['shape'], params['dtype'], params['out'])
        except ValueError as e:
            exit(e)

    @distribution
    def standard_normal(params):
        try:
            return random.standard_normal(size, params['dtype'], params['out'])
        except ValueError as e:
            exit(e)

    @distribution
    def standard_t(params):
        try:
            return random.standard_t(params['df'], size)
        except ValueError as e:
            exit(e)

    @distribution
    def triangular(params):
        try:
            return random.triangular(params['left'], params['mode'], params['right'], size)
        except ValueError as e:
            exit(e)

    @distribution
    def uniform(params):
        try:
            return random.uniform(params['low'], params['high'], size)
        except ValueError as e:
            exit(e)

    @distribution
    def vonmises(params):
        try:
            return random.vonmises(params['mu'], params['kappa'], size)
        except ValueError as e:
            exit(e)

    @distribution
    def wald(params):
        try:
            return random.wald(params['mean'], params['scale'], size)
        except ValueError as e:
            exit(e)

    @distribution
    def weibull(params):
        try:
            return random.weibull(params['a'], size)
        except ValueError as e:
            exit(e)

    @distribution
    def zipf(params):
        try:
            return random.zipf(params['a'], size)
        except ValueError as e:
            exit(e)


    return distributions_and_parameters['distributions'].get(key, lambda d: print('Invalid distribution'))(dist_params)

