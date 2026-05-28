from utils import find_index
from variables import my_name,arr
import random

def change_my_luck():
    luck = False
    i = 1
    while(luck == False):
        i+=1
        numb = random.randint(1, 502)
        if(find_index(arr, numb)%2 == 0 and find_index(arr,numb)%3 == 0 and find_index(arr,numb)%5 == 0 and find_index(arr,numb)):
            luck = True
    
    return {"luck":luck,"repetetion":i}