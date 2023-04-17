#driver.set_page_load_timeout(5000)设置超时
#driver.page_source#获取页面源码
#driver.save_screenshot(file_name)页面截屏
#driver.quit()中止会话
#driver.back()后退
#driver.implicitly_wait(5)设置隐式等待时间
#driver.set_script_timeout(5000)设置脚本超时时间
#orientation = driver.orientation获取显示方向，横屏竖屏
#driver.orientation = "LANDSCAPE"设置显示方向
#location = driver.location()获取地理位置
#driver.set_location(49, 123, 10)设置地理位置
#log_types = driver.log_types获得可用的日志类型
#logs = driver.get_log('driver')获得日志对象
#driver.log_event('appium', 'funEvent')记录事件
#driver.get_events()获取事件
#driver.get_events(['event1', 'event2'])获取事件
#driver.update_settings({"sample": "value"}))更新设备的设置项
#driver.get_settings提取设备的设置项
#driver.start_activity("com.example", "ActivityName")启动Activity
#driver.current_activity获取当前Activity名称
#driver.current_package获取当前包名
#driver.install_app('/Users/johndoe/path/to/app.apk')安装应用
#driver.is_app_installed('com.example.AppName')检查设备上是否安装了指定的应用程序
#driver.launch_app()启动应用
#driver.background_app()应用置于后台
#driver.close_app()关闭app
#driver.reset()重置应用
#driver.remove_app('com.example.AppName')删除应用
#driver.get_clipboard()获取剪切板
#driver.get_clipboard_text()获取剪切板文字
#driver.set_clipboard('happy testing')设置剪切板
#driver.set_clipboard_text('happy testing')设置剪切板文字
#推送文件
# dest_path = '/data/local/tmp/test_push_file.txt'
# data = bytes('This is the contents of the file to push to the device.', 'utf-8'
# )
# driver.push_file(dest_path, base64.b64encode(data).decode('utf-8'))
# driver.pull_file('/path/to/device/foo.bar')拉取文件
# driver.pull_folder('/path/to/device/')拉取文件夹
# driver.shake()摇一摇
# driver.lock()锁定
# driver.unlock()解锁
#duration（可省略）： 滑动这个操作一共持续的时间长度，单位：ms
# driver.is_locked()设备是否锁定
# driver.press_keycode(10)按键Code
# driver.hide_keyboard()隐藏键盘
# driver.is_keyboard_shown()是否显示键盘
# driver.toggle_wifi()切换WiFi
# driver.toggle_location_services()切换定位服务
# driver.send_sms('19904636190', 'Hey lol')发送短信(只支持模拟器)
# driver.make_gsm_call('5551234567', GsmCallActions.CALL)拨打电话(只支持模拟器)、
# driver.set_network_speed(NetSpeed.LTE)网络速度
# driver.get_performance_data('my.app.package', 'cpuinfo', 5)返回支持读取的系统状态信息，例如cpu，内存，网络流量和电池信息
# driver.get_performance_data_types()获取性能数据类型
# driver.start_recording_screen()开始屏幕录制
# driver.open_notifications()打开通知(仅模拟器)
# driver.get_system_bars()获取系统栏
# 获取系统时间
# time = driver.device_time
# time = driver.get_device_time()
# time = driver.get_device_time("YYYY-MM-DD")
# driver.find_element_by_accessibility_id('SomeAccessibilityID')元素查找
# driver.find_elements_by_accessibility_id('SomeAccessibilityID')元素组查找
# el = driver.find_element_by_accessibility_id('leizi')元素查找
# el.click()元素点击
# driver.find_element_by_accessibility_id('leizishuoceshi').send_keys('Hello world!')发送key
# driver.find_element_by_accessibility_id('leizishuoceshi').clear()清理值
# e1=driver.find_element_by_accessibility_id('leizishuoceshi')
# text = el.text获取元素的文本
# driver.find_element_by_accessibility_id('leizishuoceshi').tag_name获取标签名
# driver.find_element_by_accessibility_id('leizishuoceshi').get_attribute('content-desc')获取元素属性
# driver.find_element_by_accessibility_id('leizishuoceshi').is_selected()元素被选中
# driver.find_element_by_accessibility_id('leizishuoceshi').is_enabled()元素是否可操作性
# driver.find_element_by_accessibility_id('leizishuoceshi').is_displayed()元素是否可见
# driver.find_element_by_accessibility_id('leizishuoceshi').location获取元素定位
# driver.find_element_by_accessibility_id('leizishuoceshi').size获取元素大小
# driver.find_element_by_accessibility_id('leizishuoceshi')获取元素矩形
# driver.find_element_by_accessibility_id('leizishuoceshi').value_of_css_property("style")获取css元素的值
# element = self.driver.find_element_by_accessibility_id('leizishuoceshi')
# element.location_in_view获取视图中的元素位置
# el = self.driver.find_element_by_accessibility_id('leizishuoceshi')
# el.submit()表单提交
# driver.switch_to.active_element获取焦点元素
# context = driver.current_context获取当前Context
# 移动到点
# actions = ActionChains(driver)
# actions.move_to(element, 10, 10)
# actions.perform()
# Click单击
# actions = ActionChains(driver)
# actions.move_to_element(element)
# actions.click()
# actions.perform()
# 双击
# actions = ActionChains(driver)
# actions.move_to_element(element)
# actions.double_click()
# actions.perform()
# 轻按屏幕启用设备
# from appium.webdriver.common.touch_action import TouchAction
# actions = TouchAction(driver)
# actions.tap(element)
# actions.perform()
# 双击
# from appium.webdriver.common.touch_action import TouchAction
# actions = TouchAction(driver)
# actions.double_tap(element)
# actions.perform()
# 手指在屏幕上移动
# from appium.webdriver.common.touch_action import TouchAction
# actions = TouchAction(driver)
# actions.tap_and_hold(element)
# actions.move_to(element, 50, 50)
# actions.perform()
# 手指长按触摸屏的事件
# from appium.webdriver.common.touch_action import TouchAction
# actions = TouchAction(driver)
# actions.long_press(element)
# actions.perform()
# 手指在触摸屏上滚动的运动事件
# from appium.webdriver.common.touch_action import TouchAction
# actions = TouchAction(driver)
# actions.scroll_from_element(element, 10, 100)
# actions.scroll(10, 100)
# actions.perform()
# 手指在触摸屏上滑动的动作事件
# from appium.webdriver.common.touch_action import TouchAction
# actions = TouchAction(driver)
# actions.flick_element(element, 1, 10, 10)
# actions.perform()
# 执行多点触控动作序列
# from appium.webdriver.common.touch_action import TouchAction
# from appium.webdriver.common.multi_action import MultiAction
# a1 = TouchAction()
# a1.press(10, 20)
# a1.move_to(10, 200)
# a1.release()
# a2 = TouchAction()
# a2.press(10, 10)
# a2.move_to(10, 100)
# a2.release()
# ma = MultiAction(self.driver)
# ma.add(a1, a2)
# ma.perform()
# 执行触摸动作序列
# from appium.webdriver.common.touch_action import TouchAction
# actions = TouchAction(driver)
# actions.tap_and_hold(20, 20)
# actions.move_to(10, 100)
# actions.release()
# actions.perform()
# driver.switch_to.window("handle")切换窗口
# driver.close()关闭窗口
# driver.current_window_handle()获取窗口句柄
# driver.window_handles()获取窗口所有的句柄
# driver.title获取标题
# driver.get_window_size()获取窗口大小
# driver.set_window_size(10, 10)设置窗口大小
# 获取窗口位置
# handle_one_position = self.driver.get_window_position()
# handle_two_position = self.driver.get_window_position("handleName")
# driver.set_window_position(10, 10)设置窗口位置
# driver.maximize_window()最大化窗口
# driver.forward()前进
# driver.back()回退
# driver.refresh()刷新
# driver.get_cookies()获取所有 Cookies(仅是 Web context)
# driver.add_cookie({name: 'foo', value: 'bar'})设置 Cookie (仅是 Web context)
# driver.delete_cookie("cookie_name")删除 Cookie
# driver.delete_all_cookies()删除所有 Cookies
# driver.switch_to.frame(3)切换Frame
# driver.switch_to.parent()切换到父Frame
# driver.execute_async_script(‘document.title’）执行异步脚本
# driver.execute_script(‘document.title’)执行脚本
# 常见的元素定位方式
# driver.find_element_by_accessibility_id()
# driver.find_element_by_android_uiautomator("new UiSelector().resourceId(\"com.oupeng.mini.android:id/search_engine_title")")
# driver.find_element_by_class_name()#class属性是classname
# driver.find_element_by_id()
# driver.find_element_by_ios_class_chain()
# driver.find_element_by_ios_predicate()#仅支持iOS10以上，可以多个属性同时定位
# driver.find_element_by_ios_uiautomation()
# driver.find_element_by_link_text()
# driver.find_element_by_css_selector()
# driver.find_element_by_xpath()
# driver.find_element_by_partial_link_text()
# driver.find_element_by_tag_name()
# driver.find_element_by_name()#text属性是name


#driver.lock(5)#锁定解锁屏幕
#driver.background_app(5)#将当前应用放到后台五秒
#driver.hide_keyboard()收起键盘
#driver.start_activity('com.example.android.apis', '.Foo')在当前应用中打开一个 activity 或者启动一个新应用并打开一个 activity 。 只能在 Android 上使用
#driver.open_notifications()打开下拉通知栏 只能在Android 上使用
#driver.shake()摇晃应用
#driver.reset()应用重置（相当于卸载重装应用）
#driver.contextscontext 可以理解为 可进入的窗口 。例如，对于原生应用，可用的 context 和默认 context 均为 NATIVE_APP
#driver.current_context列出当前上下文
#driver.app_strings获取应用程序的字符串 (APP STRINGS)
#driver.keyevent(176)给设备发送一个按键事件(KEY EVENT)（只限安卓）
#driver.pinch(element=el)捏屏幕(PINCH) (双指往内移动来缩小屏幕)
#driver.zoom(element=el)放大 (ZOOM)屏幕 (双指往外移动来放大屏幕)
#driver.set_value(element=el,Val) # 设置 el 元素的值
#driver.scroll(originalEl, destinationEl ) # originalEl - 要滚动的元素 destinationEl - 要滚动到的元素 滑动 (SCROLL)到某个元素。从一个元素滚动到另一个元素

#推送文件到设备中去(PUSH FILE)，推送文件需要转换为'base64'
#data = "some data for the file"
#path = "/data/local/tmp/file.txt"
#driver.push_file(path, data.encode('base64'))

#获取/设置 appium 的服务器设置
#current_settings = driver.get_settings()
#driver.update_settings({"someSetting": True})

#driver.tap([(100, 20), (100, 60), (100,100)], 500) # list 中的元组放 5 个点，500 表示按下 500ms  多个点点击，最多五个点
'''
#在控件上执行press 按操作。
press(WebElement el)
#在坐标为（x,y）的点执行press 操作
press(int x, int y)
#在控件el 的左上角的x 坐标偏移x 单位，y左边偏移y 单位的坐标上执行press 操作。
press(WebElement el, int x, int y)
#释放操作，代表该系列动作的一个结束标志。
release()
#以el 为目标，从另一个点移动到该目标上
moveTo(WebElement el)
#以 （x,y） 点 为 目 标 ， 从 另 一 个 点 移 动 到 该 目 标 上
moveTo(intx,inty)
# 以控件el 的左上角为基准，x 轴向右移动x 单位，y 轴向下移动y 单位。以该点为目标，从另一个点移动到该点上。
moveTo(WebElement el, int x, int y)
# 在控件的中心点上敲击一下
tap(WebElement el)
#在（x,y）点轻击一下
tap(int x, int y)
#以控件el 的左上角为基准，x轴向右移动x 单位，y轴向下移动y 单位。在该点上轻击。
tap(WebElement el, int x, int y)
#代表一个空操作，等待一段时间
waitAction()
#等待ms 秒
waitAction(int ms)
#控件长按
longPress(WebElement el)
#点 长 按
longPress(intx,inty)
#偏移点长按
longPress(WebElement el, int x, int y)
#取消执行该动作
cancel()
#执行该动作
perform()
'''




