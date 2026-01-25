class Mage:
    def __init__(self, name):
        ''' 
            Init constructor with public: name; private: health, status, is_respawning
        '''
        self.name = name
        self.__health = 100
        self.__status = 'hidup'
        self.__is_respawning = False
    
    def get_health(self):
        ''' 
            Fungsi untuk mendapatkan value dari health
        '''
        return self.__health
    
    def get_status(self):
        ''' 
            Fungsi untuk mendapatkan value dari status
        '''
        return self.__status
    
    def get_respawning(self):
        ''' 
            Fungsi untuk mendapatkan value dari is_respawning
        '''
        return self.__is_respawning
    
    def set_health(self, num):
        ''' 
            Fungsi untuk mengubah nilai dari health. Kebetulan yang lain juga berubah seperti: status, is_respawning
        '''
        
        if (self.__health - num) <= 0:
            self.__status = "meninggal"
            self.__health = 0

            if self.__status == "meninggal":
                self.__is_respawning = True

            return
        self.__health -= num

