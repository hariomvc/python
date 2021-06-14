annual_Inter_rate = 0

class SavingAccount:
    def set_balance(self, balance):
        self.saving_balance = balance
    def cal_monthly_interest(self, annual_Inter_rate):
        self.saving_balance += self.saving_balance * annual_Inter_rate /12


saver1 = SavingAccount()
saver2 = SavingAccount()
saver1.set_balance(2000)
saver2.set_balance(3000)
annual_Inter_rate = 0.05
saver1.cal_monthly_interest(annual_Inter_rate)
saver2.cal_monthly_interest(annual_Inter_rate)
print(f'Balance for Saver1: Rs.{saver1.saving_balance}; Balance for Saver2: Rs.{saver2.saving_balance}')
annual_Inter_rate = 0.07
saver1.cal_monthly_interest(annual_Inter_rate)
saver2.cal_monthly_interest(annual_Inter_rate)
print(f'Balance for Saver1: Rs.{saver1.saving_balance}; Balance for Saver2: Rs.{saver2.saving_balance}')
