from src.poshta import *

token = 'COUNTERPARTY_TOKEN'
ukrpochta = Poshta('API_KEY')
new_client_data = {
    "name": "Vema LTD",
    "latinName": "Vema LTD",
    "uniqueRegistrationNumber": "0035",
    "addressId": "1284896",
    "phoneNumber": "067 123 12 34",
    "bankCode": "300001",
    "bankAccount": "26340343432",
    "resident": True,
    "edrpou": "40145721"
}
result = ukrpochta.create_client(token, new_client_data)
print(result)

# {'uuid': '5c15a920-5bcd-41b3-b488-aa130fdfac50', 'name': 'Vema LTD', 'firstName': None, 'middleName': None,
#  'lastName': None, 'latinName': 'Vema LTD', 'postId': None, 'externalId': None, 'uniqueRegistrationNumber': '0035',
#  'counterpartyUuid': '2304bbe5-015c-44f6-a5bf-3e750d753a17', 'addressId': 1284896, 'addresses': [
#     {'uuid': 'ca84b91e-e92a-4bac-ba62-02928ee0bc6d', 'addressId': 1284896,
#      'address': {'id': 1284896, 'postcode': None, 'region': 'Warsaw', 'district': None, 'city': 'Warsaw',
#                  'street': None, 'houseNumber': None, 'apartmentNumber': None, 'description': None,
#                  'countryside': False, 'foreignStreetHouseApartment': 'Warsawska 56, app 45',
#                  'detailedInfo': 'Польща, Warsaw, Warsaw, Warsawska 56, app 45', 'created': '2019-07-27T09:33:08',
#                  'lastModified': '2019-07-27T09:33:08', 'country': 'PL'}, 'type': 'PHYSICAL', 'main': True}],
#  'phoneNumber': '067 123 12 34', 'phones': [
#     {'uuid': 'ddf6e412-3c84-4364-bc51-7ee18bc8cd85', 'phoneId': 452397, 'phoneNumber': '067 123 12 34',
#      'type': 'PERSONAL', 'main': True}], 'email': '', 'emails': [], 'type': 'COMPANY',
#  'postPayPaymentType': 'POSTPAY_PAYMENT_CASH_ONLY', 'edrpou': '40145721', 'bankCode': '300001',
#  'bankAccount': '26340343432', 'contactPersonName': None, 'resident': True, 'GDPRRead': False, 'GDPRAccept': False,
#  'personalDataApproved': False, 'checkOnDeliveryAllowed': True}
