{% load staticfiles %}
<!DOCTYPE html>
<!--[if lt IE 7 ]><html class="ie ie6"><![endif]-->
<!--[if IE 7 ]><html class="ie ie7"><![endif]-->
<!--[if IE 8 ]><html class="ie ie8"><![endif]-->
<!--[if IE 9 ]><html class="ie ie9"><![endif]-->
<!--[if (gt IE 9)|!(IE)]><!-->
<!--<![endif]-->
<html>
<head>
<script src="js/mm.js" type="text/javascript"></script>
<meta http-equiv="Content-Type" content="text/html; charset=gbk">
<title>全书网</title>
<meta name="keywords" content="" />
<meta name="description" content="全书网提供最新小说，阅读小说就在全书网。" />
<meta name="author" content="http://www.quanshuwang.com" />
<meta name="generator" content="http://www.quanshuwang.com" />
<meta http-equiv="X-UA-Compatible" content="IE=edge" />
<meta name="renderer" content="webkit">
<meta name="applicable-device" content="pc">
<meta name="robots" content="all">
<meta http-equiv="Cache-Control" content="no-transform" />
<meta http-equiv="Cache-Control" content="no-siteapp" />
<!--[if lt IE 9]>
<script src="/kukuku/js/html5.js"></script>
<![endif]-->
<script language="javascript" type="text/javascript"  src="/kukuku/js/jquery-1.js"></script>
<script language="javascript" type="text/javascript"  src="/kukuku/js/index.js"></script>
<script language="javascript" type="text/javascript"  src="/kukuku/ku.js"></script>
<script language="javascript" type="text/javascript" src="/kukuku/js/common.js"></script>
<link href="/kukuku/css/common.css" rel="stylesheet" type="text/css">
<link href="/kukuku/css/board.css" rel="stylesheet" type="text/css">
<link href="/kukuku/css/book.css" rel="stylesheet" type="text/css">
</head>
<body>
<div id="wrapper">
  <div class="shadow"></div>
  <header id="global-head">
    <div>
      <nav class="site-navigation cf">
	  <a class="home" href="http://www.quanshuwang.com">首页</a>
	  <a href="/shuku/">书库榜单</a>
	  <a href="http://m.quanshuwang.com">全书手机站</a>
	  </nav>
     <div class="hd-follow" style="width:400px;">
	<div class="myhide"><a href="javascript:;" class="hides">浏览记录</a>
		<div class="hideInfo">
		<script type="text/javascript" src="/kukuku/js/json2.js"></script>
		<script type="text/javascript" src="/kukuku/js/readshow.js"></script>
		<p>*提示：浏览记录仅放置最近浏览的10本书籍</p>
		</div>
	</div>
        <span id="checklogin">
			<script language="javascript" src="/kukuku/js/denglu.js"></script>
		</span>
		</div>
    </div>
    <p class="site-logo"><a href="http://www.quanshuwang.com" title="全书网"><img src="/kukuku/images/logo-medium.jpg" alt="全书网 - logo"></a></p>
    <div class="site-search">
       <form action="http://www.quanshuwang.com/modules/article/search.php" method="get" target="_blank">
       <input name="searchkey" type="text" id="bdcsMain" onFocus="this.classname='over';if (value =='这是一个神奇的搜索'){value =''}" onBlur="this.classname='input'"  value="这是一个神奇的搜索" />
        <span style="display:none;">
        <select name="searchtype" id="select" class="searchtype">
          <option value="articlename" selected="selected">文章名称</option>
          <option value="author">文章作者</option>
        </select>
        </span>
        <input type="image" name="searchbuttom" id="searchbuttom" src="/kukuku/images/search.jpg" />
      </form>
    </div>
</header>
  <div id="channel-header" class="clearfix">
    <div class="channel-header-wrapper">
      <div class="channel-logo"><a href="http://www.quanshuwang.com" title="全书网">全书网</a></div>
      <nav class="channel-nav">
        <ul class="channel-nav-list">
  <li><a href="http://www.quanshuwang.com/list/1_1.html">玄幻魔法</a></li>
  <li><a href="http://www.quanshuwang.com/list/2_1.html">武侠修真</a></li>
  <li><a href="http://www.quanshuwang.com/list/3_1.html">纯爱耽美</a></li>
  <li><a href="http://www.quanshuwang.com/list/4_1.html">都市言情</a></li>
  <li><a href="http://www.quanshuwang.com/list/5_1.html">职场校园</a></li>
  <li><a href="http://www.quanshuwang.com/list/6_1.html">穿越重生</a></li>
  <li><a href="http://www.quanshuwang.com/list/7_1.html">历史军事</a></li>
  <li><a href="http://www.quanshuwang.com/list/8_1.html">网游动漫</a></li>
  <li><a href="http://www.quanshuwang.com/list/9_1.html">恐怖灵异</a></li>
  <li><a href="http://www.quanshuwang.com/list/10_1.html">科幻小说</a></li>
  <li><a href="http://www.quanshuwang.com/list/11_1.html">美文名著</a></li>
  <li><a href="http://www.quanshuwang.com/list/12_1.html">热门推荐</a></li>
        </ul>
      </nav>
    </div>
  </div>
  
  
<br /><br />
<form name="articlesearch" method="post" action="http://www.quanshuwang.com/modules/article/search.php">
 <table class="grid" width="250" align="center">
   <caption>小说搜索</caption>
    <tr align="center">
      <td><table width="100%" class="hide" border="0" cellspacing="0" cellpadding="5">
        <tr>
          <td width="37%" align="right" valign="middle">条　件：</td>
          <td width="63%">
		  <select name="searchtype" id="searchtype" class="select">
		  <option value="all" selected="selected">综合</option>
		  <option value="articlename">小说名称</option>
		  <option value="author">小说作者</option>
		  <option value="keywords">关键字</option>
		  </select>
          </td>
        </tr>
        <tr>
          <td align="right" valign="middle">关键字：</td>
          <td><input name="searchkey" type="text" class="text" id="searchkey" size="10" maxlength="50"></td>
        </tr>
        <tr>
		  <td><input type="hidden" name="action" value="search"></td>
          <td><input type="submit" class="button" value="&nbsp;搜&nbsp;&nbsp;索&nbsp;" name="submit"></td>
          </tr>
      </table></td>
    </tr>
  </table>
</form>
<br /><br />
    <footer id="global-foot"> &#169;Copyright http://www.quanshuwang.com 全书网 2012, All rights reserved <br>全书网小说均由网友转载于网络，若转载中的书本侵犯了您的权益，请于本站管理员联系。 邮箱：quanshunet@gmail.com<br>
  <a href="/api/baidu_sitemap.php?page=1&update=2" target="_blank">Sitemap</a> | <a href="/map/1.html" target="_blank">网站地图</a> | <script type="text/javascript">tongji();</script>  |  蜀ICP备12018289号-3
  </footer>
<script type="text/javascript">duilian();</script>
<script type="text/javascript">baidusearch();</script>
</body>
</html>