from flask import Flask, render_template, request, redirect, url_for,session 
import time
import os

app=Flask (__name__)
app.secret_key="ALEX-CHINA-GROUP0808089"

#主路由
@app.route('/')
def index():
    return redirect(url_for('login'))
    
#登录页面判断>>>>>>>>>
@app.route ('/login',methods=['GET','POST'])
def login ():
    if request.method == "POST":
         username_dicy=[
             "Parrs","Theri","skepu","Asdf","kernel","小脾气","Yi.","ALEXCEO","p"
         ]
         password_dicy=[
             "i520msikk","wxid_7lyo6d0ze7ws22","OZH20100829","1"
         ]
         username=request.form.get ('username')
         password=request.form.get ('password')
         if username in username_dicy and password in password_dicy:
             session ['username']=username 
             return redirect(url_for('home_page'))
             #密码和名字正确直接返回home页面
         else:
             return redirect(url_for('loginloser_page'))
             #密码名字错误直接返回失败页面
    else:
        return render_template ('login.html')
@app.route ('/home',methods=['GET','POST'])
def home ():
    username = session.get ('username')
    vip_level ="GalacticrhythmLV1 "
    return render_template ('home.html',username=username,vip_level=vip_level)
    
@app.route ('/Alext',methods=['GET','POST'])
def Alext ():
    user_info={
        'registered':'2025-5-28 14:00',
        'username ': 'ALEX 用户',
        'vip':'GalacticrhythmLV1'
    }
    return render_template ('Alext.html',user_info=user_info)
    
#用户入职提交表单
if not os.path.exists('Entry'):
    os.makedirs ('Entry')
    
@app.route('/apply',methods=['POST'])
def apply ():
    job_title=request.form.get ('job_title')#职位
    appname = request.form.get ('ap_name')#用户名
    Phone = request.form.get ('Phone')#手机
    brief = request.form.get ('ap_i')#简介
    if not job_title or not appname :
        return render_template ('loser.html')
    now=time.strftime ("%Y-%m-%d %H%M%S")
    Filname = f'{now}{appname}的入职信息.txt'
    names=f"/storage/emulated/0/入职申请文件夹/{Filname}"
    with open (names,'w')as e :
        e.write (f'申请名字:{appname}\n')
        e.write (f'申请职位:{job_title}\n')
        e.write (f'申请简介:{brief}\n')
        e.write (f'电话:{Phone}\n')
        e.write (f'申请时间{now}')
    return render_template('start.html')
#跳转HTML页面函数写这里->>>>>>>>>>>>
#主业
@app.route ('/home',methods=['GET','POST'])
def home_page ():
    return render_template('home.html')
    
#登录失败   
@app.route ('/loginloser_page',methods=['GET','POST'])
def loginloser_page ():
    return render_template('logingloser.html')

#购买页面    
@app.route ('/buy',methods=['GET','POST'])
def buy_page ():
    return render_template('buy.html')
    
#用户账户信息
@app.route ('/Alext',methods=['GET','POST'])
def Alext_page ():
    return render_template('Alext.html')

#深入了解产品
@app.route ('/go',methods=['GET','POST'])
def go_page ():
    return render_template ('go.html')
    
#购买VIP
@app.route ('/buy_vip',methods=['GET','POST'])
def buy_vip_page ():
    return render_template ('buy_vip.html')

#加入我们
@app.route ('/Team',methods=['GET','POST'])
def Team_page ():
    return render_template ('Team.html')
    
#联系我们
@app.route ('/contact',methods=['GET','POST'])
def contact ():
    return render_template ('contact.html')
    
            
if __name__ == '__main__':
    app.run(debug=True)