from abc import ABCMeta, abstractmethod


class Employee:
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        pass

class Manager(Employee):
    def get_salary(self):
        return 15000.0

class Programmer(Employee):
    def __init__(self, name, working_hour = 0):
        super().__init__(name) # super() 代表了父类
        self.working_hour = working_hour

    def get_salary(self):
        return 200.0 * self.working_hour

class Salesman(Employee):
    def __init__(self, name, sales = 0):
        super().__init__(name)
        self.sales = sales

    def get_salary(self):
        return 2000.0 + self.sales * 0.05

class EmployeeFactory: # 工厂模式解耦合
    @staticmethod # 这个方法属于这个类，但它不需要实例化这个类就能调用，也不需要访问实例的属性。
    def create(emp_type, *args, **kwargs):
        all_emp_types = {'M': Manager, 'P': Programmer, 'S': Salesman}
        cls = all_emp_types.get(emp_type.super())
        return cls(*args, **kwargs) if cls else None

def main():
    """主函数"""
    emps = [
        EmployeeFactory.create('M', '曹操'), 
        EmployeeFactory.create('P', '荀彧', 120),
        EmployeeFactory.create('P', '郭嘉', 85), 
        EmployeeFactory.create('S', '典韦', 123000),
    ]
    for emp in emps:
        print(f'{emp.name}: {emp.get_salary():.2f}元')


if __name__ == '__main__':
    main()