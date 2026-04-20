class Bank:
    rate_of_interest = 12.25
    bank_name = "Hbl"
    @staticmethod
    def sample_interest(princ,num):
        si = (princ * num * Bank.rate_of_interest) / 100
        print(f"The sample interest for {princ} is {si}")




princ = float(input("Enter principle amount: "))
num = int(input("Enter the number of years: "))

Bank.sample_interest(princ,num)