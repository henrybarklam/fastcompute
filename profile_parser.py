import cProfile
import pstats
from Version1.naive_binary_parser import DataParser_V1 
from Version2.naive_binary_parser import DataParser_V2
  
tick_number = 100000
def profile_parsing_v1():
    parser_v1 = DataParser_V1()
    parser_v1.parse_ticks('test_data/test_ticks_1000000.bin')

def profile_parsing_v2():

    parser = DataParser_V2()
    parser.parse_ticks('test_data/test_ticks_1000000.bin')


if __name__ == '__main__':
    cProfile.run('profile_parsing_v1()', 'profile_stats_v1.prof')
    cProfile.run('profile_parsing_v2()', 'profile_stats_v2.prof')