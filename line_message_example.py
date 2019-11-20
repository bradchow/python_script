import requests
import datetime 

#You can get your token from https://notify-bot.line.me/zh_TW/ 
token = 'your token'

def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code

now = datetime.datetime.now()
#print (str)(now.strftime("%m/%d %H:%M:%S"))
message = 'Something happened on ' + (str)(now.strftime("%m/%d %H:%M:%S"))

return_value = lineNotifyMessage(token, message)
print 'ret: ' + (str)(return_value) 