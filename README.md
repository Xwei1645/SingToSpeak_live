# SingToSpeak_live

爬取[B站直播](https://live.bilibili.com "哔哩哔哩干杯~")弹幕，并实时转化为VSQx自动播放的工具

本项目参考：[TyTalk](https://github.com/GalaxieT/TyTalk "by GalaxieT")（语调教方面）、[bilibili-danmu](https://github.com/jonssonyan/bilibili-danmu "by jonssonyan")(获取弹幕)

您可点击[此处](https://www.wjx.top/vm/mBpVU3x.aspx "问卷星")反馈BUG/提供建议

# 使用说明

1. 使用前请将`reliance`目录移动到第三方库目录中（`../Python/Python3.x/Lib/site-packages`）
2. 请确保根目录下有`logs` `outputs`2个文件夹
3. 请确认已安装相关的库：`requests`, `pyaudio`, `jieba`, `pypinyin`

# 更新日志

### v0.8.9(2022.7.31，最新版本)
- 首次发布

# 关于作者
[bilibili大号](https://space.bilibili.com/573734644 "Xwei_P") [bilibili小号](https://space.bilibili.com/691973660 "是Xwie不是Xwei") [bilibili直播间](https://space.bilibili.com/691973660 "不定期使用SingToSpeak_live直播")

# 错误代码

### ERROR #1
原因：无法连接至更新服务器。

解决方法：检查网络连接。

### ERROR #2
原因：无法获取弹幕。

解决方法：检查网络连接。

### ERROR #3
原因：输入的房间号格式不正确。
解决方法：输入正确的房间号。
