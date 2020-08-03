import random
from accounts.models import Account

from itertools import izip_longest



def create_pair(self, first_stundent, second_student):
    """
    Custom student model manager where first student and second student are picked
    randomly to make a pair.
    """
    
