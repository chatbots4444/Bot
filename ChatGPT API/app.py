from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)


# Set up Gemini API credentials
genai.configure(api_key='AIzaSyDY14vxVg7N3ljHL1ZcGxrFwT50Y8YVofU')

# Define the default route to return the index.html file
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/index2")
def index2():
    return render_template("index2.html")

@app.route("/help")
def help():
    return render_template("help.html")

@app.route('/login')
def login():
    return render_template('login.html')

# Define the /api route to handle POST requests
@app.route("/api", methods=["POST"])
def api():
    # Get the message from the POST request
    message = request.json.get("message")

    try:
        # Generate content using Gemini
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(message)
        return jsonify({"content": response.text})
    except Exception as e:
        print(f"Error using Gemini API: {e}")
        return jsonify({"content": 'Failed to Generate response!'})
    

if __name__ == '__main__':
    app.run(debug=True)

    
    
    
# อันนี้อันเก่า

# @app.route("/api", methods=["POST"])
# def api():
#     message = request.json.get("message")
#     is_admin = request.json.get("isAdmin", False)  # รับค่า isAdmin จาก JSON

#     try:
#         model = genai.GenerativeModel('gemini-pro')
#         if is_admin:
#             chat_session = model.start_chat(
#             # TODO(Na): สำหรับเก็บ cache บทสนทนาถ้าอยู่ในโหมดผู้ดูแลระบบ โดยที่จะต้องสร้างตัวแปรเก็บค่าไว้
#               history=[
#      {
#               "role": "user",
#               "parts": [
#                 "ไวไฟใช้ไม่ได้",
#               ],
#             },
#             {
#               "role": "model",
#               "parts": [
#                 "ตรวจสอบ Wi-Fi ของคุณดู ปิดอยู่หรือไม่",
#               ],
#             },
#             {
#               "role": "user",
#               "parts": [
#                 "ไวไฟใช้ไม่ได้",
#               ],
#             },
#               {
#               "role": "user",
#               "parts": [
#                 "WiFiใช้ไม่ได้",
#               ],
#             },
#                   {
#                 "role": "user",
#                 "parts": [
#                     "อินเทอร์เน็ตช้ามากเลย",
#                 ],
#             },
#                  {
#                 "role": "user",
#                 "parts": [
#                     "ไวรัสเข้าคอมพิวเตอร์ทำไงดี",
#                 ],
#             },
#             {
#                 "role": "user",
#                 "parts": [
#                     "อีเมลใช้ไม่ได้",
#                 ],
#             },
#             {
#                 "role": "model",
#                 "parts": [
#                     "ขออภัยที่คุณกำลังประสบปัญหากับอีเมล ลองตรวจสอบสิ่งต่อไปนี้:\n\n1. ตรวจสอบการเชื่อมต่ออินเทอร์เน็ตของคุณ\n2. ยืนยันว่าชื่อผู้ใช้และรหัสผ่านของคุณถูกต้อง\n3. ลองเข้าสู่ระบบผ่านเว็บเบราว์เซอร์\n4. ตรวจสอบการตั้งค่าเซิร์ฟเวอร์ขาเข้าและขาออก\n5. ปิดโปรแกรมป้องกันไวรัสหรือไฟร์วอลล์ชั่วคราว\n\nหากยังไม่สามารถแก้ไขได้ กรุณาแจ้งข้อมูลเพิ่มเติมเกี่ยวกับปัญหาที่คุณพบ เช่น ข้อความแสดงข้อผิดพลาด หรือโปรแกรมอีเมลที่คุณใช้"
#                 ],
#             },
#             {
#                 "role": "user",
#                 "parts": [
#                     "คอมพิวเตอร์เปิดไม่ติด",
#                 ],
#             },
#             {
#                 "role": "user",
#                 "parts": [
#                     "ปริ้นเตอร์พิมพ์ไม่ออก",
#                 ],
#             },
#              {
#                 "role": "user",
#                 "parts": [
#                     "ลืมรหัสผ่านregทำไง",
#                 ],
#             },
#             {
#                 "role": "user",
#                 "parts": [
#                     "โปรแกรม Excel ค้าง",
#                 ],
                
                
#             },
#           ]
#         )

#             response = chat_session.send_message(message)
#             message_lower = message.lower()
#             if "ไวไฟใช้ไม่ได้" in message_lower:
#                 response = "ตรวจสอบ Wi-Fi ของคุณดู ปิดอยู่หรือไม่? หากเปิดอยู่แล้ว ลองรีสตาร์ท router หรืออุปกรณ์ของคุณดูนะคะ หรืออาจมีปัญหาเกี่ยวกับการตั้งค่าเครือข่าย ลองตรวจสอบ password หรือการตั้งค่า DNS อีกครั้งค่ะ"
#             elif "อินเทอร์เน็ตช้ามากเลย" in message_lower:
#                 response = "อาจเกิดจากปัญหาที่ตัวเราเอง เช่น โปรแกรมที่กินแบนด์วิดท์, ไวรัส, หรือปัญหาที่ผู้ให้บริการอินเทอร์เน็ต เช่น ปัญหาสายสัญญาณ, การใช้งานเกินโควต้า ลองรีสตาร์ทเราเตอร์, ตรวจสอบการเชื่อมต่อสายแลน, และติดต่อผู้ให้บริการอินเทอร์เน็ตเพื่อขอความช่วยเหลือ ค่ะ"
#             elif "อีเมลใช้ไม่ได้" in message_lower:
#                 response = "สำหรับปัญหาเมลใช้ไม่ได้ ลองตรวจสอบสิ่งต่อไปนี้:\n1. ตรวจสอบการเชื่อมต่ออินเทอร์เน็ต\n2. ยืนยันชื่อผู้ใช้และรหัสผ่าน\n3. ตรวจสอบการตั้งค่าเซิร์ฟเวอร์อีเมล\n4. ลองเข้าใช้งานผ่านเว็บเบราว์เซอร์\nหากยังไม่สามารถแก้ไขได้ กรุณาติดต่อฝ่าย IT support ค่ะ"
#             elif "WiFiใช้ไม่ได้" in message_lower:
#                 response = "ตรวจสอบ Wi-Fi ของคุณดู ปิดอยู่หรือไม่? หากเปิดอยู่แล้ว ลองรีสตาร์ท router หรืออุปกรณ์ของคุณดูนะคะ หรืออาจมีปัญหาเกี่ยวกับการตั้งค่าเครือข่าย ลองตรวจสอบ password หรือการตั้งค่า DNS อีกครั้งค่ะ"
#             elif "คอมพิวเตอร์เปิดไม่ติด" in message_lower:
#                 response = "หากคอมพิวเตอร์เปิดไม่ติด ลองทำตามขั้นตอนนี้:\n1. ตรวจสอบการเชื่อมต่อสายไฟ\n2. ลองเสียบปลั๊กไฟที่เต้าเสียบอื่น\n3. ตรวจดูว่ามีเสียงหรือไฟแสดงสถานะหรือไม่\n4. ถอดอุปกรณ์ต่อพ่วงทั้งหมดออกแล้วลองเปิดเครื่องใหม่\nหากยังไม่สามารถแก้ไขได้ กรุณาติดต่อฝ่าย IT support เพื่อตรวจสอบฮาร์ดแวร์ค่ะ"
#             elif "ปริ้นเตอร์พิมพ์ไม่ออก" in message_lower:
#                 response = "สำหรับปัญหาปริ้นเตอร์พิมพ์ไม่ออก ลองตรวจสอบดังนี้:\n1. ตรวจสอบการเชื่อมต่อสายเคเบิลหรือการเชื่อมต่อ Wi-Fi\n2. ตรวจสอบหมึกพิมพ์หรือผงหมึก\n3. ตรวจสอบว่ามีกระดาษติดหรือไม่\n4. รีสตาร์ทปริ้นเตอร์และคอมพิวเตอร์\n5. ตรวจสอบการตั้งค่าไดรเวอร์ปริ้นเตอร์\nหากยังไม่สามารถแก้ไขได้ กรุณาติดต่อฝ่าย IT support ค่ะ"
#             elif "โปรแกรม excel ค้าง" in message_lower:
#                 response = "หากโปรแกรม Excel ค้าง ลองทำตามขั้นตอนนี้:\n1. รอสักครู่ อาจกำลังประมวลผลข้อมูลขนาดใหญ่\n2. กด Ctrl+Alt+Delete และเลือก Task Manager เพื่อปิด Excel\n3. เปิด Excel ใหม่และเรียกคืนไฟล์ที่บันทึกอัตโนมัติ\n4. ตรวจสอบและอัปเดต Excel เป็นเวอร์ชันล่าสุด\n5. ตรวจสอบพื้นที่ฮาร์ดดิสก์และ RAM\nหากปัญหายังคงอยู่ กรุณาติดต่อฝ่าย IT support ค่ะ"
#             elif "ไวรัสเข้าคอมพิวเตอร์ทำไงดี" in message_lower:
#                 response = "ควรติดตั้งโปรแกรมป้องกันไวรัสที่ดีและอัปเดตอยู่เสมอ สแกนหาไวรัสอย่างสม่ำเสมอ และระวังการคลิกลิงก์หรือดาวน์โหลดไฟล์จากแหล่งที่ไม่น่าเชื่อถือ"
#             elif "ลืมรหัสผ่านregทำไง" in message_lower:
#                 response = "ควรติดต่อกับเจ้าหน้าที่ฝ่ายไอที"
#             else:
#                 response = response.text
#         else:
#             response = model.generate_content(message)
#             response = response.text
#         return jsonify({"content": response})
#     except Exception as e:
#         print(f"Error using Gemini API: {e}")
#         return jsonify({"content": 'Failed to Generate response!'})
# if __name__ == '__main__':
#     app.run(debug=True)