from atm_card import ATMCard

class Customer(ATMCard):
    def __init__(self, id, custPin, custBalance):
        super().__init__(custPin, custBalance)
        self.id = id
    
    def info_id(self):
        return self.id

    #fitur debet dan simpan
    def withdrawBalance(self, nominal):
        if nominal > self.defaultBalance:
            msg = 'Not enough balance'
        else:
            self.defaultBalance -= nominal
            msg = 'Debit success..'
        return msg
    
    def depositBalance(self, nominal):
        self.defaultBalance += nominal
        msg = 'Success add your balance..'
        return msg

    
        
    