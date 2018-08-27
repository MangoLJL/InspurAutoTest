# coding=utf-8
# 此模块作用为解决跨py文件传递参数的问题
# 业务上为了解决传递新建的模板的模板ID问题


def _init():
    global _global_dict
    _global_dict = {}


def set_value(name, value):
    _global_dict[name] = value


def get_value(name, default_value='None'):
    try:
        return _global_dict[name]
    except KeyError:
        return default_value
