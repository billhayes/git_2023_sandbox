def hello(name):
    return 'Howdy' + name

def pi():
    return 3.14

if __name__ == '__main__':
    print('run pi test')
    assert pi() == 3.14
    print('test pi PASSED')
    
    print('run pi test that will fail')
    assert pi() == 99

    print('All tests passed')
    
    
    
