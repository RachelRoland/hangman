<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<html><head><title>Python: module Hangman</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head><body bgcolor="#f0f0f8">

<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="heading">
<tr bgcolor="#7799ee">
<td valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial">&nbsp;<br><big><big><strong>Hangman</strong></big></big></font></td
><td align=right valign=bottom
><font color="#ffffff" face="helvetica, arial"><a href=".">index</a><br><a href="file:c%3A%5Cusers%5Cmedinady%5Cprogramming%5Changman%5Changman.py">c:\users\medinady\programming\hangman\hangman.py</a></font></td></tr></table>
    <p></p>
<p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#aa55cc">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial"><big><strong>Modules</strong></big></font></td></tr>
    
<tr><td bgcolor="#aa55cc"><tt>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</tt></td><td>&nbsp;</td>
<td width="100%"><table width="100%" summary="list"><tr><td width="25%" valign=top><a href="random.html">random</a><br>
</td><td width="25%" valign=top></td><td width="25%" valign=top></td><td width="25%" valign=top></td></tr></table></td></tr></table><p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#ee77aa">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#ffffff" face="helvetica, arial"><big><strong>Classes</strong></big></font></td></tr>
    
<tr><td bgcolor="#ee77aa"><tt>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</tt></td><td>&nbsp;</td>
<td width="100%"><dl>
<dt><font face="helvetica, arial"><a href="builtins.html#object">builtins.object</a>
</font></dt><dd>
<dl>
<dt><font face="helvetica, arial"><a href="Hangman.html#Hangman">Hangman</a>
</font></dt></dl>
</dd>
</dl>
 <p>
<table width="100%" cellspacing=0 cellpadding=2 border=0 summary="section">
<tr bgcolor="#ffc8d8">
<td colspan=3 valign=bottom>&nbsp;<br>
<font color="#000000" face="helvetica, arial"><a name="Hangman">class <strong>Hangman</strong></a>(<a href="builtins.html#object">builtins.object</a>)</font></td></tr>
    
<tr><td bgcolor="#ffc8d8"><tt>&nbsp;&nbsp;&nbsp;</tt></td><td>&nbsp;</td>
<td width="100%">Methods defined here:<br>
<dl><dt><a name="Hangman-__init__"><strong>__init__</strong></a>(self)</dt><dd><tt>Initialize&nbsp;self.&nbsp;&nbsp;See&nbsp;help(type(self))&nbsp;for&nbsp;accurate&nbsp;signature.</tt></dd></dl>

<dl><dt><a name="Hangman-display_game"><strong>display_game</strong></a>(self)</dt><dd><tt>Display&nbsp;method&nbsp;displays&nbsp;the&nbsp;game.</tt></dd></dl>

<dl><dt><a name="Hangman-display_statistics"><strong>display_statistics</strong></a>(self)</dt><dd><tt>Displays&nbsp;the&nbsp;game&nbsp;statistics.</tt></dd></dl>

<dl><dt><a name="Hangman-guess"><strong>guess</strong></a>(self, let)</dt><dd><tt>Guess&nbsp;is&nbsp;how&nbsp;the&nbsp;game&nbsp;play&nbsp;works.&nbsp;Notice,&nbsp;the&nbsp;UI&nbsp;is&nbsp;not&nbsp;part&nbsp;of&nbsp;this&nbsp;method.<br>
We&nbsp;leave&nbsp;that&nbsp;to&nbsp;the&nbsp;main.py&nbsp;file.</tt></dd></dl>

<dl><dt><a name="Hangman-initialize_file"><strong>initialize_file</strong></a>(self, filename)</dt><dd><tt>Initializes&nbsp;the&nbsp;word&nbsp;data&nbsp;structure&nbsp;from&nbsp;the&nbsp;file.</tt></dd></dl>

<dl><dt><a name="Hangman-new_word"><strong>new_word</strong></a>(self)</dt><dd><tt>Selects&nbsp;a&nbsp;random&nbsp;word&nbsp;from&nbsp;the&nbsp;words&nbsp;data&nbsp;structure</tt></dd></dl>

<dl><dt><a name="Hangman-reveal_word"><strong>reveal_word</strong></a>(self)</dt><dd><tt>Reveals&nbsp;the&nbsp;word.</tt></dd></dl>

<hr>
Data descriptors defined here:<br>
<dl><dt><strong>__dict__</strong></dt>
<dd><tt>dictionary&nbsp;for&nbsp;instance&nbsp;variables&nbsp;(if&nbsp;defined)</tt></dd>
</dl>
<dl><dt><strong>__weakref__</strong></dt>
<dd><tt>list&nbsp;of&nbsp;weak&nbsp;references&nbsp;to&nbsp;the&nbsp;object&nbsp;(if&nbsp;defined)</tt></dd>
</dl>
<hr>
Data and other attributes defined here:<br>
<dl><dt><strong>ALPHA_SIZE</strong> = 26</dl>

<dl><dt><strong>AlphaInfo</strong> = &lt;class 'Hangman.AlphaInfo'&gt;<dd><tt><a href="#Hangman-AlphaInfo">AlphaInfo</a>(letter,&nbsp;is_available)</tt></dl>

<dl><dt><strong>BODY_SIZE</strong> = 9</dl>

<dl><dt><strong>BodyPart</strong> = &lt;class 'Hangman.BodyPart'&gt;<dd><tt><a href="#Hangman-BodyPart">BodyPart</a>(first,&nbsp;second,&nbsp;third,&nbsp;display_two,&nbsp;display_three)</tt></dl>

<dl><dt><strong>WORD_LIST_SIZE</strong> = 100</dl>

<dl><dt><strong>WordInfo</strong> = &lt;class 'Hangman.WordInfo'&gt;<dd><tt><a href="#Hangman-WordInfo">WordInfo</a>(word,&nbsp;is_available)</tt></dl>

<dl><dt><strong>alphabet</strong> = []</dl>

<dl><dt><strong>body</strong> = []</dl>

<dl><dt><strong>current_word</strong> = ''</dl>

<dl><dt><strong>game_over</strong> = False</dl>

<dl><dt><strong>game_won</strong> = False</dl>

<dl><dt><strong>games_lost</strong> = 0</dl>

<dl><dt><strong>games_won</strong> = 0</dl>

<dl><dt><strong>num_words_available</strong> = 0</dl>

<dl><dt><strong>num_words_read</strong> = 0</dl>

<dl><dt><strong>words</strong> = []</dl>

</td></tr></table></td></tr></table>
</body></html>