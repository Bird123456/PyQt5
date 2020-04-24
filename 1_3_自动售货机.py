from PyQt5.Qt import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("自动贩卖机")  # 标题
        self.resize(500, 500)  # 窗口大小
        self.set_ui()
        # self.sp_cao()
        # self.text_display()

    def set_ui(self):
        #设置钱
        la_money=QLabel("请投币：",self)
        la_money.move(100,50)
        rb_1=QRadioButton("1元",self)
        rb_1.move(200,50)
        rb_2=QRadioButton("5毛",self)
        rb_2.move(300,50)
        #分组
        money_group=QButtonGroup(self)
        money_group.addButton(rb_1,1)
        money_group.addButton(rb_2,2)
        self.money_group=money_group



        #设置商品
        la_sp=QLabel("请选择商品：",self)
        la_sp.move(100,150)
        rb_pijiu=QRadioButton("啤酒",self)
        rb_pijiu.move(200,150)
        rb_cz=QRadioButton("橙汁",self)
        rb_cz.move(300,150)
        # 分组
        sp_group = QButtonGroup(self)
        sp_group.addButton(rb_pijiu,1)#设置id
        sp_group.addButton(rb_cz,2)
        self.sp_group=sp_group

        #按钮
        pb_qd=QPushButton("确定",self)
        pb_qd.move(100,250)
        pb_qd.pressed.connect(self.sp_cao)

        pb_fw=QPushButton("复位",self)
        pb_fw.move(300, 250)
        pb_fw.pressed.connect(self.claer_cao)
        #显示器
        la_yl=QLabel("请取饮料:",self)
        la_yl.move(50,350)
        te_yl=QTextEdit(self)#文本设置
        te_yl.resize(80,35)
        te_yl.move(110,350)
        self.te_yl=te_yl

        la_zl=QLabel("找零:",self)
        la_zl.move(260, 350)
        te_zl=QTextEdit(self)#文本设置
        te_zl.resize(80,25)
        te_zl.move(300,350)
        self.te_zl = te_zl
 #清空数据
    def claer_cao(self):
        self.te_yl.setText("")
        self.te_zl.setText("")
        pass

#编辑商品与钱连接cao
    def sp_cao(self):
        sp_id=self.sp_group.checkedId()#获取选中按钮组中的按钮id
        money_id = self.money_group.checkedId()
        if (sp_id != -1 and money_id == -1):
            self.te_yl.setText("请选择商品！！")
        elif (sp_id == -1):
            self.te_yl.setText("请选择商品！！")  # 文本显示
        elif (sp_id == 1):
            print("购买了啤酒")
            sp_str = "啤酒"
            self.te_yl.setText(sp_str)#文本显示
            sp_id = 0.5
        elif (sp_id == 2):
            print("购买了橙汁")
            sp_str = "橙汁"
            self.te_yl.setText(sp_str)  # 文本显示
            sp_id = 0.5




        if(money_id==-1 or sp_id==-1):
            self.te_zl.setText("请投币！！")  # 文本显示

        elif((money_id == 1 or money_id == 2) and sp_id!=-1):
            if (money_id == 1):
                print("投入一元")
                money_id = 1
            elif (money_id == 2):
                print("投入5毛")
                money_id = 0.5
            zl=money_id-sp_id
            print(zl)
            zl=str(zl)#转化为字符串类型
            zl+="元"
            self.te_zl.setText(zl)  # 文本显示

        # # 获取投入的商品
        # def sp(val1):
        #     if (val1 == 1):
        #         print("购买了啤酒")
        #         sp_str = "啤酒"
        #         self.te_yl.setText(sp_str)#文本显示
        #         val1 = 0.5
        #         print(type(val1))
        #     else:
        #         print("购买了橙汁")
        #         sp_str = "橙汁"
        #         self.te_yl.setText(sp_str)  # 文本显示
        #         val1 = 0.5
        #         print(type(val1))
        # self.sp_group.buttonClicked[int].connect(sp)
        #
        # # 获取投入的money
        # def money(val):
        #     if (val == 1):
        #         print("投入一元")
        #         val = 1
        #         print(type(val))
        #     else:
        #         print("投入5毛")
        #         val = 0.5
        #         print(type(val))
        # self.money_group.buttonClicked[int].connect(money)

# #文本显示
#     def text_display(self):
#         str="sada"
#         self.te_yl.setPlainText(str)

if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建一个程序对象
    window=Window()
    window.show()#将窗口显示
    sys.exit(app.exec_())#安全退出窗口（保证程序不会退出）


