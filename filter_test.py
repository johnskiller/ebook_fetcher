#!/usr/bin/env python
# coding=utf-8
from bs4 import BeautifulSoup, Comment
test='''
<html>
<header>this is header</header>
<body>
<h1>title</h1>
<div class="header">
<ul>
  <script>ShowLogo();</script>
  <ol>
    <p>
      <span class="right"><script>ShowTop();</script></span>
    </p>
    <dl>
      <script>ShowNav();</script>
    </dl>
  </ol>
  <div class="c"></div>
</ul>
</div>

<p style="float:left;"> 
  <a href="http://www.baikm.com/newmessage.php?tosys=1&title=《官场之风流人生》章节出错啦!&content=错误章
节： 第一章 谁会参加自己的葬礼 举报原因如下： " target="_blank">章节错误/举报有奖</a>  
  <a href="http://www.baikm.com/newmessage.php?tosys=1&title=《官场之风流人生》更新太慢啦!&content= 《官场之风流人生》 
最新章节已上线，请及时更新。(请您最好告诉我们现在有哪个网站更新速度比我们快，以便我们更快的更新)。 以下网站比藏书阁更新的快: " target="_blank">更新慢了/举报有奖</a>

<div id="content" style="font-size:16px;">
&nbsp;&nbsp;&nbsp;&nbsp;更新时间：2012-06-27<br />
<br />&nbsp;&nbsp;&nbsp;&nbsp;谁会静坐在车里等待参加自己的葬礼？<br />
<br />&nbsp;&nbsp;&nbsp;&nbsp;沈淮坐在车里，看着窗外、透过寺前街古榆树荫洒下的太阳光斑，在阴影里斑驳有如琉璃，就像是死亡的沉眠，叫他看了心头空落落的。【藏书阁-无弹窗小说网，永久网址：www.baikm.com,第一时间阅读最新章节!】<br />
<br />&nbsp;&nbsp;&nbsp;&nbsp;后面的塔陵园，有民国时建造的三座佛塔，紧挨着千年古庙天宁寺。<br />
<br />&nbsp;&nbsp;&nbsp;&nbsp;这三座佛塔，原来是民国时东华市最大的民族资本家族，孙家所建的私家佛塔园，曾供金银玉三座观音像，在省内都闻名一时。<br /><br />
</div>
</body>
</html>
'''
VALID_TAGS = {'html': [],
              'head': [],
              'p': [],
              'body': [],
              'title': [],
              'h1': [],
              'br': [],
              #'a': ['href', 'title'],
              'div':['id']
              }
FILE='html/4966416.html'

def sanitize_html(value, valid_tags=VALID_TAGS):
    soup = BeautifulSoup(value)
    comments = soup.findAll(text=lambda text:isinstance(text, Comment))
    [comment.extract() for comment in comments]
    # Some markup can be crafted to slip through BeautifulSoup's parser, so
    # we run this repeatedly until it generates the same output twice.
    newoutput = soup.renderContents()
    while 1:
        oldoutput = newoutput
        soup = BeautifulSoup(newoutput)
        for tag in soup.findAll(True):
            if tag.name not in valid_tags:
                tag.hidden = True
            else:
                print tag.name,'***', tag.attrs
                print tag.name,'###', [x for x in tag.attrs ]
                m={}
                for k in tag.attrs.keys():
                    if k  in valid_tags[tag.name]:
                        m[k] = tag.attrs[k]
                tag.attrs = m
                print tag.name,'===', m
                #tag.attrs = [(attr, value) for attr, value in tag.attrs if attr in valid_tags[tag.name]]
        newoutput = soup.renderContents()
        if oldoutput == newoutput:
            break
    return newoutput

def filte(file=FILE):
    v=open(file).read()
    print sanitize_html(v)

def test():
	v=open(FILE).read()
	soup = BeautifulSoup(v)
	cont=soup.findAll('div',attrs={'id':'content'})
	print cont

filte()
print '================================'
test()
