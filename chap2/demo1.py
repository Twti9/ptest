#开发者：罗地观生
#开发时间：2021/9/2 8:42
import requests

from lxml import html
etree=html.etree
from flask import Flask,json
app=Flask(__name__)
@app.route("/s",methods=["get","post"])
def datainfo():
    header={
        'user-agent':'Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36(kHTML,like Gecko) Chrome/92.0.4515.159'
                     ' Safari/537.36 Edg/92.0.902.78',
    }
    respons=requests.get("https://weather.cma.cn/web/weather/57679.html",headers=header)
    respons.encoding='utf-8'
    html=respons.text
    tree=etree.HTML(html)
    resp=tree.xpath("//ul[@class='dropdown-menu province-select']/li/text()")
    print(resp)
    info={"listinfo":resp}
    return json.dumps(info,ensure_ascii=False)
if __name__ == '__main__':
    app.run(host="127.1.1.1")