'''
selenium模块的基本使用
问题：selenium模块和爬虫之间具有怎样的关联？
    -便捷的获取网站中动态加载的数据
    -便捷实现模拟登录
什么是selenium模块?
    -基于浏览器自动化的一个模块

selenium使用流程：
    -环境安装：pip install selenium
    -下载一个浏览器的驱动程序(谷歌浏览器)
    -实例化一个浏览器对象
    -编写基于浏览器自动化的操作代码
        -发起请求：get(url)
        -标签定位：find系列的方法
        -标签交互：send_keys('xxx')
        -执行js程序：exeute_script('jsCode')
        -前进，后退：back(),forward()
        -关闭浏览器：quit()

    -selenium处理iframe
        -如果定位的标签存在于iframe标签之中，则必须使用switch_to.frame(id)
        -动作链（拖动）：from selenium.webdriver import ActionChains
            -实例化一个动作链对象：action=ActionChains(bro)
            -click_and_hold(div)长按且点击操作
            -move_by_offset(x,y)
            -perform()让动作链立即执行
            -action.release()释放动作链对象













'''