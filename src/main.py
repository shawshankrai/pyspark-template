import os
import sys

if os.path.exists('jobs.zip'):
    sys.path.insert(0, 'jobs.zip')
else:
    sys.path.insert(0, './jobs')
    
from jobs import sumofrange

if __name__ == '__main__':
    
sum = sumofrange.handler()
print(f'Sum of range is = {sum}')
    