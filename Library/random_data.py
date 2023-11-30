import random

num = random.randint(1, 9999)

def gen_random_cust_data():
    rndm_accnt_num = str(num) + str(num) + str(num)[0:2]
    rndm_email = 'customer' + str(num) + '@gmail.com'
    rndm_cust_name = 'customer' + str(num)
    return rndm_accnt_num, rndm_cust_name, rndm_email

print(gen_random_cust_data())

def gen_random_SLA_name():
    name = 'Test' + str(num)
    return name

print(gen_random_SLA_name())
