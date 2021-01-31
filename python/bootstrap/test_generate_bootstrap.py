import pytest
import pkgutil

from .generate_template import GenerateBootstrap, HandlerAlreadyRegisteredException, CodeGenerationHandler
from .launch_test_controller import main

def test_registration():
    gb = GenerateBootstrap()
    gb.register_handler('handler_1', 1)
    assert gb._registered_handlers['handler_1'] == 1


def test_duplicate_registration():
    gb = GenerateBootstrap()
    gb.register_handler('handler_1', 1)
    with pytest.raises(HandlerAlreadyRegisteredException):
        gb.register_handler('handler_1', 2)

    assert gb._registered_handlers['handler_1'] == 1


def test_code_generation_handler():
    cgh = CodeGenerationHandler('foo', '/dev/null')
    example_dict = {'a': 'alpha', 'b': 'beta', 'l': [0, 1, 2, 3]}
    line_list = cgh._generate_simple_template(example_dict)


def test_exec():
    temp = 5
    def exec_and_return(expression):
        # print(f'Start of Locals: {locals()}')
        # print(f'At start, temp is {temp}')
        exec(f"{expression}\nlocals()['temp'] = k()")
        # print(f'At END, temp is {temp}')
        # print(f'End Locals: {locals()}')
        return locals()['temp']
    k = exec_and_return("""
# import json as os
#import json
# os = json
def k():
    # import json as os
    # os = json
    # print(f'Within exec, Name: {os.__name__} File: {os.__file__}')
    import os
    # import templates
    pkgpath = os.path.join(os.path.dirname(__file__), 'templates')
    print(f"Iter: {[name for _, name, _ in pkgutil.iter_modules([pkgpath])]}")
    # print(f"Iter: {[name for _, name, _ in pkgutil.iter_modules(['.templates'])]}")
    return 6789
# import json as os
    """)
    print(f'k is {k}')
    print(f'Temp: {temp}')
    # print(f'After exec, Name: {os.__name__} File: {os.__file__}')
    import sys
    print(f'System path: {sys.path}')
    # assert False

def test_launch_code():
    main()
