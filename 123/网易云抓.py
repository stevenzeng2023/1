# pip install requests
import requests # 发送请求用的模块


# 音乐的URL地址
m_url = 'https://m801.music.126.net/20221112101020/0fc2805b9bf4b00dc0e481e469b989a6/jdyyaac/5152/5108/550e/f827b3d999fb40d82d5fbdf4fe0f246c.m4a'
# 伪装自己
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
# 发送请求到服务器，获取音乐资源
m_resp = requests.get(m_url)
# 服务器回应数据，并保存数据
with open('zzz.mps',"wb") as f:
    f.write(m_resp.content)
