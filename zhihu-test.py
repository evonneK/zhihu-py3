#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = '7sDream'

import zhihu
import os
import shutil


def test_question():
    url = 'http://www.zhihu.com/question/24825703'
    question = zhihu.Question(url)

    # 获取该问题的详细描述
    print(question.title)
    # 亲密关系之间要说「谢谢」吗？

    # 获取该问题的详细描述
    print(question.details)
    # 从小父母和大家庭里，.......什么时候不该说"谢谢”？？

    # 获取回答个数
    print(question.answer_num)
    # 174

    # 获取关注该问题的人数
    print(question.follower_num)
    # 1419

    # 获取该问题所属话题
    print(question.topics)
    # ['心理学', '恋爱', '社会', '礼仪', '亲密关系']

    # 获取排名第一的回答
    print(question.top_answer)
    # <zhihu.Answer object at 0x03D28810>

    # 获取排名前十的十个回答
    print(question.top_i_answers(10))
    # <generator object top_i_answers at 0x0391DDF0>

    # 获取所有回答
    print(question.answers)
    # <generator object answers at 0x0391DDF0>

    # generator 对象可迭代：
    for answer in question.answers:
        # do something with answer
        print(answer.author.name, answer.upvote_num)
        pass
    # 小不点儿 197
    # 龙晓航 49
    # 芝士就是力量 89
    # 欧阳忆希 424


def test_answer():
    url = 'http://www.zhihu.com/question/24825703/answer/30975949'
    answer = zhihu.Answer(url)

    # 获取答案url
    print(answer.url)

    # 获取该答案所在问题
    print(answer.question)
    # <zhihu.Question object at 0x02E7E4F0>

    # 获取该答案作者
    print(answer.author)
    # <zhihu.Author object at 0x02E7E110>

    # 获取答案赞同数
    print(answer.upvote_num)
    # 107

    # 获取答案内容的HTML
    print(answer.content)
    # <html>
    # ....
    # </html>

    # 保存HTML
    answer.save(filepath='.')
    # 当前目录下生成 "亲密关系之间要说「谢谢」吗？ - 甜阁下.html"

    # 保存markdown
    answer.save(filepath='.', mode="md")
    # 当前目录下生成 "亲密关系之间要说「谢谢」吗？ - 甜阁下.md"

    # Question 和 Author object 可执行相应操作，如：

    print(answer.question.title)
    # 亲密关系之间要说「谢谢」吗？

    print(answer.author.name)
    # 甜阁下


def test_author():
    url = 'http://www.zhihu.com/people/7sdream'
    author = zhihu.Author(url)
    # 获取用户名称
    print(author.name)
    # 7sDream

    # 获取用户介绍
    print(author.motto)
    # 二次元新居民/软件爱好者/零回答消灭者

    # 获取用户关注人数
    print(author.followee_num)
    # 66

    # 获取用户粉丝数
    print(author.follower_num)
    # 179

    # 获取用户得到赞同数
    print(author.upvote_num)
    # 1078

    # 获取用户得到感谢数
    print(author.thank_num)
    # 370

    # 获取用户提问数
    print(author.question_num)
    # 16

    # 获取用户答题数
    print(author.answer_num)
    # 227

    # 获取用户专栏文章数
    print(author.post_num)
    # 0

    # 获取用户收藏夹数
    print(author.collection_num)
    # 5

    # 获取用户所有提问
    print(author.questions)
    # <generator object questions at 0x0156BF30>

    # 获取用户所有回答
    print(author.answers)
    # <generator object answers at 0x0156BF30>

    # 获取用户所有收藏夹
    print(author.collections)
    # <generator object collections at 0x0156BF30>

    # 对 generator 可执行迭代操作， 这里用Collection举例
    for collection in author.collections:
        print(collection.name)
    # 教学精品。
    # 可以留着慢慢看～
    # OwO
    # 一句。
    # Read it later

    # 获取用户专栏文章
    print(author.columns)

    # columns 也可以进行迭代操作
    for column in author.columns:
        print(column.name)

    # 获取用户动态
    for act in author.activities:
        if act.type == zhihu.ActType.FOLLOW_COLUMN:
            print('%s 在 %s 关注了专栏 %s' %
                  (author.name, act.time, act.column.name))
        elif act.type == zhihu.ActType.FOLLOW_QUESTION:
            print('%s 在 %s 关注了问题 %s' %
                  (author.name, act.time, act.question.title))
        elif act.type == zhihu.ActType.ASK_QUESTION:
            print('%s 在 %s 提了个问题 %s' %
                  (author.name, act.time, act.question.title))
        elif act.type == zhihu.ActType.UPVOTE_POST:
            print('%s 在 %s 赞同了专栏 %s 中 %s 的文章 %s, 此文章赞同数 %d, 评论数 %d' %
                  (author.name, act.time, act.post.column.name,
                   act.post.author.name, act.post.title, act.post.upvote_num,
                   act.post.comment_num))
        elif act.type == zhihu.ActType.UPVOTE_ANSWER:
            print('%s 在 %s 赞同了问题 %s 中 %s(motto: %s) 的回答, 此回答赞同数 %d' %
                  (author.name, act.time, act.answer.question.title,
                   act.answer.author.name, act.answer.author.motto,
                   act.answer.upvote_num))
        elif act.type == zhihu.ActType.ANSWER_QUESTION:
            print('%s 在 %s 回答了问题 %s 此回答赞同数 %d' %
                  (author.name, act.time, act.answer.question.title,
                   act.answer.upvote_num))
        elif act.type == zhihu.ActType.FOLLOW_TOPIC:
            print('%s 在 %s 关注了专栏 %s' %
                  (author.name, act.time, act.topic.name))


def test_collection():
    url = 'http://www.zhihu.com/collection/37770691'
    collection = zhihu.Collection(url)

    # 获取收藏夹名字
    print(collection.name)
    # 教学精品。

    # 获取收藏夹关注人数
    print(collection.follower_num)
    # 教学精品。

    # 获取收藏夹创建者
    print(collection.owner)
    # <zhihu.Author object at 0x03EFDB70>

    # 获取收藏夹内所有答案
    print(collection.answers)
    # <generator object answers at 0x03F00620>

    # 获取收藏夹内所有问题
    print(collection.questions)
    # <generator object questions at 0x03F00620>

    # Author 对象 和 questions generator 用法见前文


def test_column():
    url = 'http://zhuanlan.zhihu.com/xiepanda'
    column = zhihu.Column(url)

    # 获取专栏名
    print(column.name)
    # 谢熊猫出没注意

    # 获取关注人数
    print(column.follower_num)
    # 63742

    # 获取文章数量
    print(column.post_num)
    # 66

    # 获取所有文章
    print(column.posts)
    # <generator object posts at 0x0521F2D8>

    # posts 是可迭代的 Post 对象集合
    for post in column.posts:
        print(post.title)
    # 伦敦，再见。London, Pride.
    # 为什么你来到伦敦?——没有抽到h1b
    # “城邦之国”新加坡强在哪？
    # ...
    # 华盛顿纪念碑综合症


def test_post():
    url = 'http://zhuanlan.zhihu.com/xiepanda/19950456'
    post = zhihu.Post(url)

    # 获取文章地址
    print(post.url)

    # 获取文章标题
    print(post.title)
    # 为什么最近有很多名人，比如比尔盖茨，马斯克、霍金等，让人们警惕人工智能？

    # 获取所在专栏
    print(post.column)
    # <zhihu.Column object at 0x0600AF90>

    # 获取作者
    print(post.author)
    # <zhihu.Author object at 0x0600AD90>

    # 获取赞同数
    print(post.upvote_num)
    # 15326

    # 获取评论数
    print(post.comment_num)
    # 1517

    # 保存为 markdown
    post.save(filepath='.')
    # 当前目录下生成
    # 为什么最近有很多名人，比如比尔盖茨，马斯克、霍金等，让人们警惕人工智能？ - 谢熊猫君.md

if os.path.exists("test"):
    shutil.rmtree("test")

os.mkdir("test")
os.chdir("test")

test_question()
test_answer()
test_author()
test_collection()
test_column()
test_post()
