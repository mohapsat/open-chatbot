import statistics

# from statistics import mean

new_list = [1, 2, 3, 4, 5, 6, 7,8,8,7,4,33,4,6]


def mean(my_list):
    total = 0
    for item in my_list:
        total = total + item
    s_mean = total / len(my_list)
    return s_mean



# for i=0; i<=len(my_list); i++
#     print(i)

m = mean(new_list)

print(len(new_list))
s = statistics.median(new_list)




print(int(s))

print(dir(statistics))

# ['Counter', 'Decimal', 'Fraction', 'LinearRegression', 'NormalDist', 'StatisticsError', '_SQRT2', '__all__',
#  '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__',
#  '__spec__', '_coerce', '_convert', '_decimal_sqrt_of_frac', '_exact_ratio', '_fail_neg', '_float_sqrt_of_frac',
#  '_integer_sqrt_of_frac_rto', '_isfinite', '_kernel_invcdfs', '_mean_stdev', '_newton_raphson', '_normal_dist_inv_cdf',
#  '_quartic_invcdf', '_quartic_invcdf_estimate', '_random', '_rank', '_sqrt_bit_width', '_sqrtprod', '_ss', '_sum',
#  '_triweight_invcdf', '_triweight_invcdf_estimate', 'acos', 'asin', 'atan', 'bisect_left', 'bisect_right',
#  'correlation', 'cos', 'cosh', 'count', 'covariance', 'defaultdict', 'erf', 'exp', 'fabs', 'fmean', 'fsum',
#  'geometric_mean', 'groupby', 'harmonic_mean', 'hypot', 'isfinite', 'isinf', 'itemgetter', 'kde', 'kde_random',
#  'linear_regression', 'log', 'math', 'mean', 'median', 'median_grouped', 'median_high', 'median_low', 'mode',
#  'multimode', 'namedtuple', 'numbers', 'pi', 'pstdev', 'pvariance', 'quantiles', 'random', 'reduce', 'repeat', 'sin',
#  'sqrt', 'stdev', 'sumprod', 'sys', 'tan', 'tau', 'variance']
