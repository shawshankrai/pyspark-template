import os
import sys
from jobs import sumofrange

if os.path.exists('jobs.zip'):
    sys.path.insert(0, 'jobs.zip')
else:
    sys.path.insert(0, './jobs')
    

if __name__ == '__main__':
    print(f'Sum of range is = {sumofrange.handler()}')
    