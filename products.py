#檢查檔案是否存在
import os #operating system
products = []
#讀取檔案
def read_file(filename):
    products = []
    with open(filename, 'r', encoding = 'utf-8') as f :   #有時候可能需要加encoding = 'utf-8'
            for line in f:
                if '商品,價格' in line:
                    continue
                name, price = line.strip().split(',')
                products.append([name, price])
    return products

#讓使用者輸入
def user_input(products):
    while True:
        name = input('請輸入商品名稱:')
        if name == 'q':
            break
        price = input('請輸入商品價格:')
        price = int(price)
        products.append([name, price])
        #p = []
        #p.append(name)
        #p.append(price)
        #快寫法 p = [name,price]
        #products.append(p)
        #快寫法 products.append([name, price])
    print(products)
    return products

#印出所有購買記錄
def print_products(products):
    for p in products:
        print(p[0], '的價格是', p[1])

#寫入檔案
def write_file(filename, products):
    with open(filename,'w', encoding = 'utf-8') as f:
        f.write('商品,價格 \n' )
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n')

#主要執行檔案
def main():
    filename = 'products.csv'
    products = []
    if os.path.isfile(filename):  #檢查檔案在不在
        print('找到檔案了')
        products = read_file(filename)
    else:
        print('找不到檔案....')

    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)

main()