import timeit


# n**2
list_setup = 'my_list = list(range(100))'
list_stmt = 'for n in my_list: n**2'
print(f'list n**2    : {timeit.timeit(setup=list_setup, stmt=list_stmt, number=100000)}')

set_setup = 'my_set = set(range(100))'
set_stmt = 'for n in my_set: n**2'
print(f'set n**2     : {timeit.timeit(setup=set_setup, stmt=set_stmt, number=100000)}')

dict_setup = 'my_dict = {n: None for n in range(100)}'
dict_stmt = 'for n in my_dict.keys(): n**2'
print(f'dict n**2    : {timeit.timeit(setup=dict_setup, stmt=dict_stmt, number=100000)}')

dict_obj_setup = '''
class MyClass(object): 
	pass
my_dict_obj = {n: MyClass() for n in range(100)}
'''
dict_obj_stmt = 'for n in my_dict_obj.keys(): n**2'
print(f'dict_obj n**2: {timeit.timeit(setup=dict_obj_setup, stmt=dict_obj_stmt, number=100000)}')


# n*n
list_setup = 'my_list = list(range(100))'
list_stmt = 'for n in my_list: n*2'
print(f'list n*2    : {timeit.timeit(setup=list_setup, stmt=list_stmt, number=100000)}')

set_setup = 'my_set = set(range(100))'
set_stmt = 'for n in my_set: n*2'
print(f'set n*2     : {timeit.timeit(setup=set_setup, stmt=set_stmt, number=100000)}')

dict_setup = 'my_dict = {n: None for n in range(100)}'
dict_stmt = 'for n in my_dict.keys(): n*2'
print(f'dict n*2    : {timeit.timeit(setup=dict_setup, stmt=dict_stmt, number=100000)}')

dict_obj_setup = '''
class MyClass(object): 
	pass
my_dict_obj = {n: MyClass() for n in range(100)}
'''
dict_obj_stmt = 'for n in my_dict_obj.keys(): n*2'
print(f'dict_obj n*2: {timeit.timeit(setup=dict_obj_setup, stmt=dict_obj_stmt, number=100000)}')


