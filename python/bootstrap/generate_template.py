from typing import List, Optional
from abc import ABC
from collections import OrderedDict


class CodeGenerationHandler(object):
    def __init__(self, handler_name: str, template_filename: str):
        self._handler_name = handler_name
        self._template_filename = template_filename

    def generate_code(self, global_data: dict,  handler_data: dict) -> List[str]:
        with open(self._template_filename, 'r') as f:
            file_lines = f.readlines()
            file_lines.insert(0, f'{self._handler_name}_data = {handler_data}')
            return file_lines

    def _generate_simple_template(self, data: dict) -> List[str]:
        retv = []
        retv.append(f'{self._handler_name} = {{')
        for (k, v) in data.items():
            retv.append(f'  {k} = {v},')
        retv.append(f'}}')
        return retv

class HandlerAlreadyRegisteredException(Exception):
    pass

class HandlerNotRegisteredException(Exception):
    pass

class UnknownDeviceException(Exception):
    pass


class GenerateBootstrap(object):
    def __init__(self, device_data: Optional[dict] = None):
        self._registered_handlers = OrderedDict()
        self._device_data = device_data
    
    def register_handler_module(self, handler_module):
        name = handler_module.__name__.split('.')[-1]
        handler = CodeGenerationHandler(name, handler_module.__file__)
        self.register_handler(name, handler)
        # print(f'Module file: {handler_module.__file__} Name: {handler_module.__name__}')

    def register_handler(self, handler_name: str, handler: CodeGenerationHandler):
        """
        Note - handlers return code in the order that they are registered. There
        is currently no mechanism for changing their order.
        """
        if handler_name in self._registered_handlers:
            raise HandlerAlreadyRegisteredException(handler_name)
        self._registered_handlers[handler_name] = handler
    
    def set_device_data(self, device_data: dict):
        """
        Note - this doesn't copy the data, so be aware it will be a mutable reference.
        """
        self._device_data = device_data

    def generate_for_device(self, MAC_address: str) -> List[str]:
        if MAC_address not in self._device_data:
            raise UnknownDeviceException(MAC_address)

        device_data = self._device_data[MAC_address]
        retv = []
        for (handler_name, handler_instance) in self._registered_handlers.items():
            retv.extend(handler_instance.generate_code(device_data.get('global', {}), device_data.get(handler_name, {})))
        return retv

    def exec_for_device(self, MAC_address: str):
        code_lines = self.generate_for_device(MAC_address)
        code_lines.append("print(f'Hello')")
        code_lines.append('exec_main_loop()')
        exec_code_lines(code_lines)

    def generate_from_handler(self, handler_name: str, global_data: dict,  handler_data: dict) -> List[str]:
        return self._registered_handlers[handler_name].generate_code(global_data, handler_data)


def exec_code_lines(line_list: List[str]):
    exec('\n'.join(line_list))


def make_standard_bootstrap_generator(device_data: dict):
    gb = GenerateBootstrap(device_data=device_data)
    from . import templates as templates
    print(f'Templates: {dir(templates)}')
    from .templates import main_loop
    gb.register_handler_module(main_loop)
    return gb