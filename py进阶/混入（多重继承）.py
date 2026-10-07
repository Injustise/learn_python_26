'''
Mixin 是一种面向对象的设计思想。它通常是一个独立的、很小的类，不单独使用，而是配合其他类一起使用（通过多重继承）。
ps：给普通的字典增添了一个功能: 限制字典的键只能被赋值一次。 如果重复赋值同一个键，就会报错 KeyError。
Mixin 的好处就是功能解耦
'''


class SetOnceMappingMixin:
    __slots__ = () # 限制类只能有哪些属性（省内存）
    '''
    Python 的类默认非常灵活，你可以随时随地给一个实例对象添加新属性
    这是因为每个对象内部都有一个隐藏的字典 __dict__，而所有的实例对象属性都存储在这个字典里（字典是散列表，非常占内存）
    '''
    def __setitem__(self, key, value): # my_dict['username'] = 'jackfrued' 背后执行 my_dict.__setitem__('username', 'jackfrued')
        if key in self:
            raise KeyError(str(key) + ' already set')
        return super().__setitem__(key, value) # 在多重继承中，super() 指 MRO 顺序表的下一个类。
    # 而 MRO 顺序表遵循 由左及右，由近及远

    # MRO 顺序表：SetOnceDict -> SetOnceMappingMixin -> dict -> object
class SetOnceDict(SetOnceMappingMixin, dict):
    pass

my_dict = SetOnceDict()
try:
    my_dict['username'] = 'jackfrued'
    my_dict['username'] = 'hellokitty'
except KeyError:
    pass
print(my_dict)