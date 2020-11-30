import os
import json
import codecs

catalog_tpl = """
			<div class="title">
				<h3>我们的产品</h3>
			</div>
			<div class="features-info">
            """


product_tpl = """
<div class="col-md-{col} features-grids wow bounceIn animated" data-wow-delay=".5s" style="visibility: visible; -webkit-animation-delay: .5s;">
    <figure class="effect-bubba" style="text-align: -webkit-center;    background-color: #f7f7f7;">
        <img src="images/products/{image}" alt="{title}" style="width:auto;height:auto;max-width:100%;max-height:600px;"/>
        <figcaption>
            <h4 style="font-size: 50px;    font-weight: 800;    color: #150202;">{title}</h4>
            <p style="font-size: 24px;    font-weight: 600;    color:#484242;">{catalog}</p>	
        </figcaption>			
    </figure>		
</div>
"""
products = []
with codecs.open("images.html", "w", "utf-8") as wf:
    wf.write(catalog_tpl)
    for image in os.listdir("../images/products"):
        if image.endswith(".png"):
            num,name,catalog = image.rstrip(".png").split("-")
            os.rename("../images/products/"+image,"../images/products/"+ num+".png")
            p = {
                "catalog": catalog,
                "name": name,
                "title": name,
                "image": num+".png",
                "col" : 12 if catalog.endswith("组合") else 6,
                "width": "100%",
                "height": 600,
            }
            products.append(p)
            wf.write(product_tpl.format(**p))
    wf.write('<div class="clearfix"> </div></div>')
        				
with codecs.open("products.json", "w", "utf-8") as pf:
    json.dump(products, pf, ensure_ascii=False)



    