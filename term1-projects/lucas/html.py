Html1="""
	<style>
	body {
	background-image: url("""
Htmlcolor=""");
background-color:"""
Html2=""";
-moz-background-size: cover;
-webkit-background-size: cover;
background-size: cover;
background-position: top center !important;
background-repeat: no-repeat !important;
background-attachment: fixed;
color:
"""
Htmlfont=""";
font-family:"""
Htmlsize=""";
font-size:"""
Html25="""%;

}
</style>
<body>
<center><h1>"""
Html3="""</h1></center><p>"""
Html4="""</p>"""
Html45="""
<iframe width="560" height="315" src="https://www.youtube.com/embed/"""
Html5=""""frameborder="0" allowfullscreen></iframe>"""
Html6="""<div><img src="""
Html7=""" alt="""
Html8="""></div>"""
Htmllast="""
</body>
"""
subHtml="""
	<form action=/page method=post>
	<input name=pic placeholder="Background image address">
	<input name=bcolor placeholder="Background color">
	<input name=head placeholder="Heading">
	<input name=para placeholder="Paragraph">
	<input name=color placeholder="Text color">
	<input name=url placeholder="Video url">
	<input name=font placeholder="Text font family">
	<input name=size placeholder="Text size">
	<input name=img placeholder="Image url">
	<input name=alt placeholder="Alternate image text">
	<input type="submit">
</form>"""
def output(self):
		url=str(self.request.get("url")).split('=')
		pic=self.request.get("pic")
		head=self.request.get("head")
		para=self.request.get("para")
		color=self.request.get("color")
		font=self.request.get("font")
		size=self.request.get("size")
		img=self.request.get("img")
		alt=self.request.get("alt")
		bcolor=self.request.get("bcolor")
		if url[0]=='https://www.youtube.com/watch?v':
			self.response.write(Html1+str(pic)+Htmlcolor+str(bcolor)+Html2+str(color)+Htmlfont+str(font)+Htmlsize+str(size)+Html25+str(head)+Html3+str(para)+Html4+Html45+str(url[1])+Html5+Html6+'"'+str(img)+'"'+Html7+'"'+str(alt)+'"'+Html8+Htmllast)
		else:
			self.response.write(Html1+str(pic)+Htmlcolor+str(bcolor)+Html2+str(color)+Htmlfont+str(font)+Htmlsize+str(size)+Html25+str(head)+Html3+str(para)+Html4+Html6+'"'+str(img)+'"'+Html7+'"'+str(alt)+'"'+Html8+Htmllast)
