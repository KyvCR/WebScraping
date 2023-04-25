import requests
import pandas as pd
import time
import random
import math

base_url = 'https://www.lazada.co.id/beli-handphone/?ajax=true&page=1&spm=a2o4j.home.cate_1.1.666853e0Ybdio4&style=wf'
# url = 'https://www.lazada.co.id/beli-handphone/?ajax=true&page=2&spm=a2o4j.home.cate_1.1.666853e0Ybdio4&style=wf'
# url = 'https://www.lazada.co.id/beli-handphone/?ajax=true&page=3&spm=a2o4j.home.cate_1.1.666853e0Ybdio4&style=wf'

def getUrl():
    #response_json = requests.get(base_url).json()
    # total_product = int(response_json['mainInfo']['totalResults'])
    # total_product_per_page = int(response_json['mainInfo']['pageSize'])
    # total_page= math.ceil(total_product/total_product_per_page)

    urls= []
    for i in range(1, 6):
        url = f'https://www.lazada.co.id/beli-handphone/?ajax=true&page={i}&spm=a2o4j.home.cate_1.1.666853e0Ybdio4&style=wf'
        urls.append(url)
    return urls

def scrapProduct(url):
    response_json = requests.get(url).json()
    list_product = response_json['mods']['listItems']
    product_list = []
    for i in range(0, len(list_product)):
        product_seller        = list_product[i]['sellerName']
        product_brand         = list_product[i]['brandName']
        product_name          = list_product[i]['name']
        product_price         = list_product[i]['price']
        product_location      = list_product[i]['location']
        product_url           = list_product[i]['itemUrl']
        product_list.append(
            (product_seller, product_brand, product_name,  product_price, product_location, product_url)
        )
    return product_list

def dataFrame(product_list):
    df = pd.DataFrame(product_list, columns =['Seller', 'Brand', 'Name', 'Price', 'Location', 'Link'])
    return df

def savetoExcel(df):
    df.to_excel('Product_lazada_get_api_10Page.xlsx', index=False)
    print('Done')
    

if __name__ == '__main__':
    urls = getUrl()
    all_list_product = []
    for i in range(0, len(urls)):
        product = scrapProduct(urls[i])
        time.sleep(random.randint(20,60))
        all_list_product.extend(product)

    df = dataFrame(all_list_product)
    print(df)
    savetoExcel(df)

# # print(response)
# list_product = response_json['mods']['listItems']

# total_product = int(response_json['mainInfo']['totalResults'])
# print(f'total keseluran product = {total_product}')
# total_product_per_page = int(response_json['mainInfo']['pageSize'])
# print(f'total product per page = {total_product_per_page}')
# total_page= int(total_product/total_product_per_page)
# print(f'Total Page = {total_page}')






# product_list = []
# for i in range(0, len(list_product)):
#   product_seller        = list_product[i]['sellerName']
#   product_brand         = list_product[i]['brandName']
#   product_name          = list_product[i]['name']
#   product_price         = list_product[i]['priceShow']
#   product_location      = list_product[i]['location']
#   product_url           = list_product[i]['itemUrl']
#   product_list.append(
#     (product_seller, product_brand, product_name,  product_price, product_location, product_url)
#   )

#  #print(product_list)
# df = pd.DataFrame(product_list, columns =['Seller', 'Brand', 'Name', 'Price', 'Location', 'Link'])
# print(df)