import sys

def main(text, **kwargs):
    set_a = set(sys.argv[1:]) 
    set_b = set(['apple', 'banana', 'mango', 'orange'])
   
    for i in text:
        return(set_a - set_b)
        
print(main(sys.argv[1:]))