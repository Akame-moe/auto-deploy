from datetime import datetime
import os

def update_change_log():
    with open('changelog.md','r+',encoding='utf-8') as f:
        d = f.read()
        f.seek(0)
        f.truncate(0)
        f.write('updated on {}.\n'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        f.write(d)
        
        
def main():
    update_change_log()
    os.system('git add .')
    
if __name__ == '__main__':
    main()
        