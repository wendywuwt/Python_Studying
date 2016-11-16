def main():
    text = '''  The King and Queen of Hearts were seated on their throne when they arrived,
with a great crowd assembled about them--all sorts of little birds and beasts,   
as well as the whole pack of cards: the Knave was standing before them, in  
chains, with a soldier on each side to guard him; and near the King was the    
White Rabbit, with a trumpet in one hand, and a scroll of parchment in the     
other. In the very middle of the court was a table, with a large dish of tarts
upon it: they looked so good, that it made Alice quite hungry to look at them--   
`I wish they'd get the trial done,' she thought, `and hand round the     
refreshments!'

  But there seemed to be no chance of this, so she began looking at everything   
about her, to pass away the time.
'''
    listlines = (text.split('\n'))
    temp = 0
    lista = []
    for listline in listlines:

        # listline里每一行都去掉右边的空格，并存在lista中
        stra = listline.rstrip()
        lista.append(stra)

        # 计算lista中最长的串
        if( len(stra) > temp):
            temp = len(stra)
        

    str1 = '+'+ '-' * temp + '+'

    print(str1)

    for item in lista:
        print('|'+item.ljust(temp,' ')+'|')

    print(str1)



if __name__ == '__main__':
    main()
            
