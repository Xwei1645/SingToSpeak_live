# 手工指定额外的拼音规则，目前是两次循环嵌套，算法可以优化.不改变的项留空
# 只能指定儿化，不能取消。er必须是后面接'儿'，词长必须大于1
inf = [('姑娘', [(1, 'niang', None)]), ('知了', [(1, 'liao', None)]), ('太阳', [(1, 'yang', None)]),
                ('月亮', [(1, 'liang', None)]), ('故事', [(1, 'shi', None)]), ('少爷', [(1, 'ye', None)]),
                ('玩儿', [(0, '', True)]), ('鹿尾儿', [(1, 'yi3', None)]), ('鹿尾儿', [(1, 'yi3', None)]),
                ('海蜇', [(1, 'zhe2', None)]), ('东西', [(1, 'xi', None)]), ('衣服', [(1, 'fu', None)]),
                ('肚子', [(0, 'du4', None)]), ('消息', [(1, 'xi', None)]), ('技术', [(1, 'shu', None)]),
                ('看见', [(1, 'jian', None)]), ('谢谢', [(1, 'xie', None)]), ('回来', [(1, 'lai', None)]),
                ('长达', [(0, 'chang2', None)]), ('明白', [(1, 'bai', None)])]