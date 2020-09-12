import requests
from lipanampesa import gen_access_token
import keys

my_access = gen_access_token()

def register_url():
    access_token = my_access
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = { "ShortCode": keys.shortcode1 ,
        "ResponseType": "Completed",
        "ConfirmationURL": "https://bejawelfare.pythonanywhere.com/confirmation",
        "ValidationURL": "https://bejawelfare.pythonanywhere.com/validation_url"}
    
    response = requests.post(api_url, json = request, headers=headers)
    
    print (response.text)

# register_url()



def simulate_c2b():
    access_token = my_access
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = { "ShortCode":keys.shortcode1,
        "CommandID":"CustomerPayBillOnline",
        "Amount":"1",
        "Msisdn":keys.MSISDN,
        "BillRefNumber":"33222" }
    
    response = requests.post(api_url, json = request, headers=headers)
    
    print (response.text)


# simulate_c2b()