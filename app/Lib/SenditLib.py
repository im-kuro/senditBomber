import requests, json
from colorama import Fore

class SenditLib:
    
    """
    send_message(): function sends a single POST request to 
    send the sendit to the user. We pass in all the needed
    data to do this.

    + TarLinkID == The id found in the link of the sendit ex. xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx
    + TarAppID - TarRecipientID - TarShadowToken can all be found when sending a sendit. you can get this data by seening 
                                                 the data sent in Network tab on inspect element
    """
    def send_snap_message(TarLinkID, TarAppID, TarRecipientID, TarShadowToken, Message):
        heades_to_use = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36",
            "content-type": "application/json",
            "app-id": TarAppID,# made in the first POST request in headers (this will change)
            "app-version": "1.0"
        }
        data_to_use = '{"recipient_identity":{"type":"id","value":"' + TarRecipientID + '"},"type":"sendit.post-type:question-and-answer-v1","data":{"question":"' + Message + '","promptText":""},"ext_data":{"sticker_id":"' + TarLinkID + '","author_shadow_token":"'+ TarShadowToken +'","snap_reference_id":""},"timer":0}'

        ReqRes = requests.post("https://api.getsendit.com/v1/posts", headers=heades_to_use, data=data_to_use)
        
        ReqResText = ReqRes.text
        ReqResJsonData = json.loads(ReqResText)
        
        if ReqRes.status_code == 200: print(Fore.RED + f"Message Sent!\nRequest Status ==> {ReqResJsonData['status']}")
        else: return f"Error sending message\nCode ==> {ReqRes.status_code}\nRequest Status ==> {ReqResJsonData['status']}"


    def send_insta_message(TarLinkID, TarAppID, TarRecipientID, TarShadowToken, Message):
        heades_to_use = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36",
            "content-type": "application/json",
            "app-id": TarAppID,# made in the first POST request in headers (this will change)
            "app-version": "1.0"
        }
        data_to_use = '{"recipient_identity":{"type":"id","value":"' + TarRecipientID + '"},"type":"sendit.post-type:question-and-answer-v1","data":{"question":"' + Message + '","promptText":""},"ext_data":{"sticker_id":"' + TarLinkID + '","author_shadow_token":"'+ TarShadowToken +'","snap_reference_id":""},"timer":0}'

        ReqRes = requests.post("https://api.getsendit.com/v1/posts", headers=heades_to_use, data=data_to_use)
        
        ReqResText = ReqRes.text
        ReqResJsonData = json.loads(ReqResText)
        
        if ReqRes.status_code == 200: print(Fore.RED + f"Message Sent!\nRequest Status ==> {ReqResJsonData['status']}")
        else: return f"Error sending message\nCode ==> {ReqRes.status_code}\nRequest Status ==> {ReqResJsonData['status']}"














