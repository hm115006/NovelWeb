// JavaScript Document
import document
document.writeln("<ul>");
document.writeln("<li><span class=\"fl\">背景：</span>");
document.writeln("<div class=\"fl\"><input id=\"bg1\" onclick=\"setBG('#dcecf5')\" type=\"button\" class=\"setBG\" />");
document.writeln("<input id=\"bg2\" onclick=\"setBG('#e1ffe6')\" type=\"button\" class=\"setBG\" />");
document.writeln("<input id=\"bg3\" onclick=\"setBG('#edf6d0')\" type=\"button\" class=\"setBG\" />");
document.writeln("<input id=\"bg4\" onclick=\"setBG('#eae8f7')\" type=\"button\" class=\"setBG\" />");
document.writeln("<input id=\"bg5\" onclick=\"setBG('#f5f1e7')\" type=\"button\" class=\"setBG\" />");
document.writeln("<input id=\"bg6\" onclick=\"setBG('#ebf4ef')\" type=\"button\" class=\"setBG\" />");
document.writeln("<input id=\"bg7\" onclick=\"setBG('#FFFFFF')\" type=\"button\" class=\"setBG\" /></div>");
document.writeln("</li>");
document.writeln("<li><span class=\"fl\">字体大小：</span>");
document.writeln("<input type='range' name='fontsize' id='fontsize' value='14' style='display:none' readonly min='12' max='30' /></li>");
document.writeln("<li><span class=\"fl\">字体颜色：</span>");
document.writeln("<div class=\"fl\"><select onchange=\"setFontColor(this.value)\" id=\"txtcolor\" name=\"txtcolor\">");
document.writeln("<option value=\"#000000\">黑色</option>");
document.writeln("<option value=\"#ff0000\">红色</option>");
document.writeln("<option value=\"#006600\">绿色</option>");
document.writeln("<option value=\"#0000ff\">蓝色</option>");
document.writeln("<option value=\"#660000\">棕色</option>");
document.writeln("</select></div>");
document.writeln("</li>");
document.writeln("<li id=\"sudu\"><span class=\"fl\">滚动速度：</span><a id=\"sudu50\" href=\"javascript:setSpeed(50);\">快</a><a id=\"sudu100\" href=\"javascript:setSpeed(100);\" class=\"this\">中</a><a id=\"sudu150\" href=\"javascript:setSpeed(150);\">慢</a></li>");
document.writeln("</ul>");