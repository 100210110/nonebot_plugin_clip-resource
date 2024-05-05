from nonebot import on_fullmatch, on_startswith, on_command
from nonebot.params import ArgPlainText
from re import findall
from nonebot.adapters.onebot.v11 import MessageEvent
from nonebot.adapters.onebot.v11 import GroupMessageEvent as V11MessageEvent
from nonebot.adapters.onebot.v12 import GroupMessageEvent as V12MessageEvent
from nonebot.adapters.onebot.v11 import Message
from nonebot.internal.rule import Rule



group_list = [
    123456789,  # 请在此自定加群号
]

def group_rule(event: MessageEvent):
    try:
        group_id = int(findall(r'\d+', str(event.get_session_id).split('group_id=')[1])[0])
        if group_id in group_list:
            return True
    except:
        return False


check_group = Rule(group_rule)


# 贡献者名字和QQ, 使用如 f"{name[Re]}" 来使用
name = {# 名单
    "Re": "Re-10*******", # 我自己
    "C神": "C神-33********", # 提供ae报错支持和部分资源
    "咸的慌鱼": "咸的慌鱼-298*******", # 提供部分网站和adobe阿里云盘资源
    "恐龙": "超级无敌恐龙大王-16********", # 提供部分魔法节点
    "阿轩": "阿轩", # 5天10稿的超人阿轩，提供了免费商用汇总的网站
    "hxd_2": "好兄弟二辈子(代剪)-17********" # 好兄弟家族的二辈子，提供了游资网、声音克隆网站
}

txt = {
    # 主菜单
    'menu': "阿巴阿巴, 这里是Re太懒了配置的机器人: \n\
格式为叫出菜单后回复序号\n\
或直接'list 1'跳转\n\
有多页的话如'4'为菜单'4_1'为第一页: \n\
\n\
1, 番剧生肉下载网站;\n\
2, 番剧在线观看网站;\n\
3, 值得推荐的番剧(夹带私货bushi);\n\
4, 截图或台词搜番(共2页);\n\
5, 音效、插件、模板、配色、字幕翻译等(共2页)\n\
6, Adobe全家桶、c4d、补帧等软件资源下载\n\
7, Ae导不出的问题\n\
8, 音频处理如分离人声、乐器, 克隆声音\n\
9, adobe插件, 群友每的插件会记录在此(共2页)\n\
10, 设计, 出版等, 字体相关\n\
11, 魔法机场, 这里只敢做介绍还请私聊Re\n\
\n\
0, 神级网站, 免费商用汇总网站",
    # list_0
    0: f"一位义母分享的网站(贡献: {name['阿轩']}): \n\
    https://www.mfsc123.com/\n\
    网站汇总, 免费商用, 提前少多少弯路啊",
    # list_1
    1: f"生肉磁链网站(带有内封、外挂字样的): \n\
请直接复制到浏览器, 有傻蛋直接就点, 特此告知\n\
\n\
1, 动漫花园资源网(需要翻墙): \n\
    -https://dmhy.anoneko.com/ \n\
\n\
2, 动漫花园(无需翻墙, 排版简洁): \n\
    -http://dongmanhuayuan.com/ \n\
\n\
3, 蜜柑动漫(无需翻墙, 但加载速度有点玄学): \n\
    -https://mikanime.tv/ \n\
\n\
另附种子下载软件qBittorrent(教程B站可搜): \n\
    -https://www.fosshub.com/qBittorrent.html \
",
    # list_2
    2: f"在线看番: \n\
把'点'换成'.', 空格删干净。没办法啊, 机器人没法直接发这几个网站\n\
\n\
1, アニメ新番組 [看新番推荐](无需魔法): \n\
    https://bangumi点online/ \n\
\n\
2, OmoFun看番网站({name['咸的慌鱼']}): \n\
    https://www 点 omofun 点 xyz/index 点 php/vod/play/id/7930/sid/2/nid/10.html\n\
",
    # list_3
    3: f"推荐的好看番剧(更新于2024-3-25 17:38:08): \n\
\n\
1, GIRLS BAND CRY-24年4月番\n\
    hh, 画面有种RWBY的味道, 丝滑流畅表情灵动, 动作用心, 观感优秀舒适, 好看的很\n\
\n\
2, 想成为魔法少女-24年1月番\n\
    福利番, 套路蛮新的\n\
    好看的, 不便多说, 戳不戳xp得看了才知道\n\
\n\
3, 葬送的芙莉莲-23年10月番\n\
    -这部番剧观感十分得自然丝滑, 一定要看!\n\
    -神! 葬送的芙莉莲真乃神中神! 一定要看!\n\
\n\
4, 我心里危险的东西-24年1月番\n\
    学生时代的爱情, 太过耀眼, 令我自惭形秽\n\
    非常好看, 番剧对人物内心等角度刻画十分细致, 暧昧中的男女主\n\
    我词穷了, 总之就是令人羡慕到死的爱恋, 一定要看!\n\
",
    # list_4
    4: f"以图搜番目录\n\
查看方法: list 4_X\n\
\n\
第一页(4_1):\n\
1, 动漫搜图\n\
2, 毛子的搜万物\n\
3, 33台词\n\
\n\
第二页(4_2):\n\
4, 33搜帧\n\
5, 动漫台词搜索\
",
    4_1: f"以图搜番第一页: \n\
\n\
1, 动漫搜图(https://trace.moe/ )\n\
-用途: 通过截图定位在番剧中出现位置\n\
-优点: \n\
    1, 响应速度极快, 2秒左右即返回结果\n\
    2, 番剧搜索十分精准, 并附带精确到秒的出现位置\n\
-缺点: \n\
    1, 依据色块搜索, 图片不能有过重的调色\n\
    2, 截图必须十分规整, 不能出现如手机拍屏拍到显示器边框, 截图截到的播放器边框)\n\
    3, 不翻墙加载慢\n\
\n\
2, 毛子的nb搜图网站(https://ya.ru/ )\n\
-用途: 搜索图片出处\n\
-优点: \n\
    1, 搜图引擎非常强大, 图片相似度极高\n\
    2, 可以搜到图片的更高分辨率版本\n\
-缺点: \n\
    1, 国内不翻墙需要注册账号, 翻墙可直接使用\n\
    2, 只能搜索图片出现过的网站, 无法搜索视频的截图\n\
\n\
3, 33台词(http://33.agilestudio.cn/ )\n\
-用途: 通过台词搜索出现的剧集和位置\n\
-优点: \n\
    1, 番剧连续剧电影均可搜\n\
    2, 同样的精准到集数和秒数\n\
    3, 提供片段预览, 登录后提供云截图\n\
-缺点: \n\
    1, 如果是搜番剧台词会夹杂一些电影出现在搜索结果, 不过往下翻翻就有了\n\
\
",
    4_2: f"以图搜番第二页: \n\
\n\
4, 33搜帧(https://fse.agilestudio.cn/ )\n\
-用途: 基于ai, 通过文字描述搜索相似镜头\n\
-优点: \n\
    1, 不用我说也明白, 急速获取大量匹配镜头\n\
-缺点: \n\
    1, 网页端几乎只能搜索和预览, 无法下载\n\
    2, 如果需求苛刻, 也无法搜到, 只是ai搜索不是ai生成\n\
\n\
5, 动漫台词搜索网站(https://dialogue.moe/ )\n\
-用途: 动漫台词搜索番剧(贡献: {name['咸的慌鱼']})\n\
-优缺点: 暂无\
",
    # list_5
    5: f"音效、图片、模板等素材目录\n\
查看方法: list 5_X\n\
\n\
第一页(5_1): \n\
0, 免费商用汇总\n\
1, 爱给网\n\
2, LookAe\n\
3, 书生CG资源站\n\
4, 游资网\n\
5, 求字体网\n\
\n\
第二页(5_2): \n\
6, 魔音工坊\n\
7, ColorSpace\n\
8, 免扣图片网\n\
9, 自己传网盘的音效\n\
",
    5_1: f"音效、图片、模板等素材第一页\n\
\n\
0, 究极免费可商用汇总(https://www.mfsc123.com/ )\n\
    一位义母分享(贡献: {name['阿轩']}), 点进去就晓得含金量了\n\
\n\
1, 爱给网(https://www.aigei.com/ )\n\
    近乎万能的素材网站, 下载消耗铜币, 每天免费50个\n\
\n\
2, 大名鼎鼎的LookAe(https://www.lookae.com/ )\n\
    极多免费插件, pr、ae、达芬奇都有, 宝藏, 速速收藏\n\
\n\
3, 书生CG资源站(https://c4dsky.com/ )\n\
    ae、blender、c4d、FCPX、Houdini的插件以及各种模板, 绝大部分免费, 基本目前业余接触得到的都免费\n\
\n\
4, 游资网(https://youzi006.com/ )\n\
    游戏的素材为主, 包括aepr的游戏剪辑模板/调色预设, 游戏人物绿幕等\n\
    (贡献: {name['hxd_2']})\n\
\n\
5, 求字体网(https://www.qiuziti.com/ )\n\
    字体的识别与搜索, 但本该付费的字体依旧付费, 搜完就各显神通吧\n\
    ！！！提醒, 不知道什么时候被墙了, 目前需要翻墙访问\n\
",
    5_2: f"音效、图片、模板等素材第二页\n\
\n\
6, 魔音工坊(https://www.moyin.com/ )\n\
    ai配音, 专业级别配音, word文档式傻瓜操作, 免费也提供很多音色和全功能, 可以说人家不在意被白嫖\n\
    可微调, 多音字、数字符号、连读、音标、局部变速、局部变音、停顿调节、插入静音等等\n\
\n\
7, ColorSpace - 调色板生成器和渐变工具(https://mycolor.space/ )\n\
    再也不用浪费时间寻找完美的调色板了！永远不要再浪费时间去寻找完美的颜色！只需输入颜色！ 只需输入颜色！并生成漂亮的调色板 并生成漂亮的调色板\n\
\n\
8, 免抠图片网(https://miankoutupian.com/ )\n\
    基本什么都有, 全都带透明通道, 甚至游戏立绘技能图标, 它都这么好了, 版权问题我们自己来考虑也不是不行。\n\
    我的妈呀, B站up设计学姐和她的程序员朋友开发的完全免费素材网, 放心绝对免费, 因为甚至连注册账号都不需要\n\
    up主页: https://space.bilibili.com/35864444 \n\
\n\
9, 自己传网盘的音效(链接: https://pan.baidu.com/s/1ttxbGoWCi6rXzDCn63UlQw?pwd=1111 )\n\
    我自己平时用的都是, 有的我翻译分类了, 音效太细碎, 压缩包自己下载吧\n\
\n\
10, 在线免费翻译字幕(链接: https://translate-subtitles.com/zh-CN )\n\
    贡献: {name['hxd_2']}\n\
    “这个简单的工具允许您将 SRT 字幕文件翻译成 Google Translate 支持的任何语言。”\n\
",
    # list_6
    6: f"Adobe全家桶、c4d、补帧软件等\n\
\n\
1, Adobe全家桶, 2015, 2017-2024全版本(贡献: {name['Re']}, {name['咸的慌鱼']}): \n\
	百度网盘: https://pan.baidu.com/s/1oA9L2pe4aQ7L6g8R08jObw?pwd=1111 \n\
	阿里云盘: https://www.alipan.com/s/hXEHs87VSEQ \n\
\n\
2, Topaz Video Ai 视频超分补帧(贡献: {name['Re']}): \n\
	百度网盘: https://pan.baidu.com/s/1iZ5ixb8sT0xZx-gc2GBY-w?pwd=1111 \n\
\n\
3, C4d, qbittorrent, 小丸工具箱(贡献: {name['C神']}): \n\
	百度网盘: https://pan.baidu.com/share/init?surl=N8YWTlSKD18t8yRCdOm9uA&pwd=83f9 \n\
\n\
4, E3d(贡献: {name['C神']}): \n\
	百度网盘: https://pan.baidu.com/s/1SeYA4pyQcIWG3LemoGq97Q?pwd=mex7 \n\
\n\
5, ae插件(贡献: {name['C神']}): \n\
	百度网盘: https://pan.baidu.com/s/1yJSA9Jq4SRzUbjXJhg4p_Q?pwd=8wqs\
",
    # list_7
    7: f"AE导不出的问题(总结: {name['C神']}): \n\
\n\
1: ae问题\n\
2: mp4没有破解\n\
3: 效果像素超纲(x50000x)\n\
4: 不是新建合成(打开ae面前有两个选项打开左边)\n\
5: 素材不能拖进AE, 要不然就导不出\n\
6: AE的mp4不能装在Program files(X86)要不然无效\n\
7: MP4的文件补丁在'C盘磁盘路径: program files-Adobe-Common-plug ins-7.0-mediacore'里面有一个autokroma aftercodecs, 这就是mp4文件夹, 稳定磁盘是C盘也是这个文件路径。删除了就不会出现MP4这个插件\n\
",
    # list_8
    8: f"音频处理网站: \n\
\n\
1, 分离人声[AI](免费)(https://vocalremover.org/zh/ )\n\
    界面简洁明了, 非常好用。曾经要vip, 现在免费。网站原话: '尽管此服务复杂且成本高, 但你仍然可以完全免费使用它。处理通常需要10秒左右。'\n\
\n\
2, 人声去除器和AI只能伴奏分离器(付费, 听个响)(https://www.lalal.ai/ )\n\
    怎么说呢, 功能完全被上一条覆盖还要钱, 不开会员一次一分钟还不能下载。留着吧, 收费网站很难倒闭当备用吧\n\
\n\
3, 免费去人声(https://dialogue.moe/ )\n\
    如名字, 免费去人声(贡献: {name['咸的慌鱼']})\n\
\n\
4, 克隆人声(https://kevinwang676-openvoice.hf.space/ )\n\
    需要大概20s音源, 效果蛮好(贡献: {name['hxd_2']})\n\
",
    # list_9
    9:f"Adobe常用插件目录\n\
(用度盘是因为资源网站和我都常用度盘, 要其他网盘或者插件艾特Re, 新找的插件都会存档到机器人)\n\
查看方法: list 9_X\n\
\n\
第一页(9_1): \n\
1, 红巨星, uni前缀的插件\n\
2, 蓝宝石, S_前缀的插件\n\
3, Deepglow (发光)\n\
4, Saber (光效)\n\
5, Twixtor Pro (补帧)\n\
\n\
第二页(9_2): \n\
6, loopflow (纹理流动)\n\
7, Atom, 预设管理 (带预设)\n\
8, BCC插件\n\
",
    9_1: f"Adobe常用插件第一页: \n\
\n\
1, 红巨星宇宙特效套装插件Universe(Ae、Pr通用, 收集: {name['Re']})\n\
    百度网盘: 链接: https://pan.baidu.com/s/1dEiPEVWbyt_cBI7073Nu0g?pwd=1111 \n\
\n\
2, 蓝宝石插件BorisFX.Sapphire(Ae、Pr通用, 收集: {name['Re']})\n\
    百度网盘: 链接: https://pan.baidu.com/s/1dGx3GA0tjbyW51LpHThWyg?pwd=1111 \n\
\n\
3, 发光插件Deepglow(Ae, 收集: {name['Re']})\n\
    百度网盘: 链接: https://pan.baidu.com/s/1PQdyo0basF9a8-f_ieu2eA?pwd=1111 \n\
\n\
4, 能量激光描边光效特效Saber(Ae, 收集: {name['Re']})\n\
    百度网盘: 链接: https://pan.baidu.com/s/1OX01XwHR_JnLGbi2hfunfA?pwd=1111 \n\
\n\
5, 变速插件Twixtor Pro 7.5.5 Win中文版(Ae、Pr通用, 购买: {name['Re']})\n\
    百度网盘: 链接: https://pan.baidu.com/s/1YeNrOKlDyDZG_ltOv405iw?pwd=1111 \n\
",
    9_2: f"Adobe常用插件第二页: \n\
\n\
6, 纹理流动, 静态转动态插件loopflow(Ae, 收集: {name['Re']})\n\
    阿里云盘: https://www.aliyundrive.com/s/fe3DqWUxbEM \n\
    百度网盘: https://pan.baidu.com/s/142lr6tSo1d6z1DkuZSh_Cw?pwd=2022 \n\
\n\
7, 预设管理插件以及它的众多预设AtomX(Ae、Pr通用, 收集: {name['Re']})\n\
    百度网盘: https://pan.baidu.com/s/1TeZO-D8-aiXye85ykuQP1w?pwd=1111 \n\
\n\
8, BCC插件Boris FX Continuum Complete(Ae, Pr通用, 收集: {name['Re']})\n\
    百度网盘: https://pan.baidu.com/s/1thKiNEyqF6KQWbHf5yJDZw?pwd=1111 \n\
",
    # list_10
    10: f"设计, 出版等, 字体相关: \n\
\n\
1, 庞门正道的免费字体库, 包括庞门正道, 思源黑体, 胡晓波免费字体, 以及数十种免费西文字体: \n\
    https://pan.baidu.com/s/1kscd-WbOaeQv3yYXfNi30Q?pwd=PMZD#list/path=%2F \n\
\n\
2, 中文免版权可商用字体: \n\
    https://www.100font.com/ \n\
\n\
3, 英文免版权可商用字体: \n\
    https://www.fontsquirrel.com/ \n\
",
    # list_11
    11: f"魔法上网, 目前收藏的机场(请私聊Re细说): \n\
1, 一元机场\n\
    价格: 12元/年;20元/2年(500G/月, 他说不限速实测速度大于200Mbps, 后同), 15元/季(400G/月, 不限速), 7元/月(8000G/月, 不限速)\n\
    体验: \n\
        优点: 便宜, 使用起来访问网站和视频都挺好, 没有转圈加载不慢的情况\n\
        缺点: 延迟1000-4000ms, 节点很多时候会挂一大半, 虽然不会全挂就是了\n\
\n\
2, Global-Fast\n\
    价格: 15/月;40/季(200G/月, 5000Mbps), 还有好多懒得写了\n\
    体验: \n\
        优点: 速度快延迟不高, 延迟基本在100, 最多不超过500ms, 速度也快, 爽的起飞\n\
        缺点: 或许他的价格是缺点, 体验真的很棒\n\
\n\
3, 免费云\n\
    价格: 0元/永久(100G/月, 限速10Mbps), 88元/年(150G/月, 限速200Mbps)\n\
    体验: 我没用过, 体验暂无, 你可以试试回头告诉我\n\
\n\
4, 金坷垃, 提供: {name['恐龙']}\n\
    价格: 12/月(节日八折)\n\
    体验: 他们每个节日都做活动, 全场8折还是能便宜不少的,最大的问题是大部分都是中转而且欧美节点比较少\n\
",
}


menu = on_startswith({'list', 'menu', '神奇列表'}, rule=check_group)


@menu.handle()
async def c(event: V11MessageEvent | V12MessageEvent):
    # 正则匹配list后的包含下划线的数字，str为对象返回值，然后取'text':'后面的部分，在用第二个'分割去前面，得到干净的源文本
    # str示例：<bound method Message.extract_plain_text of [MessageSegment(type='text', data={'text': 'raw'})]>
    page = findall("^list[_\s]*(\d+(?:_\d+)*)$", str(event.get_message().extract_plain_text).split("text': '")[1].split("'")[0])
    if page:
        
        await menu.finish(
            txt[int(page[0])]
        )


@menu.got('page', prompt=txt['menu'])
async def c(page: str = ArgPlainText('page')):
    # 如果输入数字，则输出对应页数，否则按list开头处理
    try:
        await menu.send(
            txt[int(page)]
        )
    except Exception as e:
        # 判断是否为list开头，如果不是则没有返回
        a = findall("^list[_\s]*(\d+(?:_\d+)*)$", page)
        if a:
            await menu.send(
                txt[int(a[0])]
            )
        elif page in ['神奇列表', 'list', 'menu']:
            await menu.send(
                '健忘是吧, 看完菜单就忘了'
            )
        else:
            return
        return
