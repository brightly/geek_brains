class Corrently_int:

    def __init__(self, data_list):
        self.data_list = data_list

    def corr_input(self):
        while True:
            try:
                temp = int(input('Введите число в список: '))
                self.data_list.append(temp)
                quit = input('Введите stop для окончания ввода ')
                if quit.lower() == 'stop':
                    print(self.data_list)
                    break
            except:
                print('ошибка ввода')
            else:
                print(self.data_list)

input_cor = Corrently_int([])
print(input_cor.corr_input())