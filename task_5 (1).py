class TestCase:
    def __init__(self):
        self.steps = {}  
        self.result = []  
    
    def set_step(self, step_number, step_text):

        self.steps[step_number] = step_text
    
    def delete_step(self, step_number):

        if step_number in self.steps:
            del self.steps[step_number]
    
    def set_result(self, result):

        self.result = result
    
    def get_test_case(self):

        print({
            'шаги': self.steps,
            'ожидаемый результат': self.result
        })
    
    def step_number(self):

        new_steps = {}
        for key in sorted(self.steps.keys()):
            new_steps[key + 1] = self.steps[key]
        self.steps = new_steps



test_case_1 = TestCase()
test_case_1.set_step(1, 'перейти на сайт')
test_case_1.set_step(3, 'перейти в раздел Товары')
test_case_1.delete_step(3)
test_case_1.set_step(2, 'перейти в раздел Товары')
test_case_1.set_step(3, 'Нажать кнопку «В корзину» у первого товара')
test_case_1.set_result('Товар окажется в корзине') 
test_case_1.get_test_case()

print()  # разделитель для наглядности

test_case_2 = TestCase()
test_case_2.set_step(1, 'перейти на сайт')
test_case_2.set_step(2, 'перейти в раздел Корзина')
test_case_2.set_step(3, 'Нажать кнопку "Удалить"')
test_case_2.set_result('Товар удален из корзины')  
test_case_2.get_test_case()