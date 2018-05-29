
def main():
    lcdic = ['2593E44A','25938567','25932B7B','259385B8','A57E856C','A57E8568',
             'A57E85B7','A57E8569','A57E85BD','A57E85BA','A57E2B7D','2593E25F',
             '2593E345','2593C5F9','A57E181C','A57E181D','A57E2079','A57E207C',
             'A57E181F','A57E2077','A57E2078','2593C8D3','2593E22D']
    fileObj = open('C:\\Users\\fengjj\\Desktop\\lacciposition_0','rt')
    output = open('C:\\Users\\fengjj\\Desktop\\fshz_lacciposition_0','wt')
    for line in fileObj:
        tmp = line.split(',')
        lacci = tmp[0]
        if lacci in lcdic:
            output.writelines("%s" % line)
    output.close()
            

if __name__ == '__main__':
    main()
