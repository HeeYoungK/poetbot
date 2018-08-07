from rtmbot import RtmBot #class
from rtmbot.core import Plugin


class HelloPlugin(Plugin):
    def process_message(self, data):
        if "힘들어" in data["text"]:
            self.outputs.append([data["channel"], "연탄재 함부로 발로 차지 마라"])
        elif "힘들어" in data["text"]:
            self.outputs.append([data["channel"], "연탄재 발로 차지 마라"])
        elif "댕댕" in data["text"]:
            self.outputs.append([data["channel"], "개는 어느 날 문득 부숭부숭하고 작은 털뭉치로 사람에게 와서 마음을 온통 사로잡은 다음 서둘러 떠나는 존재다."])
        elif "유병재" in data["text"]:
            self.outputs.append([data["channel"], "어제의 나 개X끼야ㅠㅠ너 때문에 뺑이 치게 생겼잖아 부탁한다 내일의 나ㅠ"])

config = {
    "SLACK_TOKEN"=secret.SLACK_TOKEN
    "ACTIVE_PLUGINS": ["main.HelloPlugin"] #main이라는 제목 -> 모듈이 됨!

}
bot = RtmBot(config)
bot.start()


print("Hello! World!")
print("우리 인생에 필요한 시")
