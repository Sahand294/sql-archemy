from Bank_Account import BankAccount as Banks
from Filemanager import Filemanager

class NormalAccount(Banks):
    def __init__(self, bank_holder, account_number, password,account_file: str,type):
        super().__init__(bank_holder, account_number, password,account_file,type)
        self.new_attribute = None
    def review(self):
        return {'owner': Filemanager.check_status(self.file, self.account_number,'owner'), 'id': self.account_number,
                'balance': Filemanager.check_status(self.file, self.account_number, 'balance'),'type':'normall'}

