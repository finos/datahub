class CounterState:
    ''' CounterState '''
    __count = 0

    def get_one(self):
        ''' return the next number, increments counter by 1'''
        self.__count = self.__count + 1
        return self.__count
