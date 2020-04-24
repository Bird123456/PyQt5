from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("航空服务查询模拟")
        self.resize(500, 500)
        self.set_ui()

    def set_ui(self):
        #提示文本
        la_hx=QLabel("航线:",self)
        la_hx.move(50,50)
        #航线按钮
        rb_hx1=QRadioButton("欧美",self)
        rb_hx1.move(100,50)
        rb_hx2=QRadioButton("国外非欧美",self,)
        rb_hx2.move(200,50)
        rb_hx3=QRadioButton("国外",self)
        rb_hx3.move(350,50)
        #分组
        hx_group=QButtonGroup(self)
        hx_group.addButton(rb_hx1,1)#设置id
        hx_group.addButton(rb_hx2,2)
        hx_group.addButton(rb_hx3,3)
        self.hx_group=hx_group

        # 提示文本
        la_cw = QLabel("舱位:", self)
        la_cw.move(50, 150)
        #舱位按钮
        rb_cw1=QRadioButton("商务舱",self)
        rb_cw1.move(100,150)
        rb_cw2=QRadioButton("经济舱",self,)
        rb_cw2.move(300,150)
        #分组
        cw_group = QButtonGroup(self)
        cw_group.addButton(rb_cw1, 1)  # 设置id
        cw_group.addButton(rb_cw2, 2)
        self.cw_group=cw_group

        # 提示文本
        la_sj = QLabel("飞行时间:", self)
        la_sj.move(50, 250)
        #舱位按钮
        rb_sj1=QRadioButton("2小时以内",self)
        rb_sj1.move(120,250)
        rb_sj2=QRadioButton("超过2小时",self,)
        rb_sj2.move(300,250)
        #分组
        sj_group = QButtonGroup(self)
        sj_group.addButton(rb_sj1, 1)  # 设置id
        sj_group.addButton(rb_sj2, 2)
        self.sj_group=sj_group

        #提示文本
        la_fw=QLabel("航空服务:",self)
        la_fw.move(50,350)
        #显示器
        te_fw=QTextEdit(self)
        te_fw.move(120,335)
        te_fw.resize(300,40)
        self.te_fw=te_fw
        #确认按钮
        pb_cx=QPushButton("查询",self)
        pb_cx.move(230,400)
        self.pb_cx=pb_cx
        pb_cx.pressed.connect(self.cx_check)

    def cx_check(self):
        hx_id=self.hx_group.checkedId()#获取航线id
        cw_id=self.cw_group.checkedId()#获取舱位id
        sj_id=self.sj_group.checkedId()#获取时间id

        hx_str=""
        cw_str=""
        sj_str=""

        if (hx_id == 1):
            hx_str = "欧美"
        if(hx_id==2):
            hx_str="国外非欧美"
        if (hx_id == 3):
            hx_str = "国内"
        if(hx_id==-1):
            hx_str="请选择航线"

        if(cw_id==1):
            cw_str="商务舱"
        if(cw_id==2):
            cw_str="经济舱"
        if (cw_id == -1):
            cw_str = "请选择舱位"

        if(sj_id==1):
            sj_str="2小时以内"
        if(sj_id==2):
            sj_str="超过2小时"
        if (sj_id == -1):
            sj_str = "请选择飞行时间"

        dy_str1 = "可以看电影"
        dy_str2 = "不能看电影"
        sw_str1 = "有食物提供"
        sw_str2 = "无食物提供"

        fh_str1=";"
        fh_str2=":"
        if(hx_id==-1 or cw_id==-1 or sj_id==-1):
            self.te_fw.setText("请完善相关服务！！")
        elif(hx_id==1):
            self.te_fw.setText(hx_str+fh_str1+cw_str+fh_str1+sj_str+fh_str2+dy_str1+fh_str1+sw_str1)
        elif(hx_id==2 and cw_id==1):
            self.te_fw.setText(hx_str + fh_str1 + cw_str + fh_str1 + sj_str + fh_str2 + dy_str1 + fh_str1 + sw_str1)
        elif(hx_id==2 and cw_id==2):
            self.te_fw.setText(hx_str + fh_str1 + cw_str + fh_str1 + sj_str + fh_str2 + dy_str2 + fh_str1 + sw_str1)
        elif(hx_id==3 and cw_id==1):
            self.te_fw.setText(hx_str + fh_str1 + cw_str + fh_str1 + sj_str + fh_str2 + dy_str2 + fh_str1 + sw_str1)
        elif(hx_id==3 and cw_id==2 and sj_id==2):
            self.te_fw.setText(hx_str + fh_str1 + cw_str + fh_str1 + sj_str + fh_str2 + dy_str2 + fh_str1 + sw_str1)
        elif(hx_id==3 and cw_id==2 and sj_id==1):
            self.te_fw.setText(hx_str + fh_str1 + cw_str + fh_str1 + sj_str + fh_str2 + dy_str2 + fh_str1 + sw_str2)



if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=Window()

    window.show()

    sys.exit(app.exec_())


