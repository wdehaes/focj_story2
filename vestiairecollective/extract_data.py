from bs4 import BeautifulSoup
import json

products = {}
for i in range(1, 26):
  filepath = "html/page_{}.html".format(str(i))
  with open(filepath) as fp:
    html = fp.read()

  soup = BeautifulSoup(html, "lxml")
  product_wrappers = soup.find_all(
      "vc-catalog-snippet", class_="catalog__product")
  print(len(product_wrappers))
  for product_wrapper in product_wrappers:
    product_ref = product_wrapper.find(
        "a")['href']
    print(product_ref)
    product_sku = product_ref[-13:-6]
    print(product_sku)
    product_tag_html = product_wrapper.find_all(
        "span", class_="tag")
    product_tags = [tag.text.strip() for tag in product_tag_html]
    print(product_tags)
    # product_info = product_wrapper.find("div", class_="productSnippet__infos")
    # print(product_info.text.strip())
    product_brand = product_wrapper.find(
        "span", class_="productSnippet__text--brand").text.strip()
    product_name = product_wrapper.find(
        "span", class_="productSnippet__text--name").text.strip()
    # product_size = product_wrapper.find(
    #     "span", class_="productSnippet__size").text.strip()
    product_price = product_wrapper.find(
        "span", class_="productSnippet__price").text.strip()
    product = {'name': product_name, 'tags': product_tags, 'brand': product_brand, 'sku': product_sku, 'price': product_price }
    if not product_sku in products:
      products[product_sku] = product

with open('vestiaire.json', 'w') as fp:
    json.dump(products, fp)
